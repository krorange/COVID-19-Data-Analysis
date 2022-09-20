#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('C:\\Users\\GK228823\\Downloads\\COVID-19_Daily_Counts_of_Cases__Hospitalizations__and_Deaths.csv',
                 parse_dates=['date_of_interest']) 


# In[3]:


print(df)


# In[4]:


df.head()


# In[5]:


for col in df.columns:
    print(col)


# In[6]:


selected_columns = df[["date_of_interest","CASE_COUNT"]]


# In[7]:


df_copy = selected_columns.copy()
print(df_copy)


# In[8]:


#rename columns
df_copy.columns = ['date', 'case']


# In[9]:


#check data types
df_copy.dtypes


# In[10]:


#create year-month column
df_copy['year-month'] = df_copy['date'].dt.strftime('%Y-%m')


# In[11]:


df_copy.head()


# In[13]:


#group by year-month
gb = df_copy.groupby('year-month')


# In[14]:


#plot a line chart
fig, ax = plt.subplots(1, 1)
ax.set_title('NYC COVID-19 Case Tracker')
ax.plot_date(gb['date'].max(),
             gb['case'].mean(), '-', lw=3)
ax.set_xlabel('date')
ax.set_ylabel('number of cases')
ax.set_ylim(0)

#save plot image
plt.savefig('NYC COVID-19 Case Tracker.jpg')


# In[ ]:




