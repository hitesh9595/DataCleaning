import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer as kn

a = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
# when we want to index to our dataframe we use index keyword with dataframe 
# print(a)

b = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
# In series also we use indexing and naming to the column name keyword we use for assign the column name 
# print(b)

im = kn(n_neighbors=3)
df = pd.read_csv(r"C:\DataAnalyst\PythonBasicToAdvance\smallDataSet.csv")
# print(df.head())

# print(df["Gender"].isnull().sum())

# Gender 
df['Gender'] = df['Gender'].fillna(df["Gender"].mode()[0])
df["Gender"] = df["Gender"].replace({"M": "Male", "F": "Female"})

# Customer ID
df = df.reset_index()
 
# Age
df["Age"] = pd.to_numeric(df['Age'],errors="coerce")
df.loc[df['Age'] < 0 | (df['Age'] > 100),"Age"] = None
df['Age'] = im.fit_transform(df[['Age']])
df['Age'] = df['Age'].astype(int)

# City
df['City'] = df['City'].fillna(df['City'].mode()[0])

# Purchase 
df['Purchase_Amount'] = pd.to_numeric(df['Purchase_Amount'],errors='coerce')
df.loc[df['Purchase_Amount']< 0,'Purchase_Amount'] = None
df['Purchase_Amount'] = im.fit_transform(df[['Purchase_Amount']])  

# Joining Dates
df["Join_Date"] = pd.to_datetime(df["Join_Date"], errors="coerce", format="mixed")
df.loc[df['Join_Date'] > pd.Timestamp.today(),'Join_Date'] = np.nan
df['Join_Date'] = df['Join_Date'].fillna(df['Join_Date'].median())

# MemberShip Column
df['Membership'] = df['Membership'].str.capitalize()
df['Membership'] = df['Membership'].fillna(df['Membership'].mode()[0])

print(df.info())

df.to_csv(r"C:\DataAnalyst\PythonBasicToAdvance\new.csv",index=False)


print(df.read_csv(r"C:\DataAnalyst\PythonBasicToAdvance\SmallDataSet.csv"))
