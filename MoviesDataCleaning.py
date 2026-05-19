import pandas as pd 
import data 


df = pd.read_csv(r"C:\DataAnalyst\data\movies.csv")

# Year
df["YEAR1"] = df["YEAR"]
df["YEAR1"] = df["YEAR1"].str.replace(r'\([IVXLCDM]+\)','',regex=True).str.strip()
df["YEAR1"] = df["YEAR1"].str.extract(r'(\d{4})').astype(float)
df["YEAR1"] = pd.to_numeric(df["YEAR1"])
df["Content"] = "Movie"
df.loc[df["YEAR"].str.contains("TV Movie",na = False), "Content"] = "TV Movie"
df.loc[df["YEAR"].str.contains("Movie",na = False), "Content"] = "Movie"
df.loc[df["YEAR"].str.contains("Series",na = False), "Content"] = "Series"
df.loc[df["YEAR"].str.contains("TV Special",na = False), "Content"] = "TV Special"
df.loc[df["YEAR"].str.contains("Video",na = False), "Content"] = "Video"
df.loc[df["YEAR"].str.contains("Video Game",na = False), "Content"] = "Video Game"
df["YEAR"] = df["YEAR1"]
df["YEAR"] = df["YEAR"].fillna(df["YEAR"].median())


#GENRE
df['GENRE'] = df['GENRE'].str.strip().str.replace('\n','', regex=False).str.replace(r'\s+',' ', regex=True)
df["GENRE"] = df["GENRE"].fillna("Unknown")
df["GENRE"] = df["GENRE"].replace(data.genre_to_single)

# RATING
df["RATING"] = df["RATING"].fillna(df["RATING"].median())
df["RATING"] = df["RATING"].round(1)

#VOTES
df["VOTES"] = df["VOTES"].str.replace(',','').astype(float)
df["VOTES"] = df["VOTES"].fillna(df["VOTES"].median())  

# Runtime
df["RunTime"] = df["RunTime"].fillna(df["RunTime"].mean())

# Gross
df.drop(["Gross","YEAR1"],axis=1,inplace=True)

try: 
    df.to_csv(r"C:\DataAnalyst\data\movies.csv", index=False)
except Exception as e:
    print("File not Found:", e)