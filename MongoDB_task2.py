#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pymongo
import ssl
import csv
import json
import pandas as pd
user_name="root"
pw="root"

client = pymongo.MongoClient(f"mongodb+srv://{user_name}:{pw}@cluster0.cgpw3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)


# In[2]:


data_base="NewsDump"
db=client[data_base]


# In[3]:


collection_name="InfoQ"
demo_col_name=db[collection_name]


# In[23]:


data_base="NewsDump"
db=client[data_base]
mng_db = client['db'] 
collection_name = 'InfoQ'
db_cm = mng_db[collection_name]
data = pd.read_csv(r"C:\Users\AMI\Downloads\News_Details_task.csv")
data_json = json.loads(data.to_json(orient='records'))
db_cm.remove()
db_cm.insert(data_json)


# In[22]:


myquery = { "Article Date": "Nov 19, 2021" }

mydoc = db_cm.find(myquery)

for x in mydoc:
    print(x) 


# In[ ]:




