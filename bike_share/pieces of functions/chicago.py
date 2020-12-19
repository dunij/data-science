# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 07:58:00 2020

@author: dunij
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 07:58:00 2020

@author: dunij
"""

import pandas as pd

df = pd.read_csv("chicago.csv")
print(df.head())  # start by viewing the first few rows of the dataset!

print(df.tail())  # start by viewing the last few rows of the dataset!

print(df.columns)  # viewing the columns of the dataset!

print(df.describe())  #  describe dataset!
print(df.info())  # start by viewing the info of the dataset!

print(df['Gender'].value_counts())  # start by viewing the the gender in  the dataset!

print(df['Start Station'].unique())  # start by viewing the uniqure Start Station of the dataset!




