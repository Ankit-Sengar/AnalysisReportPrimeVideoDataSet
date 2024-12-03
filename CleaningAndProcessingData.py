#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd


# In[11]:


raw_data = pd.read_csv("D:\\PrimeVideoAnalysisProject\\PrimeVideoDataSet\\titles.csv",index_col ="id")


# In[12]:


sample = raw_data.head()
sample


# In[14]:


#selecting only the required columns
selected_columns = raw_data[['title','type','release_year','runtime','genres','imdb_score']]
selected_columns


# In[42]:


def sortAndConcatGenre(data):
    arr = (((data[1:-1]).replace('\'','')).strip()).split(',')
    result = []
    for s in arr:
        result.append(s.strip())
    result.sort()
    result = ' & '.join(result)
    return result

selected_columns['genre'] = selected_columns.apply(lambda row: sortAndConcatGenre(row['genres']), axis=1)
selected_columns


# In[47]:


selected_columns_with_new_genre = selected_columns[['title','type','release_year','runtime','genre','imdb_score']]


# In[49]:


selected_columns_with_new_genre.to_csv('D:\\PrimeVideoAnalysisProject\\PrimeVideoProcessedDataSet\\titles.csv')


# In[ ]:




