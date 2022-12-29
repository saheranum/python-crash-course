#!/usr/bin/env python
# coding: utf-8

# # Pandas Series

# In[1]:


import pandas as pd
PN = pd.Series([4, 7, -5, 3])    
print(PN)


# # pandas Series has two things in one object
# 1 Values
# 2 Index

# In[7]:


sales = pd.Series(['anum', 'aywsha', 'manahil', 'abeeha','doll'])

print(sales.values)
print(sales.index)
print(sales)


# In[8]:


sales = pd.Series([100, 200, 400, 700], index = ['Jan', 'Feb', 'Mar','Apr'])
print(sales)
print(sales.values)
print(sales.index)


# In[9]:


sales = pd.Series([100, 200, 400, 700], index = ['Jan', 'Feb', 'Mar','Apr'])

print(sales.values)
print(sales.index)
print(sales)


# # create a pandas series to store a canteen data to hold values of how many sandwitches are sold each days (one week

# In[11]:


schizophrenia = pd.Series(['psychotic disorder', 'schizophreniform disorder', 'schizoaffective disorder', 'catatonia disorder'], 
               index = ['1', '2', '3', '4'])
print(schizophrenia)


# In[21]:


print(schizophrenia[0])

print (schizophrenia["1"])


# # for providing multiple index for selecting element in an pd series, use array notation

# In[32]:



print("schizophreniform disorder")


# # taking input from numpy arrays and converting to Pandas Series

# In[33]:


import numpy as np

ar = np.array([3,2,4,5,6])   # creating array 
ind = np.array( ['a', 'b', 'c', 'd', 'e']) 

obj2 = pd.Series(ar, index = ind)    
print(obj2)


# # creating dictionary and then converting to pandas series

# In[41]:


data = {"psychotic disorder": 1, "schizophreniform disorder": 2, "schizoaffective disorder": 3, "catatonia disorder": 4} 
tax = pd.Series(data)  
print(tax)
print(tax.index)


# # if index more than values :

# In[47]:


data = {"psychotic disorder":1, "schizophreniform disorder":2, "schizoaffective disorder":3, "catatonia disorder":4} 
tax = pd.Series(data, index = ['psychotic disorder', 'schizophreniform disorder', 'schizoaffective disorder', 'catatonia disorder', 'schizophrenia'])
print(pd.isnull(tax))


# # DataFrame

# In[13]:


import pandas as pd
a = pd.Series(['a',2,'b',1])
b = pd.Series([3,4,7,8])
print(a, b)
  


# In[18]:


import pandas as pd

a = pd.Series([3,2,0,1])
b = pd.Series([3,4,7,8])
c= pd.Series(["rana", "saeed","gogran", "ali"])
data = {"class1": a, "class2": b, "names" : c}
fruits_df = pd.DataFrame(data)
print(fruits_df)


# # keep in mind, Indexes

# In[20]:


a= pd.Series([3,2,0,1], ["a", "b", "c", "d"] )
a


# In[21]:


b = pd.Series([3,2,0,1], index = ["mon", "tue", "wed", "thr"])
b


# In[22]:


import pandas as pd

a = pd.Series([3,2,0,1], ["a", "b", "c", "d"] )

b = pd.Series([3,2,0,1], index = ["mon", "tue", "wed", "thr"])

#print(apples, oranges)
data = {"apples": a, "oranges": b}
fruits = pd.DataFrame(data)
print(fruits)
# index not matched


# In[32]:


import pandas as pd

a = pd.Series([3,2,0,1] , index = ["mon", "tue", "wed", "thr"] )   # same index
b = pd.Series([3,2,0,1], index = ["mon", "tue", "wed", "thr"])

#print(apples,"\n", oranges)

data = {"apples": a, "oranges": b}
fruits_df = pd.DataFrame(data)
print(fruits_df)


# In[35]:


state = ['a', 'b', 'c', 'd', 'e', 'f']

data = {'city': state ,
        'year' : [2000, 2001, 2002, 2001, 2002, 2003],
        'ratio'  : [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

rows_index = pd.DataFrame(data, index = ['1st', '2nd', '3rd', '4th', '5th','6th'] )

print(rows_index)


# In[38]:


rows_index =pd.DataFrame(data, columns=['city', 'year', 'ratio'])

print(rows_index)


# In[40]:


rows_index =pd.DataFrame(data, columns=['year', 'city', 'ratio'])

print(rows_index)


# In[27]:


frame2 = pd.DataFrame(data, 
                      columns=['year', 'state', 'pop', 'debt'],
                      index=['one', 'two', 'three', 'four','five', 'six'])

#print(frame2)
frame2.head()   # Head function used for displayed 1st 5 rows


# In[28]:


frame2.head(3)


# # displaying index and columns names

# In[29]:


print(frame2.columns)
print( frame2.index )


# In[30]:


frame2.columns


# # A column in a DataFrame can be retrieved as a Series either by dict-like notation or by attribute:
# dictinary like notation to access or extract

# In[31]:


frame2["pop"]


# # there frame2 is another method , attribute style of accessing

# In[41]:


frame2.year


# In[42]:


print(frame2.loc['two'] )  # loc attribute used for specific rows location
print()
frame2.head()


# # Columns can be modified by assignment. For example, the empty 'debt' column could be assigned a scalar value or an array values:¶

# In[43]:


frame2['debt'] = 16.5
frame2.head()


# In[44]:


val = pd.Series([-1.2, -1.5, -1.7, 2.6], index=['two', 'four', 'five', 'six'])

frame2['debt'] = val  # in debt column adding values
frame2


# In[60]:


val = pd.Series([-1.2, -1.5, -1.7, 2.6, 10, 20])#index=['two', 'four', 'five', 'six'])

frame2['debt'] = val  # in debt column adding values
frame2


# # Deleting data (row or column from dataframe)

# In[58]:


import numpy as np
import pandas as pd

random = np.arange(25)
print(random)

data = np.arange(25).reshape((5, 5))
data


# In[71]:


import numpy as np
import pandas as pd

data = pd.DataFrame(np.arange(16).reshape((4, 4)),   # random generate values
             index=['a', 'b', 'c', 'd'],
             columns=['one', 'two', 'three', 'four'])

print(data)


# # Deleting columns from dataframe

# In[72]:


data


# In[78]:


datas = data.drop('two', axis=1)
print(datas)


# In[79]:


data.drop('three', axis=1, inplace = True)
print(data)


# # Deleting specific rows from DataFrame

# In[82]:


import numpy as np
import pandas as pd

data = pd.DataFrame(np.arange(16).reshape((4, 4)),   # random generate values
             index=['a', 'b', 'c', 'd'],
             columns=['one', 'two', 'three', 'four'])

print(data)


# In[83]:


print(frame2)


# In[84]:


data.drop('two', axis= 1, inplace= True)
print(data)


# # Selection with loc and iloc

# In[90]:


import pandas as pd

data = pd.DataFrame(np.arange(16).reshape((4, 4)), 
             index=['on', 'tw', 'th', 'fo'],
             columns=['one', 'two', 'three', 'four'])
print(data)


# In[92]:


print( data.loc[['th', 'fo'], ['three', 'four'] ] )


# In[94]:


print( data.iloc[1: 3, [3, 0, 1] ] )


# In[96]:


print( data.iloc[:])


# In[97]:


sample_df= pd.read_csv("G:/Anum phd thesis/thesis data/phd thesis/Data_Set_4/Data_Set/Features_extracted_of_all_mental_disorder/Shezophrenia/schizophrenia.csv")
print(sample_df)


# In[98]:


sample_df.info()


# In[ ]:





# In[ ]:





# In[ ]:




