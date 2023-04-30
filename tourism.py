#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd

# Load the domestic visitor data and the foreign visitor data into separate DataFrames
domestic_df = pd.read_csv(r'C:\Users\RIC\OneDrive\Desktop\telengana-tourism\domestic_visitors.csv')
foreign_df = pd.read_csv(r"C:\Users\RIC\OneDrive\Desktop\telengana-tourism\foreign_visitors.csv")
merged_df= pd.read_csv(r'C:\Users\RIC\OneDrive\Desktop\telengana-tourism\merged_data.csv')


# Print the merged DataFrame
print(merged_df.tail())


# In[39]:


#merged_df.to_csv('merged_data.csv', index=False)


# In[19]:


import pandas as pd
get_ipython().system('pip install matplotlib')
from matplotlib import pyplot as plt
# Group the DataFrame by district and sum the number of visitors for each district
district_totals = domestic_df.groupby('district')['visitors'].sum().reset_index()
# Sort the resulting DataFrame in descending order based on the visitors column
top_districts = district_totals.sort_values('visitors', ascending=False).reset_index(drop=True)
# Select the top 10 districts
top_districts = top_districts.head(10)




# In[20]:


plt.bar(top_districts['district'], height=1.0)
plt.xticks(rotation=90)
plt.xlabel('District')
plt.ylabel('')
plt.title('Top 10 Districts with the Highest Number of Domestic Visitors (2016-2019)')
plt.show()


# In[21]:


#CAGR = ((Ending Value / Beginning Value) ** (1 / Number of Years)) - 1


# Convert the 'visitors' column to numeric
domestic_df['visitors'] = pd.to_numeric(domestic_df['visitors'], errors='coerce')

# Group the DataFrame by district and year and sum the number of visitors for each district and year
grouped = domestic_df.groupby(['district', 'year'])['visitors'].sum().reset_index()

# Pivot the DataFrame to create separate columns for each year's visitor count
pivoted = grouped.pivot(index='district', columns='year', values='visitors')

# Calculate the CAGR for each district
pivoted['CAGR'] = ((pivoted[2019] / pivoted[2016]) ** (1/3)) - 1

# Sort the districts by their CAGR in descending order and select the top 3
top_districts = pivoted.sort_values('CAGR', ascending=False).head(3)

# Print the top 3 districts and their CAGR
print(top_districts[['CAGR']])



# In[22]:


# Convert the 'visitors' column to numeric
domestic_df['visitors'] = pd.to_numeric(domestic_df['visitors'], errors='coerce')

# Group the DataFrame by district and year and sum the number of visitors for each district and year
grouped = domestic_df.groupby(['district', 'year'])['visitors'].sum().reset_index()

# Pivot the DataFrame to create separate columns for each year's visitor count
pivoted = grouped.pivot(index='district', columns='year', values='visitors')

# Calculate the CAGR for each district
pivoted['CAGR'] = ((pivoted[2019] / pivoted[2016]) ** (1/3)) - 1

# Sort the districts by their CAGR in ascending order and select the bottom 3
bottom_districts = pivoted.sort_values('CAGR', ascending=True).head(3)

# Print the bottom 3 districts and their CAGR
print(bottom_districts[['CAGR']])


# In[23]:


import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
# Filter the DataFrame to only include data for Hyderabad district
hyderabad_df = domestic_df[domestic_df['district'] == 'Hyderabad']

# Group the DataFrame by year and month and sum the number of visitors for each month
grouped = hyderabad_df.groupby(['year', 'month'])['visitors'].sum().reset_index()

# Pivot the DataFrame to create separate columns for each year's visitor count
pivoted = grouped.pivot(index='month', columns='year', values='visitors')

# Plot a bar chart showing the total number of visitors to Hyderabad by month for each year
ax = pivoted.plot(kind='bar', figsize=(10, 6))
ax.set_title('Total Visitors to Hyderabad by Month (2016-2019)')
ax.set_xlabel('Month')
ax.set_ylabel('Total Visitors')
plt.show()


# In[24]:


