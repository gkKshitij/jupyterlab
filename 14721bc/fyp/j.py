#!/usr/bin/env python
# coding: utf-8

# In[81]:


import pandas as pd
import numpy as np
import random


# In[107]:


datel=[]
hoursl=[]
minutesl=[]
timel=[]


# In[108]:


for i in range(1,334):
    date="29/12/2020"
    hoursl.append(random.randrange(17, 22))
    minutesl.append(random.randrange(11, 59))
    time=f"{hoursl[i-1]}:{minutesl[i-1]}"
    datel.append(date)
    timel.append(time)
    #print(random.randrange(0, 23))
    


# In[109]:


stimel=sorted(timel)


# In[110]:


df = pd.DataFrame()


# In[111]:


df['Date'] = datel 
df['Time'] = stimel


# In[112]:


df


# In[113]:


datel=[]
hoursl=[]
minutesl=[]
timel=[]


# In[114]:


for i in range(1,74):
    date="29/12/2020"
    hoursl.append(random.randrange(17, 22))
    minutesl.append(random.randrange(11, 59))
    time=f"{hoursl[i-1]}:{minutesl[i-1]}"
    datel.append(date)
    timel.append(time)
    #print(random.randrange(0, 23))


# In[115]:


stimel=sorted(timel)


# In[116]:


df2 = pd.DataFrame()


# In[117]:


df2['Date'] = datel 
df2['Time'] = stimel


# In[118]:


df2


# In[127]:


df3=pd.merge(df, df2, on='Time', how='left')


# In[128]:


df3


# In[104]:


df.to_excel('29_12_test.xlsx') 


# In[98]:


df2.to_excel('29_12_actual.xlsx') 


# In[99]:


df3.to_excel('29_12_comparison.xlsx') 


# In[ ]:





# %%
