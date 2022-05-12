import warnings
import time

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

train_data = train_data.drop(train_data[train_data['房屋面积'] > 1300].index)
# train_data = train_data.drop(train_data[train_data['房屋面积'] > 1100].index)
# train_data = train_data.drop(train_data[train_data['卧室数量'] > 10].index)


# 将地铁站点、地铁线路缺失值填充为0。
train_data['地铁站点'] = train_data['地铁站点'].fillna(0)
train_data['地铁线路'] = train_data['地铁线路'].fillna(0)
# train_data['地铁站点'] = train_data['地铁站点'].fillna(train_data['地铁站点'].mean())
# train_data['地铁线路'] = train_data['地铁线路'].fillna(train_data['地铁站点'].mean())
# train_data['位置'] = train_data['位置'].fillna(train_data["位置"].mean())
# train_data['区'] = train_data['区'].fillna(train_data["区"].mean())
# train_data['小区房屋出租数量'] = train_data['小区房屋出租数量'].fillna(train_data["小区房屋出租数量"].mean())
# train_data['距离'] = train_data['距离'].fillna(train_data["距离"].mean())
# train_data['位置'] = train_data['位置'].fillna(0)
# train_data['区'] = train_data['区'].fillna(0)
# train_data['小区房屋出租数量'] = train_data['小区房屋出租数量'].fillna(0)
# train_data['距离'] = train_data['距离'].fillna(0)

test_data['地铁站点'] = test_data['地铁站点'].fillna(0)
test_data['地铁线路'] = test_data['地铁线路'].fillna(0)
# test_data['地铁站点'] = test_data['地铁站点'].fillna(test_data['地铁站点'].mean())
# test_data['地铁线路'] = test_data['地铁线路'].fillna(test_data['地铁站点'].mean())
# test_data['位置'] = test_data['位置'].fillna(test_data["位置"].mean())
# test_data['区'] = test_data['区'].fillna(test_data["区"].mean())
# test_data['小区房屋出租数量'] = train_data['小区房屋出租数量'].fillna(test_data["小区房屋出租数量"].mean())
# test_data['距离'] = test_data['距离'].fillna(train_data["距离"].mean())
# test_data['位置'] = test_data['位置'].fillna(0)
# test_data['区'] = test_data['区'].fillna(0)
# test_data['小区房屋出租数量'] = train_data['小区房屋出租数量'].fillna(0)
# test_data['距离'] = test_data['距离'].fillna(0)

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
    # 每个小区附近的地铁站点数
    df_temp = df.groupby('小区名')['地铁站点'].count().reset_index()
    df_temp.columns = ['小区名', '地铁站点数量']
    df = df.merge(df_temp, how='left', on='小区名')
    # 每个小区楼房的平均楼层高度
    floor_hmean = df.groupby('小区名')['总楼层'].mean().reset_index()
    floor_hmean.columns = ['小区名', '小区楼房平均高度']
    df = df.merge(floor_hmean, how='left', on='小区名')

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

x_train, x_val, y_train, y_val = train_test_split(X_data, Y_data, test_size=0.3, random_state=0)
X_test = df_test[feats]

# 10折交叉验证
regressor = LGBMRegressor(n_estimators=100, random_state=0)
print(cross_val_score(regressor, X_data, Y_data, cv=10, scoring="neg_mean_squared_error").mean())