print(merged_df['domestic_visitor'].isna().sum())
merged_df['domestic_visitor'] = merged_df['domestic_visitor'].fillna(0)
merged_df = merged_df.dropna(subset=['domestic_visitor'])
merged_df.head()




# In[25]:


merged_df['domestic_visitor'] = pd.to_numeric(merged_df['domestic_visitor'], errors='coerce')
merged_df['foreign_visitor'] = pd.to_numeric(merged_df['foreign_visitor'], errors='coerce')

merged_df['Domestic_to_Foreign_Ratio'] = merged_df['domestic_visitor'] / merged_df['foreign_visitor']


# In[26]:


merged_df['Domestic_to_Foreign_Ratio'] = merged_df['domestic_visitor'] / merged_df['foreign_visitor']
top_3 = merged_df.sort_values(by='Domestic_to_Foreign_Ratio', ascending=False).head(3)
bottom_3 = merged_df.sort_values(by='Domestic_to_Foreign_Ratio', ascending=True).head(3)

print("Top 3 districts with high domestic to foreign tourist ratio:")
print(top_3[['district', 'Domestic_to_Foreign_Ratio']])

print("\nBottom 3 districts with high domestic to foreign tourist ratio:")
print(bottom_3[['district', 'Domestic_to_Foreign_Ratio']])




# In[35]:


data['totals'] = data['domestic_visitor'] + data['foreign_visitor']
print(data.columns)


# In[38]:


# convert the 'totals' column to numeric datatype with 'coerce'
data['totals'] = pd.to_numeric(data['totals'], errors='coerce')

# filter the data for the year 2019
data_2019 = data[data['year'] == 2019]


# create a pivot table with the sum of visitors by district
district_pivot = pd.pivot_table(data_2019, values='totals', index='district', aggfunc='sum')

# sort the pivot table in descending order
district_pivot_sorted = district_pivot.sort_values(by='totals', ascending=False)

# list the top 5 districts based on tourist visits in 2019
print("Top 5 districts based on tourist visits in 2019:")
print(district_pivot_sorted.head(5))

# list the bottom 5 districts based on tourist visits in 2019
print("\nBottom 5 districts based on tourist visits in 2019:")
print(district_pivot_sorted.tail(5))


# In[62]:


import pandas as pd

# Read in the merged CSV file
data = pd.read_csv(r'C:\Users\RIC\OneDrive\Desktop\telengana-tourism\merged_data.csv')

# Filter data for Hyderabad district only
hyderabad_data = data[data['district'] == 'Hyderabad']
hyderabad_data['visitors'] = hyderabad_data['domestic_visitor']+ hyderabad_data['foreign_visitor']
hyderabad_data.tail()


# In[11]:


visitor_count['total_visitor'] = visitor_count['domestic_visitor'] + visitor_count['foreign_visitor']
# Calculate total number of visitors for each year
visitor_count = hyderabad_data.groupby('year')[['domestic_visitor', 'foreign_visitor']].sum()
visitor_count['total_visitor'] = visitor_count['domestic_visitor'] + visitor_count['foreign_visitor']
total_visitor = pd.to_numeric(visitor_count['total_visitor'], errors='coerce').isna()
# Convert 'total_visitor' column to numeric type
visitor_count['total_visitor'] = pd.to_numeric(visitor_count['total_visitor'], errors='coerce')

# Calculate growth rate for each year
visitor_count['growth_rate'] = (visitor_count['total_visitor'].pct_change() + 1) * 100
print(visitor_count[['growth_rate']])




# In[14]:


# Convert columns to numeric type
visitor_count['domestic_visitor'] = pd.to_numeric(visitor_count['domestic_visitor'], errors='coerce')
visitor_count['foreign_visitor'] = pd.to_numeric(visitor_count['foreign_visitor'], errors='coerce')

# Calculate growth rate
visitor_count['growth_rate'] = visitor_count['domestic_visitor'].pct_change()

# Calculate average growth rate
avg_growth_rate = visitor_count['growth_rate'].mean()

