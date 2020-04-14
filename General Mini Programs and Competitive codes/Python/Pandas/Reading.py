import pandas as pd
df=pd.read_csv(r"C:\Users\Zano\Downloads\P2-Demographic-Data.csv")
print(df.shape)
print(df[['Country Code','Internet users']])
print(df['Internet users'].max())