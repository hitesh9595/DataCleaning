import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import re
from sklearn.impute import KNNImputer as knn
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

la = LabelEncoder()

Item_Encoders = LabelEncoder()
Payment_Encoders = LabelEncoder()
Location_Encoders = LabelEncoder()


kn = knn(n_neighbors=5)

df = pd.read_csv(r"C:\DataAnalyst\data\dirty_cafe_sales.csv")


# Item
df.loc[df["Item"].str.contains("UNKNOWN",na = False), "Item"] = np.nan
df.loc[df["Item"].str.contains("ERROR", na = False), "Item"] = np.nan
df.loc[df["Item"].notnull(), "Item"] = la.fit_transform(df.loc[df["Item"].notnull(), "Item"])
df["Item"] = pd.to_numeric(df["Item"], errors='coerce')
df["Item"] = kn.fit_transform(df[["Item"]])
df["Item"] = df["Item"].round().astype(int)
df["Item"] = la.inverse_transform(df["Item"])

# Quantity
df["Quantity"] = pd.to_numeric(df["Quantity"], errors='coerce')
df["Quantity"] = kn.fit_transform(df[["Quantity"]])
df["Quantity"] = df["Quantity"].round().astype(int)

# Price Per Unit
df["Price Per Unit"] = pd.to_numeric(df["Price Per Unit"], errors='coerce')
df["Price Per Unit"] = kn.fit_transform(df[["Price Per Unit"]])

# Total Spent
df["Total Spent"] = pd.to_numeric(df["Total Spent"], errors='coerce')
df["Total Spent"] = kn.fit_transform(df[["Total Spent"]])

# Payment Method
df.loc[df["Payment Method"].str.contains("UNKNOWN",na = False), "Payment Method"] = np.nan
df.loc[df["Payment Method"].str.contains("ERROR", na = False), "Payment Method"] = np.nan
df["Payment Method"] = df["Payment Method"].fillna(df["Payment Method"].mode()[0])

# Location

df.loc[df["Location"].str.contains("UNKNOWN", na=False), "Location"] = np.nan
df.loc[df["Location"].str.contains("ERROR", na=False), "Location"] = np.nan

train_df = df[df["Location"].notnull()].copy()
test_df = df[df["Location"].isnull()].copy()

train_df["Item"] = Item_Encoders.fit_transform(train_df["Item"])
train_df["Payment Method"] = Payment_Encoders.fit_transform(train_df["Payment Method"])
train_df["Location"] = Location_Encoders.fit_transform(train_df["Location"])  

test_df["Item"] = Item_Encoders.transform(test_df["Item"])
test_df["Payment Method"] = Payment_Encoders.transform(test_df["Payment Method"])

train_df["Transaction Date"] = pd.to_datetime(train_df["Transaction Date"],errors='coerce')
test_df["Transaction Date"] = pd.to_datetime(test_df["Transaction Date"],errors='coerce')

for data in [train_df, test_df]:

    data["Year"] = data["Transaction Date"].dt.year
    data["Month"] = data["Transaction Date"].dt.month
    data["Day"] = data["Transaction Date"].dt.day

drop_col = ["Transaction Date","Transaction ID"]
train_df.drop(columns=drop_col,axis=1,inplace=True)
test_df.drop(columns=drop_col,axis=1,inplace=True)

x_train = train_df.drop(["Location"],axis=1)
y_train = train_df["Location"]
x_test = test_df.drop(["Location"],axis=1)

Model = RandomForestClassifier(n_estimators=100, random_state=42)

Model.fit(x_train, y_train)
predicted_Location = Model.predict(x_test)

predicted_Location = Location_Encoders.inverse_transform(predicted_Location)

df.loc[df["Location"].isnull(),"Location"] = predicted_Location

# Transaction Date
df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], errors='coerce')
df.loc[df["Transaction Date"].isnull(), "Transaction Date"] = df["Transaction Date"].mode()[0]

df.to_csv(r"C:\DataAnalyst\data\cleaned_cafe_sales.csv", index=False)