import pandas as pd
import numpy as np

#-- PANDAS SERIES --#

list = [10,20,30,40]
labels = ['a' , 'b' , 'c' , 'd']
dictionary = {'a':10 , 'b':20 , 'c':30 , 'd':40}
np_array = np.array([10,20,30,40])

# print(pd.Series(list,labels))

#%%

population = pd.Series([200,125,56,0],['CHINA' , 'INDIA' , 'AMERICA' , 'BURMUDA_TRIANGLE'])
population2 = pd.Series([2000,1250,56,0],['CHINA' , 'INDIA' , 'USA' , 'BURMUDA_TRIANGLE'])

print(population)
print(population2)

# print(population+population2)

#-- PANDAS DATAFRAME--#
#%%

labels2 = ['a' , 'b' , 'c' , 'd']
colums_name = ['feat_1','feat_2','feat_3','feat_4']
data = np.arange(1,17).reshape(4,4)

# colomn access
df = pd.DataFrame(data,labels2,colums_name)
print(df)
# df['feat_1']
df['new'] = df['feat_1']/2
print(df)
df = df.drop('feat_1',axis=1)
print(df)
# print(df)

#%%
# row access
row = df.loc[['a' , 'c']]
print(row)
row = df.iloc[:2]
print(row)
ext = df.drop('a')
print(ext)
# print(ext)
# multiple columns

mul_col = df.loc[['a' , 'b'] , ['feat_4' , 'feat_2']]
print(mul_col)
