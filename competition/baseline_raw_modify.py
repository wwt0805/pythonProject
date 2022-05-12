import warnings

warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV, cross_val_score, train_test_split
from sklearn.metrics import mean_squared_error
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor
from sklearn import linear_model

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义数据所在路径
TRAIN_PATH = "./data/train.csv"
TEST_PATH = "./data/test.csv"
SUBMIT_PATH = "./data/submit.csv"

# 利用pandas读入csv数据
train_data = pd.read_csv(TRAIN_PATH)
test_data = pd.read_csv(TEST_PATH)
submit_data = pd.read_csv(SUBMIT_PATH)

# 挑选离散变量（缺失值严重的出租方式、居住状态、装修情况三个字段不考虑）
class_feats = [f for f in train_data.columns if f not in ['ID', '出租方式', '居住状态', '装修情况', '房屋面积', '距离', 'Label']]
# print(class_feats)

# train_data = train_data.drop(train_data[train_data['房屋面积'] > 1100].index)
# train_data = train_data.drop(train_data[train_data['卧室数量'] > 10].index)

# 将地铁站点、地铁线路缺失值填充为0。
train_data['地铁站点'] = train_data['地铁站点'].fillna(0)
train_data['地铁线路'] = train_data['地铁线路'].fillna(0)
train_data['位置'] = train_data['位置'].fillna(0)
train_data['区'] = train_data['区'].fillna(0)
train_data['小区房屋出租数量'] = train_data['小区房屋出租数量'].fillna(0)
train_data['距离'] = train_data['距离'].fillna(0)

# train_data['位置'] = train_data['位置'].fillna(train_data["位置"].mean())
# train_data['区'] = train_data['区'].fillna(train_data["区"].mean())
# train_data['小区房屋出租数量'] = train_data['小区房屋出租数量'].fillna(train_data["小区房屋出租数量"].mean())
# train_data['距离'] = train_data['距离'].fillna(train_data["距离"].mean())

test_data['地铁站点'] = test_data['地铁站点'].fillna(0)
test_data['地铁线路'] = test_data['地铁线路'].fillna(0)
test_data['位置'] = test_data['位置'].fillna(0)
test_data['区'] = test_data['区'].fillna(0)
test_data['小区房屋出租数量'] = train_data['小区房屋出租数量'].fillna(0)
test_data['距离'] = test_data['距离'].fillna(0)
# test_data['位置'] = test_data['位置'].fillna(test_data["位置"].mean())
# test_data['区'] = test_data['区'].fillna(test_data["区"].mean())
# test_data['小区房屋出租数量'] = train_data['小区房屋出租数量'].fillna(test_data["小区房屋出租数量"].mean())
# test_data['距离'] = test_data['距离'].fillna(train_data["距离"].mean())
#
# train_data['地铁站点'] = train_data['地铁站点'].fillna(train_data['地铁站点'].mean())
# train_data['地铁线路'] = train_data['地铁线路'].fillna(train_data['地铁站点'].mean())
# test_data['地铁站点'] = test_data['地铁站点'].fillna(test_data['地铁站点'].mean())
# test_data['地铁线路'] = test_data['地铁线路'].fillna(test_data['地铁站点'].mean())

# 我们先将train和test拼起来一起处理
data = pd.concat([train_data, test_data], axis=0, ignore_index=True)


# 通过对上面统计房屋朝向元素的数量的观察，我们发现房屋朝向类别太多，需要整理归类，并进行编码
def classified_direction(text, direction):
    x = text.split(" ")
    return 1 if direction in x else 0


def get_feat1(df):
    direction_list = ['东', '南', '西', '北', '东南', '西南', '西北', '东北']
    for i in direction_list:
        df[i] = df['房屋朝向'].apply(lambda x: classified_direction(x, i))
    return df


data = get_feat1(data)


# 再构造一些新的特征
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
    # 卫卧比
    df["卫卧比"] = df["卫的数量"] / df["卧室数量"]
    # 卫厅比
    df["卫厅比"] = df["卫的数量"] / df["厅的数量"]
    # # 每个小区附近的地铁站点数
    df_temp = df.groupby('小区名')['地铁站点'].count().reset_index()
    df_temp.columns = ['小区名', '地铁站点数量']
    df = df.merge(df_temp, how='left', on='小区名')
    # 每个小区楼房的平均楼层高度
    floor_hmean = df.groupby('小区名')['总楼层'].mean().reset_index()
    floor_hmean.columns = ['小区名', '小区楼房平均高度']
    df = df.merge(floor_hmean, how='left', on='小区名')

    area_hmean = df.groupby('小区名')['房屋面积'].mean().reset_index()
    area_hmean.columns = ['小区名', '小区房屋平均面积']
    df = df.merge(area_hmean, how='left', on='小区名')

    rest_hmean = df.groupby('小区名')['卫的数量'].mean().reset_index()
    rest_hmean.columns = ['小区名', '小区卫生间平均数量']
    df = df.merge(rest_hmean, how='left', on='小区名')

    bed_hmean = df.groupby('小区名')['卧室数量'].mean().reset_index()
    bed_hmean.columns = ['小区名', '小区卧室平均数量']
    df = df.merge(bed_hmean, how='left', on='小区名')

    dinner_hmean = df.groupby('小区名')['厅的数量'].mean().reset_index()
    dinner_hmean.columns = ['小区名', '小区客厅平均数量']
    df = df.merge(dinner_hmean, how='left', on='小区名')  # 6.50297

    rest_sum = df.groupby('小区名')['卫的数量'].sum().reset_index()
    rest_sum.columns = ['小区名', '小区卫生间总数量']
    df = df.merge(rest_sum, how='left', on='小区名')

    rest_sum = df.groupby('小区名')['卧室数量'].sum().reset_index()
    rest_sum.columns = ['小区名', '小区卫生间总数量']
    df = df.merge(rest_sum, how='left', on='小区名')

    dinner_sum = df.groupby('小区名')['厅的数量'].mean().reset_index()
    dinner_sum.columns = ['小区名', '小区厅的总数量']
    df = df.merge(dinner_sum, how='left', on='小区名')  # 6.4287

    return df


data = get_feat2(data)
data = data.replace([np.inf, -np.inf], np.nan)

# 手动删除特征,删除样本ID、缺失严重的特征都进行删除。
feats = [f for f in data.columns if f not in ['ID', '出租方式', '居住状态', '房屋朝向', '装修情况', 'Label']]
# print(feats)

df_train = data[data['Label'].notna()].copy()
df_test = data[data['Label'].isna()].copy()

X_data = df_train[feats]
Y_data = df_train['Label']

x_train, x_val, y_train, y_val = train_test_split(X_data, Y_data, test_size=0.1, random_state=0)
X_test = df_test[feats]


# 参数可以手动去调整，也可以用GridSearchCV暴力调参。
def get_xgb_model(x_train, y_train):
    estimator = XGBRegressor(
        max_depth=8,  # 构建树的深度，越大越容易过拟合
        n_estimators=150,  # 3.22879
        n_jobs=-1,  # 启动cpu所有核
        objective='reg:squarederror',
        random_state=0)
    param_grid = {
        'learning_rate': [0.2],
        # 'learning_rate': [0.01, 0.05, 0.1, 0.2],
        # "max_depth": [8],
        # "n_estimators": [1000, 1500, 2000]
    }
    xgb_model = GridSearchCV(estimator, param_grid)
    xgb_model.fit(x_train, y_train)
    return xgb_model


def get_lgb_model(x_train, y_train):
    estimator = LGBMRegressor(
        num_leaves=800,
        n_estimators=150,  # 2.3839
        n_jobs=-1,
        objective='regression',
        random_state=0)
    param_grid = {
        # 'learning_rate': [0.01, 0.05, 0.1, 0.2],
        'learning_rate': [0.2],
        # "num_leaves": [31, 800],
        # "n_estimators": [2000, 3000, 4000]  # 20000 1.8434
    }
    lgb_model = GridSearchCV(estimator, param_grid)
    lgb_model.fit(x_train, y_train)
    return lgb_model


# print(cross_val_score(LGBMRegressor(n_estimators=100, random_state=0), X_data, Y_data, cv=5,
#                       scoring="neg_mean_squared_error").mean())


# 训练模型，并预测结果，写出结果。
print('Train lgb...')
model_lgb = get_lgb_model(x_train, y_train)
val_lgb = model_lgb.predict(x_val)
mse_lgb = mean_squared_error(y_val, val_lgb)
print('MSE of val with lgb:', mse_lgb)
print("Best estimator is:", model_lgb.best_estimator_)

print('Predict lgb...')
pre_lgb = get_lgb_model(X_data, Y_data)
sub_lgb = pre_lgb.predict(X_test)
print('lgb模型运行完成！')

# 训练xgb模型，这个模型比lgb模型更耗时
print('Train xgb...')
model_xgb = get_xgb_model(x_train, y_train)
val_xgb = model_xgb.predict(x_val)
mse_xgb = mean_squared_error(y_val, val_xgb)
print('MSE of val with xgb:', mse_xgb)
print("Best estimator is:", model_xgb.best_estimator_)

# print('Predict xgb...')
# pre_xgb = get_xgb_model(X_data, Y_data)
# sub_xgb = pre_xgb.predict(X_test)
print('xgb模型运行完成！')


#
#
def get_submit(submit_data, result, save_path):
    submit = pd.DataFrame()
    submit['ID'] = submit_data.ID
    submit['Label'] = result
    submit.to_csv(save_path, index=None)
    print('结果已写出！')


get_submit(submit_data, sub_lgb, 'sub_lgb.csv')
# get_submit(submit_data, sub_xgb, 'sub_xgb.csv')
#
# # 第一层
# train_lgb_pred = model_lgb.predict(x_train)
# train_xgb_pred = model_xgb.predict(x_train)
#
# Stack_X_train = pd.DataFrame()
# Stack_X_train['Method_1'] = train_lgb_pred
# Stack_X_train['Method_2'] = train_xgb_pred
#
# Stack_X_val = pd.DataFrame()
# Stack_X_val['Method_1'] = val_lgb
# Stack_X_val['Method_2'] = val_xgb
#
# Stack_X_test = pd.DataFrame()
# Stack_X_test['Method_1'] = sub_lgb
# Stack_X_test['Method_2'] = sub_xgb
#
#
# # 第二层
# def build_model_lr(x_train, y_train):
#     reg_model = linear_model.LinearRegression()
#     reg_model.fit(x_train, y_train)
#     return reg_model
#
#
# model_lr_Stacking = build_model_lr(Stack_X_train, y_train)
# # 训练集
# train_pre_Stacking = model_lr_Stacking.predict(Stack_X_train)
# print('MSE of Stacking-LR:', mean_squared_error(y_train, train_pre_Stacking))
#
# # 验证集
# val_pre_Stacking = model_lr_Stacking.predict(Stack_X_val)
# print('MSE of Stacking-LR:', mean_squared_error(y_val, val_pre_Stacking))
#
# # 预测集
# print('Predict Stacking-LR...')
# sub_Stacking = model_lr_Stacking.predict(Stack_X_test)
#
# get_submit(test_data, sub_Stacking, 'sub_stacking.csv')
