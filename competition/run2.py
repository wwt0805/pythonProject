import warnings
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import mean_squared_error
from lightgbm import LGBMRegressor
import xgboost as xgb

# 定义数据所在路径
TRAIN_PATH = "./data/train.csv"
TEST_PATH = "./data/test.csv"
SUBMIT_PATH = "./data/submit.csv"

# 利用pandas读入csv数据
train_data = pd.read_csv(TRAIN_PATH)
predict_data = pd.read_csv(TEST_PATH)
submit_data = pd.read_csv(SUBMIT_PATH)

total_data = pd.concat([train_data, predict_data], axis=0)
total_data = total_data.replace("西北 北 东北", "西北 北")
total_data = total_data.replace("南 东南", "南")
# total_data['地铁站点'] = total_data['地铁站点'].fillna(0)
# total_data['地铁线路'] = total_data['地铁线路'].fillna(0)
total_data = pd.get_dummies(total_data)


def get_feat2(df):
    # 房间总数
    df['房间总数'] = df['卫的数量'] + df['卧室数量'] + df['厅的数量']
    # 卫的面积
    df['卫的面积'] = df['房屋面积'] * (df['卫的数量'] / df['房间总数'])
    # 卧室面积
    df['卧室面积'] = df['房屋面积'] * (df['卧室数量'] / df['房间总数'])
    # 厅的面积
    df['厅的面积'] = df['房屋面积'] * (df['厅的数量'] / df['房间总数'])
    # 楼层比
    df['楼层比'] = (df['楼层'] + 1) / df['总楼层']
    # 每个小区附近的地铁站点数
    df_temp = df.groupby('小区名')['地铁站点'].count().reset_index()
    df_temp.columns = ['小区名', '地铁站点数量']
    df = df.merge(df_temp, how='left', on='小区名')
    # 每个小区楼房的平均楼层高度
    floor_hmean = df.groupby('小区名')['总楼层'].mean().reset_index()
    floor_hmean.columns = ['小区名', '小区楼房平均高度']
    df = df.merge(floor_hmean, how='left', on='小区名')
    return df


total_data = get_feat2(total_data)

train_data = total_data[:196539]
test_data = total_data[196539:]
X = train_data.drop("Label", axis=1)
print(X.shape)
Y = train_data["Label"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.8, random_state=0)

regressor_lgb = LGBMRegressor(random_state=0)
# params = {"n_estimators": [500, 750, 1000, 1250, 1500, 1750, 2000]}
params = {"n_estimators": [2000]}
model = GridSearchCV(regressor_lgb, params, cv=5)

model.fit(X_train, Y_train)
print(model.score(X_train, Y_train))
print(model.best_score_)
print(model.best_estimator_)

val_lgb = model.predict(X_test)
mse_lgb = mean_squared_error(Y_test, val_lgb)

sub_lgb = model.predict(test_data.iloc[:, :-1])
print('lgb模型运行完成！')


def get_submit(submit_data, result, save_path):
    submit = pd.DataFrame()
    submit['ID'] = submit_data.ID
    submit['Label'] = result
    submit.to_csv(save_path, index=None)
    print('结果已写出！')


get_submit(submit_data, sub_lgb, 'sub_lgb.csv')
