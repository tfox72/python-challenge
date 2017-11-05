
# coding: utf-8

# ## Option 3: PyBoss
# 
# ![Boss](Images/boss.jpg)
# 
# In this challenge, you get to be the _boss_. You oversee hundreds of employees across the country developing Tuna 2.0, a world-changing snack food based on canned tuna fish. Alas, being the boss isn't all fun, games, and self-adulation. The company recently decided to purchase a new HR system, and unfortunately for you, the new system requires employee records be stored completely differently.
# 
# Your task is to help bridge the gap by creating a Python script able to convert your employee records to the required format. Your script will need to do the following:
# 
# * Import the `employee_data1.csv` and `employee_data2.csv` files, which currently holds employee records like the below:
# 
# 
# ```
# Emp ID,Name,DOB,SSN,State
# 214,Sarah Simpson,1985-12-04,282-01-8166,Florida
# 15,Samantha Lara,1993-09-08,848-80-7526,Colorado
# 411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
# ```
# 
# * Then convert and export the data to use the following format instead:
# 
# 
# ```
# Emp ID,First Name,Last Name,DOB,SSN,State
# 214,Sarah,Simpson,12/04/1985,***-**-8166,FL
# 15,Samantha,Lara,09/08/1993,***-**-7526,CO
# 411,Stacy,Charles,12/20/1957,***-**-8526,PA
# ```
# 
# * In summary, the required conversions are as follows:
# 
#   * The `Name` column should be split into separate `First Name` and `Last Name` columns.
# 
#   * The `DOB` data should be re-written into `DD/MM/YYYY` format.
# 
#   * The `SSN` data should be re-written such that the first five numbers are hidden from view.
# 
#   * The `State` data should be re-written as simple two-letter abbreviations.
# 
# * Special Hint: You may find this link to be helpfulâ€”[Python Dictionary for State Abbreviations](https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5).
# 

# In[356]:

import pandas as pd


# In[357]:

emp1 = pd.read_csv('employee_data1.csv')


# In[358]:

emp2 = pd.read_csv('employee_data2.csv')


# In[359]:

frames = [emp1,emp2]
emp3 = pd.concat(frames)


# In[360]:

splitemp1 = pd.DataFrame()
splitemp1[['First Name','Last Name']] = emp3['Name'].str.split(' ',expand=True)
splitemp1.head()


# In[361]:

emp3['DOB']= pd.DatetimeIndex(emp3.DOB)


# In[362]:


dob2 = emp3['DOB'].dt.strftime('%m/%d/%Y')
dob3 = pd.DataFrame(dob2)


# In[363]:

df= pd.DataFrame(emp3)
df[['a','b','SSN2']] = df['SSN'].str.split('-',expand=True)
df['SSN2'] = 'xxx-xx-' + df['SSN2'].astype(str)


# In[372]:

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


# In[373]:

df.replace({"State": us_state_abbrev},inplace=True)


# In[374]:

df1= df[['Emp ID','State','SSN2']]


# In[375]:

result = pd.concat([df1, splitemp1,dob3], axis=1, join='inner')


# In[379]:

table= ['Emp ID','First Name','Last Name','DOB','SSN2','State']


# In[381]:

result = result[table]
result.head()


# In[ ]:



