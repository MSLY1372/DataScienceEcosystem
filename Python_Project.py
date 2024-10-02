#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install yfinance')


# In[ ]:


import yfinance as yf
import pandas as pd


# In[ ]:


tesla_stock_data = yf.download('TSLA', start='2010-01-01', end='2023-12-31')


# In[ ]:


tesla_stock_data.head()


# In[1]:


get_ipython().system('pip install beautifulsoup4')
get_ipython().system('pip install requests')


# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[3]:


url = 'https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue'


# In[5]:


html_data = requests.get(url).text
soup = BeautifulSoup(html_data, 'html.parser')
tables = soup.find_all('table')
tesla_revenue_table = tables[0]  


# In[ ]:


tesla_revenue = pd.read_html(str(tesla_revenue_table))[0]


# In[ ]:


tesla_revenue.columns = ['Date', 'Revenue']
tesla_revenue['Revenue'] = tesla_revenue['Revenue'].str.replace('$', '').str.replace(',', '').astype(float)


# In[ ]:


tesla_revenue.head()


# In[ ]:


gamestop_stock_data = yf.download('GME', start='2010-01-01', end='2023-12-31')


# In[ ]:


gamestop_stock_data.head()


# In[ ]:


url = 'https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue'
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, 'html.parser')


# In[ ]:


tables = soup.find_all('table')
gamestop_revenue_table = tables[1]  


# In[ ]:


gamestop_revenue = pd.read_html(str(gamestop_revenue_table))[0]


# In[ ]:


gamestop_revenue.columns = ['Date', 'Revenue']
gamestop_revenue['Revenue'] = gamestop_revenue['Revenue'].str.replace('$', '').str.replace(',', '').astype(float)


# In[ ]:


gamestop_revenue.head()


# In[ ]:


import matplotlib.pyplot as plt


# In[ ]:


tesla_stock_data.reset_index(inplace=True)
tesla_revenue['Date'] = pd.to_datetime(tesla_revenue['Date'])
tesla_dashboard = pd.merge(tesla_stock_data, tesla_revenue, left_on='Date', right_on='Date', how='inner')


# In[ ]:


fig, ax1 = plt.subplots(figsize=(14, 7))


# In[ ]:


ax1.plot(tesla_dashboard['Date'], tesla_dashboard['Close'], color='blue', label='Stock Price')
ax1.set_xlabel('Date')
ax1.set_ylabel('Stock Price (USD)', color='blue')


# In[ ]:


ax2 = ax1.twinx()
ax2.plot(tesla_dashboard['Date'], tesla_dashboard['Revenue'], color='green', label='Revenue')
ax2.set_ylabel('Revenue (USD)', color='green')


# In[ ]:


plt.title('Tesla Stock Price and Revenue Over Time')
fig.tight_layout()
plt.show()


# In[ ]:


gamestop_stock_data.reset_index(inplace=True)
gamestop_revenue['Date'] = pd.to_datetime(gamestop_revenue['Date'])
gamestop_dashboard = pd.merge(gamestop_stock_data, gamestop_revenue, left_on='Date', right_on='Date', how='inner')


# In[ ]:


fig, ax1 = plt.subplots(figsize=(14, 7))


# In[ ]:


ax1.plot(gamestop_dashboard['Date'], gamestop_dashboard['Close'], color='blue', label='Stock Price')
ax1.set_xlabel('Date')
ax1.set_ylabel('Stock Price (USD)', color='blue')


# In[ ]:


ax2 = ax1.twinx()
ax2.plot(gamestop_dashboard['Date'], gamestop_dashboard['Revenue'], color='green', label='Revenue')
ax2.set_ylabel('Revenue (USD)', color='green')


# In[ ]:


plt.title('GameStop Stock Price and Revenue Over Time')
fig.tight_layout()
plt.show()

