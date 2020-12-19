# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 08:47:02 2020

@author: dunij
"""

import pandas as pd

filename = 'chicago.csv'

# load data file into a dataframe
df = pd.read_csv(filename)


# display total travel time
print("total travel time: ",df["Trip Duration"].sum()) 

# display mean travel time
print("mean travel time: ",df["Trip Duration"].mean())

