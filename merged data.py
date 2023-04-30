#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install os')
import os
os.getcwd()
import pandas as pd
pd


# In[2]:


dataset16= pd.read_csv(r"C:\Users\RIC\OneDrive\Documents\domestic_visitors\domestic_visitors_2016.csv")
dataset17= pd.read_csv(r"C:\Users\RIC\OneDrive\Documents\domestic_visitors\domestic_visitors_2017.csv")
dataset18= pd.read_csv(r"C:\Users\RIC\OneDrive\Documents\domestic_visitors\domestic_visitors_2018.csv")
dataset19= pd.read_csv(r"C:\Users\RIC\OneDrive\Documents\domestic_visitors\domestic_visitors_2019.csv")



# In[3]:


data16=pd.read_csv(r"C:\Users\RIC\OneDrive\Documents\foreign_visitors\foreign_visitors_2016.csv")
data17=pd.read_csv(r"C:\Users\RIC\OneDrive\Documents\foreign_visitors\foreign_visitors_2017.csv")
data18=pd.read_csv(r"C:\Users\RIC\OneDrive\Documents\foreign_visitors\foreign_visitors_2018.csv")
data19=pd.read_csv(r"C:\Users\RIC\OneDrive\Documents\foreign_visitors\foreign_visitors_2019.csv")
df_merged16_17 = data16.merge(data17, how='outer')
df_merged17_18 = df_merged16_17.merge(data18, how='outer')
df_merged18_19 = df_merged17_18.merge(data19, how='outer')
merged_foreign_data=df_merged18_19
merged_foreign_data


# In[42]:


import os
os.getcwd()


# In[44]:


merged_foreign_data.to_csv('merged_foreign_data',index=False)
merged_domestic_data.to_csv('merged_domestic_data',index=False)


# In[4]:


df_merged1617 = dataset16.merge(dataset17, how='outer')


# In[5]:


df_merged1718 = dataset17.merge(dataset18, how='outer')


# In[6]:


df_merged1819 = dataset18.merge(dataset19, how='outer')


# In[7]:


df_merged1= df_merged1617.merge(df_merged1718,how='outer')
df_merged= df_merged1.merge(df_merged1819,how='outer')


# In[8]:


merged_domestic_data=df_merged
merged_domestic_data


# In[9]:


domestic_visitors=merged_domestic_data
foreign_visitors= merged_foreign_data


# In[50]:


#TOP 10 DISTRICTS


# In[11]:


import pandas as pd

# Load the dataset into a DataFrame
df = pd.read_csv(r'C:\Users\RIC\OneDrive\Desktop\New folder\domestic_visitors.csv')

# Filter the data by year
df_filtered = df[(df['year'] >= 2016) & (df['year'] <= 2019)]

# Group the data by district and sum the visitors
visitors_by_district = df_filtered.groupby('district')['visitors'].sum()

# Sort the districts by the number of visitors in descending order and take the top 10
top_10_districts = visitors_by_district.sort_values(ascending=False).head(10)

# Print the top 10 districts
print(top_10_districts)


# In[15]:


get_ipython().system('pip install matplotlib')


# In[34]:


# Create a bar chart
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\RIC\OneDrive\Desktop\New folder\domestic_visitors.csv')
visitors_by_district_year = df.groupby(['district', 'year'])['visitors'].sum().reset_index()


# In[47]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a DataFrame
df = pd.read_csv(r'C:\Users\RIC\OneDrive\Desktop\New folder\domestic_visitors.csv')
# Group the data by district and sum the visitors
visitors_by_district = df.groupby('district')['visitors'].count()

# Sort the districts by the number of visitors in descending order
visitors_by_district = visitors_by_district.sort_values(ascending=False)


# In[54]:


#2.	List down the top 3 districts based on compounded annual growth rate (CAGR) of visitors between (2016 - 2019)?
##Domestic


# In[53]:


import pandas as pd


# Convert the visitors column to numeric values
df['visitors'] = pd.to_numeric(df['visitors'], errors='coerce')

# Filter the data to only include years 2016-2019
df = df[df['year'].isin([2016, 2017, 2018, 2019])]

# Group the data by district and calculate the total visitors for each year
visitors_by_district_year = df.groupby(['district', 'year'])['visitors'].sum().reset_index()

