import pandas as pd
import numpy as np

dict = {"A":[1,2,3,7,5,9],
        "B":[0,4,9,3,np.nan,50],
        "C":[1,0,np.nan,3,np.nan,5]}
df = pd.DataFrame(dict)
print(df)
#%%
# print(df.dropna(axis=0,thresh=2))     #drop nan values , threshold can be set
# print(df.fillna(value=df['B'].mean()))        #fill nan vlue with given value
df['B'] = df['B'].fillna(value=df["B"].mean())
# df.fillna(df.mean())      # fill dataframe with mean of column
# print(df)

#%%

# GROUP BY IMP METHOD IN WHICH GROUP BY CATOGACAL DATA AND THEN APPLY FUNCTION AND THEN AGGRIGATE USING AGG.
labels = ['M1' , 'M2' , 'M3' , 'M4']
data_f = pd.DataFrame({"A" : ['M1','M2','M1','M1'],
                       "B" : ['MC','LM','OB','BC'],
                       "C" : [0,1,2,6],
                       "D" : [0,1,2,8]})
print(data_f)
print(data_f['A'].unique())
data_f['A'].unique() #list of unique catagory
data_f['A'].nunique()   #len of unique cat list
data_f["A"].value_counts()  #return cunts of unique value in coloumn

# create coloumn
#%%

def first_leter(string):
    return string[0]

data_f['new'] = data_f['B'].apply(first_leter)
my_map = {"M" : "melon" , "L" : "lemmon" , "O" : "orange"  , "B" : "bannana"}
data_f['new'] = data_f['new'].map(my_map)
# print(data_f)

# getting index of max value in coloumn
data_f['C'].idxmax()

# getting index of min value in coloumn
data_f['C'].idxmin()

#getting coloumns
# print(data_f.columns)

#changing colomn names
# data_f.columns = ["NEW1","NEW2","NEW3","NEW4","NEW5"] # EFFECTS ARE PERMANENT

#SORTING VALUE BASED ON  SPECIFIC
data_f.sort_values("new",ascending=True)

# JOIN TWO DATA FRAMES
pd.concat([df,data_f],axis=1) # shoud be axix = 1
