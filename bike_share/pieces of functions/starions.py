# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 08:00:17 2020

@author: dunij
"""

import pandas as pd

filename = 'chicago.csv'

# load data file into a dataframe
df = pd.read_csv(filename)



# display most commonly used Start Station
popular_start_station = df['Start Station'].mode()
print('\n\nMost popular Start Station:\n', popular_start_station)


# display most commonly used End Station
popular_end_station = df['End Station'].mode()
print('\n\nMost popular End Station:\n', popular_end_station)


# most frequent combination of start station and end station
start_end_stations = (df['Start Station'] + " , " +  df['End Station']).mode()
print('\n\nMost common trip from start to end:\n', start_end_stations)