# Pivot the data to create columns for each year
visitors_by_district = visitors_by_district_year.pivot(index='district', columns='year', values='visitors').reset_index()

# Calculate the CAGR for each district between 2016 and 2019
visitors_by_district['CAGR'] = (visitors_by_district[2019] / visitors_by_district[2016]) ** (1/3) - 1

# Sort the districts by CAGR in descending order and select the top 3
top_3_districts = visitors_by_district.sort_values(by='CAGR', ascending=False).head(3)['district'].tolist()

print("Top 3 districts based on CAGR of visitors (2016-2019):", top_3_districts)


# In[55]:


#2.	List down the top 3 districts based on compounded annual growth rate (CAGR) of visitors between (2016 - 2019)?
##Foreign


# In[56]:


import pandas as pd

# Load the dataset into a DataFrame
df = pd.read_csv(r'C:\Users\RIC\OneDrive\Desktop\New folder\foreign_visitors.csv')

# Convert the visitors column to numeric values
df['visitors'] = pd.to_numeric(df['visitors'], errors='coerce')

# Filter the data to only include years 2016-2019
df = df[df['year'].isin([2016, 2017, 2018, 2019])]

# Group the data by district and calculate the total visitors for each year
visitors_by_district_year = df.groupby(['district', 'year'])['visitors'].sum().reset_index()

# Pivot the data to create columns for each year
visitors_by_district = visitors_by_district_year.pivot(index='district', columns='year', values='visitors').reset_index()

# Calculate the CAGR for each district between 2016 and 2019
visitors_by_district['CAGR'] = (visitors_by_district[2019] / visitors_by_district[2016]) ** (1/3) - 1

# Sort the districts by CAGR in descending order and select the top 3
top_3_districts = visitors_by_district.sort_values(by='CAGR', ascending=False).head(3)['district'].tolist()

print("Top 3 districts based on CAGR of visitors (2016-2019):", top_3_districts)


# In[ ]:


#3.	List down the bottom 3 districts based on compounded annual growth rate (CAGR) of visitors between (2016 - 2019)?
##Domestic


# In[57]:


import pandas as pd

# Load the dataset into a DataFrame
df = pd.read_csv(r'C:\Users\RIC\OneDrive\Desktop\New folder\domestic_visitors.csv')

# Convert the visitors column to numeric values
df['visitors'] = pd.to_numeric(df['visitors'], errors='coerce')

# Filter the data to only include years 2016-2019
df = df[df['year'].isin([2016, 2017, 2018, 2019])]

# Group the data by district and calculate the total visitors for each year
visitors_by_district_year = df.groupby(['district', 'year'])['visitors'].sum().reset_index()

# Pivot the data to create columns for each year
visitors_by_district = visitors_by_district_year.pivot(index='district', columns='year', values='visitors').reset_index()

# Calculate the CAGR for each district between 2016 and 2019
visitors_by_district['CAGR'] = (visitors_by_district[2019] / visitors_by_district[2016]) ** (1/3) - 1

# Sort the districts by CAGR in ascending order and select the bottom 3
bottom_3_districts = visitors_by_district.sort_values(by='CAGR', ascending=True).head(3)['district'].tolist()

print("Bottom 3 districts based on CAGR of visitors (2016-2019):", bottom_3_districts)


# In[58]:


#3.	List down the bottom 3 districts based on compounded annual growth rate (CAGR) of visitors between (2016 - 2019)?
##foreign


# In[59]:


# Load the dataset into a DataFrame
df = pd.read_csv(r'C:\Users\RIC\OneDrive\Desktop\New folder\foreign_visitors.csv')

# Convert the visitors column to numeric values
df['visitors'] = pd.to_numeric(df['visitors'], errors='coerce')

# Filter the data to only include years 2016-2019
df = df[df['year'].isin([2016, 2017, 2018, 2019])]

# Group the data by district and calculate the total visitors for each year
visitors_by_district_year = df.groupby(['district', 'year'])['visitors'].sum().reset_index()

# Pivot the data to create columns for each year
visitors_by_district = visitors_by_district_year.pivot(index='district', columns='year', values='visitors').reset_index()

# Calculate the CAGR for each district between 2016 and 2019
visitors_by_district['CAGR'] = (visitors_by_district[2019] / visitors_by_district[2016]) ** (1/3) - 1

# Sort the districts by CAGR in ascending order and select the bottom 3
bottom_3_districts = visitors_by_district.sort_values(by='CAGR', ascending=True).head(3)['district'].tolist()

print("Bottom 3 districts based on CAGR of visitors (2016-2019):", bottom_3_districts)


# In[60]:


#To determine the peak and low season months for Hyderabad district based on the data from 2016 to 2019,
#Filter the data to include only the Hyderabad district and the years 2016-2019.
#Group the data by month and calculate the total number of visitors for each month.
#Sort the data by the number of visitors in descending order to identify the peak season months.
#Sort the data by the number of visitors in ascending order to identify the low season months.


# In[ ]:


#Foreign_data


# In[61]:


import pandas as pd

# Load the dataset into a DataFrame
df = pd.read_csv(r'C:\Users\RIC\OneDrive\Desktop\New folder\foreign_visitors.csv')

# Filter the data to include only Hyderabad district and years 2016-2019
hyd_data = df[(df['district'] == 'Hyderabad') & (df['year'].isin([2016, 2017, 2018, 2019]))]

# Group the data by month and calculate the total visitors for each month
visitors_by_month = hyd_data.groupby('month')['visitors'].sum().reset_index()

# Sort the data by the number of visitors in descending order to identify the peak season months
peak_season = visitors_by_month.sort_values('visitors', ascending=False)

# Sort the data by the number of visitors in ascending order to identify the low season months
low_season = visitors_by_month.sort_values('visitors')

# Print the peak and low season months
print("Peak season months for Hyderabad:", peak_season['month'].tolist()[:3])
print("Low season months for Hyderabad:", low_season['month'].tolist()[:3])


# In[ ]:


#Domestic-data


# In[62]:


import pandas as pd

# Load the dataset into a DataFrame
df = pd.read_csv(r'C:\Users\RIC\OneDrive\Desktop\New folder\domestic_visitors.csv')

# Filter the data to include only Hyderabad district and years 2016-2019
hyd_data = df[(df['district'] == 'Hyderabad') & (df['year'].isin([2016, 2017, 2018, 2019]))]

# Group the data by month and calculate the total visitors for each month
visitors_by_month = hyd_data.groupby('month')['visitors'].sum().reset_index()

# Sort the data by the number of visitors in descending order to identify the peak season months
peak_season = visitors_by_month.sort_values('visitors', ascending=False)

# Sort the data by the number of visitors in ascending order to identify the low season months
low_season = visitors_by_month.sort_values('visitors')

# Print the peak and low season months
print("Peak season months for Hyderabad:", peak_season['month'].tolist()[:3])
print("Low season months for Hyderabad:", low_season['month'].tolist()[:3])


# In[3]:


import pandas as pd
datamerged=pd.read_csv(r'C:\Users\RIC\OneDrive\Desktop\New folder\merged_data.csv')
datamerged.head()


# In[8]:


import pandas as pd

# Load the 2020 domestic and foreign visitor data into dataframes
domestic_2020 = pd.read_csv(r"C:\Users\RIC\OneDrive\Desktop\New folder\domestic_visitor_2020.csv")
foreign_2020 = pd.read_csv(r"C:\Users\RIC\OneDrive\Desktop\New folder\foreign_visitor_2020.csv")

# Add a "year" column to each dataframe and set it to 2020
domestic_2020["year"] = 2020
foreign_2020["year"] = 2020

# Merge the two dataframes together using "district", "date", and "month" as the key columns
merged_2020 = pd.merge(domestic_2020, foreign_2020, on=["district", "date", "month"])

# Select only the "district", "date", "month", "domestic_visitor", and "foreign_visitor" columns
selected_2020 = merged_2020[["district", "date", "month", "domestic_visitor", "foreign_visitor"]]

# Append the selected data to your existing merged csv file
merged = pd.read_csv("merged_data.csv")
merged = pd.concat([merged, selected_2020])

# Save the updated merged csv file
merged.to_csv("merged_data.csv", index=False)


# In[ ]:




