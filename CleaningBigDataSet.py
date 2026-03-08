import pandas as pd 
import numpy as np
import re
from sklearn.impute import KNNImputer 


kn = KNNImputer(n_neighbors=3)
dt = pd.read_csv(r"C:\DataAnalyst\PythonBasicToAdvance\messy_people_data_10k.csv")

# ID 
def Indexing(data,expected = (1,10000)):
    df = data.copy()
    df['id'] = pd.to_numeric(df['id'])
    df.loc[dt['id'].duplicated(keep='first'),'id'] = np.nan
    out_of_range = (dt['id'] < expected[0]) | (dt['id'] > expected[1])
    dt.loc[out_of_range, 'id'] = np.nan
    valid_ids = set(df['id'].dropna().astype(int))
    all_ids = set(range(expected[0],expected[1]+1))
    missing_ids = sorted(list(all_ids - valid_ids))
    needed_ids = dt[dt['id'].isna()].index.tolist()
    for i,row_index in enumerate(needed_ids):
        if i < len(missing_ids):
            dt.loc[row_index,'id'] = missing_ids[i]
        else:
            dt.loc[row_index, 'id'] = expected[1] + 1 + (i - len(missing_ids))
    return dt

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

def Age_(dt):
    dt['age'] = dt["age"].replace(num_words)
    dt["age"] = pd.to_numeric(dt["age"],errors='coerce')
    dt["age"] = dt["age"].abs()
    dt.loc[dt["age"] > 100,'age'] = np.nan 
    dt["age"] = kn.fit_transform(dt[['age']])
    dt["age"] = dt["age"].astype(int)
    return dt


gender_map = {
    'Prefer not to say': np.nan,
    'Other': np.nan,
    'Non-binary': np.nan
}

def Gender__(dt):
    dt["gender"] = dt['gender'].replace(gender_map)
    dt["gender"] = dt['gender'].replace({'M':'Male','F':'Female','FEMALE':'Female'})
    dt["gender"] = dt["gender"].fillna(dt["gender"].mode()[0])
    return dt

def Email__(email):
    email = str(email).strip().lower()
    pattern = r'.+@.+\.[a-zA-Z]{2,}'
    if "@" not in email :
        match = re.search(r'(gmail|yahoo|hotmail|outlook|live|example)', email)
        if match:
            domain = match.group(0)
            username = email[:match.start()]
            return username + '@' + domain
        if re.match(pattern,email):
            return email
        elif '@' in email and '.' not in email.split('@')[1]:
            email = email + '.com'
    return email

# ID 
dt = Indexing(dt)
dt['id'] = sorted(dt['id'])
dt['id'] = dt['id'].astype(int)

# Age
dt = Age_(dt)

# Gender
dt = Gender__(dt)

# Email
dt['email'] = dt['email'].apply(Email__)
dt['email'] = dt['email'].fillna("unknown@example.com")
dt['email'] = dt['email'].replace('nan', 'missing@example.com')

# Phone
def string__(dt):
    dt = str(dt)
    if len(dt) == 10:
        return dt
    else: 
        return np.nan
    
dt['phone'] = dt['phone'].str.replace(r"\D","",regex=True)
dt['phone'] = dt['phone'].apply(string__)
dt['phone'] = dt['phone'].fillna("98XXXXXXXX")

# Address
dt['address'] = dt['address'].fillna(dt['address'].mode()[0])

# join_date
dt['join_date'] = pd.to_datetime(dt['join_date'],errors='coerce',format='mixed')
dt.loc[dt['join_date'] >= pd.Timestamp.today(),'join_date'] = np.nan
dt['join_date'] = dt['join_date'].fillna(dt['join_date'].mode()[0])

# Salary
dt['salary'] = pd.to_numeric(dt['salary'],errors='coerce')
dt['salary'] = dt['salary'].fillna(dt['salary'].mean())
dt['salary'] = dt['salary'].astype(int)

mapping1 = {
        'hr': 'HR',
        'h r': 'HR',                
        'human resources': 'HR',
        'sales': 'Sales',
        'sale': 'Sales',
        'sells': 'Sales',
        'operations': 'Operations',
        'markting': 'Marketing',
        'marketing': 'Marketing',
        'market': 'Marketing',
        'mktg': 'Marketing',
        'engineering': 'Engineering',
        'eng': 'Engineering',
        'enginnering': 'Engineering',
        'engg': 'Engineering',
        'engineeringg': 'Engineering',
        'legal': 'Legal',
        'it': 'IT',
        'finance': 'Finance'
        }

# Department
dt['department'] = dt['department'].str.strip().str.lower()
dt["department"] = dt['department'].replace(mapping1)
dt['department'] = dt['department'].fillna(dt['department'].mode()[0])

# Rating
dt["rating"] = pd.to_numeric(dt['rating'],errors='coerce')
dt.loc[dt['rating'] > 5,'rating'] = np.nan
dt['rating'] = dt['rating'].fillna(dt['rating'].mean().round(2))

# Comments
dt['comments'] = dt['comments'].fillna(dt['comments'].mode()[0])

dt.to_csv(r"C:\DataAnalyst\PythonBasicToAdvance\CleanedMessyPeople.csv",index = False)