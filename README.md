**Technology used:**
- Python 3.8
- Chrome Selenium driver
- Beautiful Soup


**Approach:**
_______________________________________________________________________________________________________________________________________________________________________________
- Single python file has been created to develop Scraper.
- Selenium driver was used to access webpage via chrome.
- Parsed html content from the accessed webpage using Class and elements name using 
BS4, this fetching data from single provided page.
- First page contains only 15 count of news, I have utilized Selenium for navigating to next 
page. for Convince, code is written to navigate up to 10 pages
- Parsed content from html page contains article_tag, article date, article 
- headline, article url, article short description; these all content will be fetch as individual 
list from all 10 webpages.
- Further all data is stored to single Dataframe.
- Dataframe then converted to CSV file
- Data stored to MondoDB cloud instance.
- Flask framework is used for creation of API.
- HTML was used to create search form which will take an input as keyword and will be 
searched from MongoDB database via API created using Flask.

**Hosted on Heroku cloud** :**https://newsscrapper1.herokuapp.com/**
