import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DataUrl='https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv'
df=pd.read_csv(DataUrl,sep='\t')
print(df.head())

#이것은 수류탄이여!!