# Project number of tourists for 2025
last_year_domestic_visitor = visitor_count['domestic_visitor'].iloc[-1]
last_year_foreign_visitor = visitor_count['foreign_visitor'].iloc[-1]
projected_domestic_visitor = last_year_domestic_visitor * avg_growth_rate
projected_foreign_visitor = last_year_foreign_visitor * avg_growth_rate

# Print projected number of tourists
print(f"Projected number of domestic tourists in Hyderabad for 2025: {int(projected_domestic_visitor)}")
print(f"Projected number of foreign tourists in Hyderabad for 2025: {int(projected_foreign_visitor)}")


# In[15]:


# Calculate projected revenue
projected_domestic_revenue = projected_domestic_visitor * 4000
projected_foreign_revenue = projected_foreign_visitor * 5600
total_projected_revenue = projected_domestic_revenue + projected_foreign_revenue

# Print projected revenue
print(f"Projected revenue for domestic tourists in Hyderabad for 2025: Rs {int(projected_domestic_revenue)}")
print(f"Projected revenue for foreign tourists in Hyderabad for 2025: Rs {int(projected_foreign_revenue)}")
print(f"Total projected revenue for Hyderabad for 2025: Rs {int(total_projected_revenue)}")


# In[27]:


get_ipython().system('pip install numpy')
import numpy as np
# Group the data by district and year
district_data = data.groupby(['district', 'year']).sum().reset_index()

# Convert the string columns to integer columns
district_data['domestic_visitor'] = pd.to_numeric(district_data['domestic_visitor'], errors='coerce').fillna(0).astype(np.int64)
district_data['foreign_visitor'] = pd.to_numeric(district_data['foreign_visitor'], errors='coerce').fillna(0).astype(np.int64)

# Create the Tourist_Visitors column
district_data['Tourist_Visitors'] = district_data['domestic_visitor'] + district_data['foreign_visitor']

district_data.head()



# In[28]:


# Calculate the growth rate of tourist visitors for each district
district_data['growth_rate'] = district_data.groupby('district')['Tourist_Visitors'].pct_change()

# Get the average growth rate for each district
district_growth = district_data.groupby('district')['growth_rate'].mean()

# Sort the districts by average growth rate in descending order
district_growth.sort_values(ascending=False, inplace=True)

# Print the districts with the highest potential for tourism growth
print("Districts with the highest potential for tourism growth:")
print(district_growth.head())


# In[78]:


# filter for the Hyderabad district
hyderabad_data = data[data['district'] == 'Hyderabad']

# find the maximum number of domestic and foreign visitors
hyderabad_data['domestic_visitor'] = pd.to_numeric(hyderabad_data['domestic_visitor'])
hyderabad_data['foreign_visitor'] = pd.to_numeric(hyderabad_data['foreign_visitor'])
max_domestic_visitors = hyderabad_data['domestic_visitor'].max()
max_foreign_visitors = hyderabad_data['foreign_visitor'].max()

# print the results
print(f"Highest number of domestic visitors in Hyderabad: {max_domestic_visitors}")
print(f"Highest number of foreign visitors in Hyderabad: {max_foreign_visitors}")


# In[79]:


max_domestic_visitors = hyderabad_data.groupby('month')['domestic_visitor'].max()
max_foreign_visitors = hyderabad_data.groupby('month')['foreign_visitor'].max()

# find the months with the maximum number of visitors
max_domestic_month = max_domestic_visitors.idxmax()
max_foreign_month = max_foreign_visitors.idxmax()

# print the results
print(f"Highest number of domestic visitors in Hyderabad occurred in {max_domestic_month}: {max_domestic_visitors[max_domestic_month]}")
print(f"Highest number of foreign visitors in Hyderabad occurred in {max_foreign_month}: {max_foreign_visitors[max_foreign_month]}")


# In[80]:


# highest number of domestic visitors in Hyderabad was recorded in the month of January, with a total of 12,032,661 visitors. Similarly, the highest number of foreign visitors in Hyderabad was also recorded in the month of January, with a total of 38,933 visitors.


# In[ ]:




