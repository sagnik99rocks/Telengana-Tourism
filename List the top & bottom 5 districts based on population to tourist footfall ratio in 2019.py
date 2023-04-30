#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')

get_ipython().system('pip install numpy')

get_ipython().system('pip install plotly')

get_ipython().system('pip install bs4')

get_ipython().system('pip install requests')


# In[2]:


import pandas as pd
import numpy as np
import plotly.express as px
from bs4 import BeautifulSoup
import requests


# In[8]:


dataset16= pd.read_csv(r"C:\Users\RIC\OneDrive\Documents\domestic_visitors\domestic_visitors_2016.csv")
dataset17= pd.read_csv(r"C:\Users\RIC\OneDrive\Documents\domestic_visitors\domestic_visitors_2017.csv")
dataset18= pd.read_csv(r"C:\Users\RIC\OneDrive\Documents\domestic_visitors\domestic_visitors_2018.csv")
dataset19= pd.read_csv(r"C:\Users\RIC\OneDrive\Documents\domestic_visitors\domestic_visitors_2019.csv")
#merging all domestic csv files in one in pandas
domesticcombined=pd.concat([dataset16, dataset17, dataset18, dataset19], ignore_index=True)
domesticcombined=domesticcombined.dropna()
domesticcombined.to_csv('domesticcombined.csv', index=False)


# In[10]:


data16=pd.read_csv(r"C:\Users\RIC\OneDrive\Documents\foreign_visitors\foreign_visitors_2016.csv")
data17=pd.read_csv(r"C:\Users\RIC\OneDrive\Documents\foreign_visitors\foreign_visitors_2017.csv")
data18=pd.read_csv(r"C:\Users\RIC\OneDrive\Documents\foreign_visitors\foreign_visitors_2018.csv")
data19=pd.read_csv(r"C:\Users\RIC\OneDrive\Documents\foreign_visitors\foreign_visitors_2019.csv")
#merging all domestic csv files in one in pandas
foreigncombined=pd.concat([dataset16, dataset17, dataset18, dataset19], ignore_index=True)
foreigncombined=domesticcombined.dropna()
foreigncombined.to_csv('foreigncombined.csv', index=False)


# In[14]:


foreigncombined['visitors']=pd.to_numeric(foreigncombined['visitors'],errors='coerce')
domesticcombined['visitors']=pd.to_numeric(domesticcombined['visitors'],errors='coerce')


# In[51]:


populus2011=pd.read_csv(r'C:\Users\RIC\OneDrive\Desktop\telengana-tourism\census_data.csv')
url='https://www.indiacensus.net/states/telangana'
r=requests.get(url)
soup=BeautifulSoup(r.content)
populus23=[]
table=soup.select('table.pincode-tbl')[4]
for el in table.find_all("div", attrs={"class":"txt-right"}):
    populus23.append(el.get_text())


# In[52]:


populus23.pop(0)
populus23=populus23[1::2]
populus23=[int(s.replace(',','')) for s in populus23]
populus23.pop(16)
populus23.pop(19)
populus2011['est._pop_23']=populus23
populus2011['growthrateperyear']=((populus2011['est._pop_23']-populus2011['Total'])/populus2011['Total'])*100/12
populus2011['est._pop_19']=populus2011['Total']*(1+populus2011['growthrateperyear']/100*8)
populus2011['est._pop_19']=populus2011['est._pop_19'].round(decimals=2)
populus2011.drop(25,inplace=True)


# In[59]:


dcsum=domesticcombined[["district","visitors"]]
dv=domesticcombined[['year','district','visitors']]
fv=foreigncombined[['year','district','visitors']]
dv=dv[dv['year']==2019]
fv=fv[fv['year']==2019]
dv=dv.groupby(['district'])['visitors'].sum()
fv=fv.groupby(['district'])['visitors'].sum()
print(len(dv))
print(len(fv))


# In[64]:


populus2011 = populus2011.reset_index(drop=True)


# In[65]:


print(len(populus2011))


# In[66]:


dv = dv[:30]
fv = fv[:30]

totaltourists = dv.values + fv.values
populus2011['totaltourists'] = totaltourists
populus2011['totaltourists']=populus2011['totaltourists'].round(decimals=2)
populus2011['footfall_ratio']=populus2011['totaltourists']/populus2011['est._pop_19']


# In[72]:


populustop5=populus2011.head(5)
populustail5=populus2011.tail(5)


# In[73]:


import plotly.express as px

top5fig = px.bar(populustop5, x='footfall_ratio', y='district')

top5fig.update_layout(
    title={
        'text': "Top 5 Districts by Footfall Ratio",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

top5fig.show()


# In[74]:


import plotly.express as px

top5fig = px.bar(populustail5, x='footfall_ratio', y='district')

top5fig.update_layout(
    title={
        'text': "Bottom 5 Districts by Footfall Ratio",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

top5fig.show()


# In[76]:


com5pd=[populustop5,populustail]
com5pd=pd.concat(com5pd)
com5pd['footfall_ratio']=com5pd['footfall_ratio'].astype(float).round(decimals=4)
com5pdfig=px.line(com5pd,x='district',y='footfall_ratio',text='footfall_ratio',template='plotly_white',color_discrete_sequence=px.colors.sequential.Greens_r).update_layout(font=dict(size=30)).update_traces(line=dict(width=5))
com5pdfig.show()


# In[ ]:




