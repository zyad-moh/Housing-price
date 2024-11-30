import numpy as np 
import pandas as pd
df3=pd.read_csv("housing_prices.csv")
df1=pd.read_csv("housing_prices.csv")
df1=df1[df1["price"]< 1000000]
print(df1)