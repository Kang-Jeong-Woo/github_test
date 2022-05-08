import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DataUrl='https://www.kaggle.com/datasets/ahmedelnaggar/fifa-worldcup-2018-dataset?select=World+Cup+2018+Dataset.csv'
df=pd.read_csv(DataUrl)
print(df.head())