
# coding: utf-8

# ## Option 2: PyPoll
# 
# ![Vote-Counting](Images/Vote_counting.jpg)
# 
# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
# 
# You will be given two sets of poll data (`election_data_1.csv` and `election_data_2.csv`). Each dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
# 
# * The total number of votes cast
# 
# * A complete list of candidates who received votes
# 
# * The percentage of votes each candidate won
# 
# * The total number of votes each candidate won
# 
# * The winner of the election based on popular vote.
# 
# As an example, your analysis should look similar to the one below:
# 
# ```
# Election Results
# -------------------------
# Total Votes: 620100
# -------------------------
# Rogers: 36.0% (223236)
# Gomez: 54.0% (334854)
# Brentwood: 4.0% (24804)
# Higgins: 6.0% (37206)
# -------------------------
# Winner: Gomez
# -------------------------

# In[1]:

import pandas as pd


# In[2]:

elect_df = pd.read_csv('election_data_2.csv')


# In[3]:

total_votes = elect_df["Voter ID"].count()
total_votes


# In[4]:

canidates = elect_df.groupby('Candidate').County.count()
canidates


# In[5]:

canidate2 = pd.DataFrame(canidates)
canidate2.reset_index(inplace=True)
canidate2.rename(columns={'County':'Votes'},inplace=True)
canidate2


# In[6]:

winner = canidate2.iloc[1, 0]


# In[7]:

winner2 = "Winner " + winner


# In[8]:

percent = (canidate2.iloc[:,1]/total_votes).apply('{:.0%}'.format)
percent2 = pd.DataFrame(percent)
percent2.rename(columns={'Votes':'Percentage'},inplace=True)
percent2


# In[9]:

table = pd.concat([canidate2,percent2], axis=1)
table


# In[10]:

print('Election Results')
print('----------------')
total_votes2 = 'Total Votes: ' + str(total_votes)
print(total_votes2)
print('----------------')
print(table)
print('----------------')
print(winner2)


# In[ ]:




# In[ ]:



