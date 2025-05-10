import numpy as np
import pandas as pd
# columns are separated by tabs not commas
data = pd.read_csv('data/ab_ag.tsv', sep='\t')

# # print first few lines 
# print(data.head(n=4))
print('nein, Alisa war hier')

<<<<<<< Updated upstream
# # Inspect the dataser ab_ag.tsv
# df = pd.read_csv("data/ab_ag.tsv", sep="\t")
# print(df.shape)
# print(df.columns)
# print(df.head())
=======
# Inspect the dataser ab_ag.tsv
df = pd.read_csv("data/ab_ag.tsv", sep="\t")
print(df.shape) # dimensions dataset
print(df.columns) # column names
print(df.head()) # first 5 rows 
>>>>>>> Stashed changes
