import pandas as pd

df = pd.read_csv("./Data/EnrolmentsByProvider/table-1-(2014-15).csv", skiprows=14)

print(df.head())
print(df.info())
print(df.describe())