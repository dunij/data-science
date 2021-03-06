# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:34:20 2020

@author: dunij
"""

"""Displays statistics on bikeshare users."""
import pandas as pd

filename = 'chicago.csv'

# load data file into a dataframe
df = pd.read_csv(filename)



# print value counts for each user type
user_types = df["User Type"].value_counts(dropna=False) 
print("\n\ncounts of user types: \n" , user_types)

# print value counts for  Gender
gender = df["Gender"].value_counts(dropna=False) 
print("\n\ncounts of gender: \n" , gender)

# print  earliest  Birth Year 
print("\n\nThe earliest Birth Year: \n",df["Birth Year"].min()) 

# print The most recent Birth Year 
print("\n\nThe most recent Birth Year: \n",df["Birth Year"].max())

# print The most common of Birth Year 
print("\n\nThe most common of Birth Year: \n",df["Birth Year"].mode()) 



