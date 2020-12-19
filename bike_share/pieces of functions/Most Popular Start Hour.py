# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 08:14:40 2020

@author: dunij
"""

import pandas as pd

filename = 'chicago.csv'

# load data file into a dataframe
df = pd.DataFrame(pd.read_csv(filename))


# convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract hour from the Start Time column to create an hour column
df['hour'] = df['Start Time'].dt.hour

# the most common hour (from 0 to 23)
popular_hour = df['hour'].mode()[0]

print('Most Frequent Start Hour:', popular_hour)


    
