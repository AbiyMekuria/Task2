#!/usr/bin/env python
# coding: utf-8

# ## QKN1 - QKN1 Task 2: Coding
# # Analytics Programming - D598
# 
# # PRFA — QKN1

# # A:PYTHON PROGRAM
# 

# In[1]:


# Loading library
import numpy as np
import pandas as pd


# ### Data Loading and Displaying

# In[2]:


df = pd.read_excel("C:/Users/behailu/Desktop/WGU-Workspace/D598 Data Set.xlsx")
df2 = df.groupby("Business State").mean(numeric_only=True)
df2.head()


# # Calculating Debt to Equity using Total Long-term Debt and Total Equity
# 

# In[3]:


#  Debt-to-Equity ratio
df["Debt_to_Equity_Calc"] = df["Total Long-term Debt"] / df["Total Equity"]

df["Debt_to_Equity_Calc"]


# # Creating analyzed data summary

# In[4]:


# Create summary table
summary_table = df[["Business ID", "Business State", "Debt_to_Equity_Calc", "Profit Margin"]].copy()
summary_table["Debt_to_Equity_Calc"] = summary_table["Debt_to_Equity_Calc"].round(2)
summary_table["Profitability"] = summary_table["Profit Margin"].apply(
    lambda x: "Profitable" if x > 0 else "Not Profitable"
)
summary_table


# # Saving Result

# In[5]:


## Save results 
df.to_csv("business_analysis_results.csv", index=False)
print("\nResults saved to business_analysis_results.csv")


# # WORK CITED

# #https://www.linkedin.com/learning/data-ingestion-with-python/working-in-csv?resume=false&u=2045532
# 

# #https://research.ebsco.com/c/25xrgu/ebook-viewer/pdf/4tlx4d5mhn/page/pp_53

# #https://www.linkedin.com/learning/python-for-data-science-essential-training-part-1/filtering-and-selecting?resume=false&u=2045532

# In[ ]:




