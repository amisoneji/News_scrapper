#!/usr/bin/env python
# coding: utf-8

# In[23]:



from bs4 import BeautifulSoup
import requests 
from selenium import webdriver
import time
from datetime import timedelta
import pandas as pd
driver = webdriver.Chrome(r"C:\Users\AMI\Downloads\chromedriver")


# In[24]:


tags=[]
title=[]
content=[]
url_href=[]
date=[]
url="https://www.infoq.com/ai-ml-data-eng/news/"

pages=0
doamin_name="https://www.infoq.com"

max_pages=10
#nxt = driver.find_element_by_class_name('button button__small button__arrow arrow__right')
#nxt.click()
#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'OLDER'))).click()
while (pages < max_pages):
    try:
        #next_page = driver.find_elements_by_class_name('button button__small button__arrow arrow__right')
        #driver.execute_script("$(arguments[0]).click();", next_page)
        #time.sleep(0.5)

        driver.get(url)

        time.sleep(3)

        soup = BeautifulSoup(driver.page_source,"html.parser")

        for item in soup.findAll('div', attrs={'class': 'items__content columns'}):
            new = item.findAll('div', attrs={'class': 'card__content'})
            tag = item.findAll('div', attrs={'class': 'card__topics topics'})
            titles = item.findAll('h3', attrs={'class': 'card__title'})
            contents = item.findAll('p', attrs={'class': 'card__excerpt'})
            urls = item.findAll('h3', attrs={'class': 'card__title'})
            dates = item.findAll('span', attrs={'class': 'card__date date'})

            for i in tag:
                tags.append(i.text.strip())
            for t in titles:
                title.append(t.text.strip())
            for con in contents:
                content.append(con.text.strip())
            for u in urls:
                url_href.append(doamin_name+u.find('a').get('href'))
            for d in dates:

                date.append((d.find('span').contents[0]).strip())
                print(d.find('span').contents[0])
            next = driver.find_element_by_css_selector("a[title='Older']")
            next.click()
            url=driver.current_url

            print("Navigating to Next Page")
            pages=pages+1
        print("success")
    except:
          print("An exception occurred")



# In[25]:


df = pd.DataFrame({'Article Tag': tags,
                   'Article Headline': title,
                   'Article Description': content,
                   'Article url': url_href,
                   'Article Date':date
                   })


# In[26]:


df.isnull().sum()


# In[27]:


df.to_csv("NewsDetails1.csv")


# In[ ]:




