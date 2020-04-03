# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 10:13:30 2020

@author: 20605019
"""

import pandas as pd

df = pd.read_csv('PS_20174392719_1491204439457_log.csv')

# 불필요한 Feature 삭제
df = df.drop(['nameOrig', 'nameDest', 'isFlaggedFraud'], axis = 1)  # 송금자, 수신자, 20만이상부정거래

# 데이터 줄이기 (부정거래:모두, 정상거래:부정거래수*150%)
df_fraud = df[df['isFraud'] == 1]

df_nofraud = df[df['isFraud'] == 0]
df_nofraud = df_nofraud.head(12000)

df = pd.concat([df_fraud, df_nofraud], axis = 0)
df.index = range(len(df))


# 카테고리 인코딩(one-hot-encoding)
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

df['type'] = df['type'].astype('category')

type_encode = LabelEncoder()
df['type'] = type_encode.fit_transform(df.type)

type_one_hot = OneHotEncoder()
type_one_hot_encode = type_one_hot.fit_transform(df.type.values.reshape(-1,1)).toarray()
ohe_variable = pd.DataFrame(type_one_hot_encode,
columns = ["type_"+str(int(i)) for i in range(type_one_hot_encode.shape[1])])
df2 = pd.concat([df, ohe_variable], axis=1)


# 데이터 준비하기
features = df.drop('isFraud', axis = 1).values
target = df['isFraud'].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
features, target, test_size = 0.3, random_state = 42, stratify = target)


# 학습하기
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# 예측하기
y_pred = knn.predict(X_test)
pred = pd.DataFrame(dict(target=y_test, pred=y_pred))

knn.score(X_test, y_test)


# ----------------------------------------------------------------------------
import numpy as np
import pandas as pd
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.model_selection import validation_curve


digits = load_digits()
X, y = digits.data, digits.target

param_range = np.logspace(-6, -1, 10)

train_scores, test_scores = \
    validation_curve(SVC(), X, y,
                     param_name="gamma", param_range=param_range,
                     cv=8, scoring="accuracy", n_jobs=1)

train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)

df = pd.DataFrame({'train': train_scores_mean, 'test': test_scores_mean})
df.plot()



