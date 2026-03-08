import pandas as pd
import numpy as np 
from sklearn.impute import KNNImputer 
import re

kn = KNNImputer(n_neighbors=3)
num_words = {
"one":1,
"two":2,
"three":3,
"four":4,
"five":5,
"six":6,
"seven":7,
"eight":8,
"nine":9,
"ten":10,
"eleven":11,
"twelve":12,
"thirteen":13,
"fourteen":14,
"fifteen":15,
"sixteen":16,
"seventeen":17,
"eighteen":18,
"nineteen":19,
"twenty":20,
"twenty one":21,
"twenty two":22,
"twenty three":23,
"twenty four":24,
"twenty five":25,
"twenty six":26,
"twenty seven":27,
"twenty eight":28,
"twenty nine":29,
"thirty":30,
"thirty one":31,
"thirty two":32,
"thirty three":33,
"thirty four":34,
"thirty five":35,
"thirty six":36,
"thirty seven":37,
"thirty eight":38,
"thirty nine":39,
"forty":40,
"forty one":41,
"forty two":42,
"forty three":43,
"forty four":44,
"forty five":45,
"forty six":46,
"forty seven":47,
"forty eight":48,
"forty nine":49,
"fifty":50,
"fifty one":51,
"fifty two":52,
"fifty three":53,
"fifty four":54,
"fifty five":55,
"fifty six":56,
"fifty seven":57,
"fifty eight":58,
"fifty nine":59,
"sixty":60,
"sixty one":61,
"sixty two":62,
"sixty three":63,
"sixty four":64,
"sixty five":65,
"sixty six":66,
"sixty seven":67,
"sixty eight":68,
"sixty nine":69,
"seventy":70,
"seventy one":71,
"seventy two":72,
"seventy three":73,
"seventy four":74,
"seventy five":75,
"seventy six":76,
"seventy seven":77,
"seventy eight":78,
"seventy nine":79,
"eighty":80,
"eighty one":81,
"eighty two":82,
"eighty three":83,
"eighty four":84,
"eighty five":85,
"eighty six":86,
"eighty seven":87,
"eighty eight":88,
"eighty nine":89,
"ninety":90,
"ninety one":91,
"ninety two":92,
"ninety three":93,
"ninety four":94,
"ninety five":95,
"ninety six":96,
"ninety seven":97,
"ninety eight":98,
"ninety nine":99,
"one hundred":100
}

dt = pd.read_csv(r"C:\DataAnalyst\PythonBasicToAdvance\dataCleaning.csv")

# Age
dt['Age'] = dt["Age"].replace(num_words)
dt['Age'] = pd.to_numeric(dt["Age"],errors='coerce')
dt.loc[dt["Age"] < 0 ,'Age'] = None
dt["Age"] = kn.fit_transform(dt[['Age']])
dt["Age"] = dt["Age"].astype(int)

# Gender
dt['Gender'] = dt["Gender"].replace({"M":"Male","F":"Female"})
dt["Gender"] = dt["Gender"].fillna(dt["Gender"].mode()[0])


# City
dt["City"] = dt["City"].fillna(dt["City"].mode()[0])
dt["City"] = dt["City"].str.capitalize()

# Purchase_Amount
dt["Purchase_Amount"] = dt["Purchase_Amount"].abs()
dt["Purchase_Amount"] = dt["Purchase_Amount"].fillna(dt["Purchase_Amount"].mean())
dt["Purchase_Amount"] = dt["Purchase_Amount"].astype(int)

# Join_Date
dt["Join_Date"] = pd.to_datetime(dt["Join_Date"],errors='coerce' ,format='mixed')
dt.loc[dt["Join_Date"] > pd.Timestamp.today(),'Join_Date'] = np.nan
dt["Join_Date"] = dt["Join_Date"].fillna(dt["Join_Date"].median())
dt["Join_Date"] = dt["Join_Date"].dt.date

# Membership
dt["Membership"] = dt["Membership"].fillna(dt["Membership"].mode()[0])
dt["Membership"] = dt["Membership"].str.capitalize()

# Email
def EmailFix(email):
    email = str(email).strip().lower()
    pattern = r'.+@.+\.[a-zA-Z]{2,}'
    if '@' not in email:
        match = re.search(r'(gmail|yahoo|hotmail|outlook|live)', email)
        if match:
            domain = match.group(0)
            username = email[:match.start()]
            email = username + '@' + domain
    if re.match(pattern,email):
        return email
    elif '@' in email and '.' not in email.split('@')[1]:
        email = email + '.com'
    return email

dt["Email"] = dt["Email"].fillna("unknown@gmail.com")
dt["Email"] = dt["Email"].apply(EmailFix)

# Phone 
def clean_mobile(x):
    try:
        return str(int(x))
    except:
        return str(x)

dt["Phone"] = pd.to_numeric(dt["Phone"],errors='coerce')
mobile_prefix = dt["Phone"].dropna().astype(str).str[:2].mode()[0]
dt['Phone'] = dt["Phone"].fillna(mobile_prefix + "XXXXXXXX")
dt["Phone"] = dt["Phone"].apply(clean_mobile)

# Salary
dt["Salary"] = dt["Salary"].abs()
dt["Salary"] = dt["Salary"].fillna(dt["Salary"].mean())
dt["Salary"] = dt["Salary"].round()

# Last_Login
dt["Last_Login"] = pd.to_datetime(dt["Last_Login"],errors='coerce',format='mixed')
dt.loc[dt["Last_Login"] > pd.Timestamp.today(),'Last_Login'] = np.nan
dt["Last_Login"] = dt["Last_Login"].fillna(dt["Last_Login"].mode()[0])
# dt = dt.drop(columns=['Unnamed: 0'])

dt.to_csv(r"C:\DataAnalyst\PythonBasicToAdvance\dataCleaning.csv",index=False)
print(dt.info())