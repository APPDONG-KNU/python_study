from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

pldb =pd.read_csv('Programming_title.csv')

del pldb['Unnamed: 0']
pldb = pldb.sort_values(by = 'usage')
pldb['CountRank'] = pldb.groupby('usage')['Count'].rank(method = 'min', ascending=False)
pldb['UserRank'] = pldb.groupby('usage')['Users'].rank(method = 'min', ascending=False)
pldb['JobRank'] = pldb.groupby('usage')['Jobs'].rank(method = 'min', ascending=False)
pldb['SalaryRank'] = pldb.groupby('usage')['Salary'].rank(method = 'min', ascending=False)
rank_columns = ['CountRank', 'UserRank', 'JobRank', 'SalaryRank']
pldb['RankMean'] = pldb[rank_columns].mean(axis=1)
pldb = pldb.sort_values(by = 'RankMean')
print(pldb)
