import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing

df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')


#print(df.info())
X_num = df.select_dtypes(include=['int64','float64']).columns.tolist() # SeniorCitizen, tenure, MonthlyCharges

X_cat = df.select_dtypes(include=['object']).columns.tolist()

scaler = preprocessing.StandardScaler().fit(df[X_num])
X_num_scaled = scaler.transform(df[X_num])
print(f"mean: {X_num_scaled.mean(axis=0)} std: {X_num_scaled.std(axis=0)}\n")

min_max_scaler = preprocessing.MinMaxScaler()
X_num_scaled = min_max_scaler.fit_transform(df[X_num])
print(f"MinMaxScaler: {X_num_scaled}\n")

max_abs_scaler = preprocessing.MaxAbsScaler()
X_num_scaled = max_abs_scaler.fit_transform(df[X_num])
print(f"MaxAbsScaler: {X_num_scaled}\n")

X_num_normalized = preprocessing.normalize(df[X_num], norm='l2')
print(f"Norm: {X_num_normalized}\n")

encoder = preprocessing.OrdinalEncoder(encoded_missing_value=-1)
X_cat_encoded = encoder.fit_transform(df[X_cat])
print(f"Encoded: {X_cat_encoded}")
