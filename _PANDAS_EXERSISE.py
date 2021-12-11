import numpy as np
import pandas as pd

pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)

df = pd.read_csv('01-Pandas-Crash-Course/african_econ_crises.csv')
df['country'].nunique()
df['country'].unique()
print(df[(df['country']=='Kenya') & (df['systemic_crisis']==1)].sort_values('year').head(1))
# df = df.groupby('country').sum().sort_values('systemic_crisis',ascending=False)



