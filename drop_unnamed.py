import pandas as pd
import csv

# read_csv function which is used to read the required CSV file
data = pd.read_csv('shooting_stats_cleaned.csv')

"""
data.drop('Unnamed: 9', inplace=True, axis=1)
data.drop('Unnamed: 16', inplace=True, axis=1)
data.drop('Unnamed: 23', inplace=True, axis=1)
data.drop('Unnamed: 26', inplace=True, axis=1)
data.drop('Unnamed: 29', inplace=True, axis=1)
data.drop('Unnamed: 32', inplace=True, axis=1)
"""

data.drop('Rk', inplace=True, axis=1)
data.drop('0', inplace=True, axis=1)
data.drop(data.columns[0], inplace=True, axis=1)


data.to_csv("shooting_stats_cleaned.csv")