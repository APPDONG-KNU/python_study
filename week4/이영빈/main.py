from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

issues = pd.read_csv('issues.csv')
prs = pd.read_csv('prs.csv')
repos = pd.read_csv('repos.csv')

print(issues, "\n")

del issues['quarter']

df = pd.DataFrame(issues.groupby(['name'])['count'].sum().sort_values(ascending=False))
print(df)
dfy = pd.DataFrame(issues.groupby(['year', 'name'])['count'].sum())
print(dfy)

print(dfy.index)
df_2011 = dfy[dfy.index.get_level_values('year') == 2011]
df_2011 = df_2011.sort_values(by='count', ascending=False)

df_2012 = dfy[dfy.index.get_level_values('year') == 2012]
df_2012 = df_2012.sort_values(by='count', ascending=False)

df_2013 = dfy[dfy.index.get_level_values('year') == 2013]
df_2013 = df_2013.sort_values(by='count', ascending=False)

df_2014 = dfy[dfy.index.get_level_values('year') == 2014]
df_2014 = df_2014.sort_values(by='count', ascending=False)

df_2015 = dfy[dfy.index.get_level_values('year') == 2015]
df_2015 = df_2015.sort_values(by='count', ascending=False)

df_2016 = dfy[dfy.index.get_level_values('year') == 2016]
df_2016 = df_2016.sort_values(by='count', ascending=False)

df_2017 = dfy[dfy.index.get_level_values('year') == 2017]
df_2017 = df_2017.sort_values(by='count', ascending=False)

df_2018 = dfy[dfy.index.get_level_values('year') == 2018]
df_2018 = df_2018.sort_values(by='count', ascending=False)

df_2019 = dfy[dfy.index.get_level_values('year') == 2019]
df_2019 = df_2019.sort_values(by='count', ascending=False)

df_2020 = dfy[dfy.index.get_level_values('year') == 2020]
df_2020 = df_2020.sort_values(by='count', ascending=False)

df_2021 = dfy[dfy.index.get_level_values('year') == 2021]
df_2021 = df_2021.sort_values(by='count', ascending=False)

df_2022 = dfy[dfy.index.get_level_values('year') == 2022]
df_2022 = df_2022.sort_values(by='count', ascending=False)


plt.figure(figsize=(13, 7))
plt.xlabel('Language')
plt.ylabel('Count')
plt.bar(df_2011.index.get_level_values('name').to_list(), df_2011['count'].to_list(), width=0.6)
plt.title("2011's")
plt.xticks(fontsize=10, rotation=45)
plt.yticks(fontsize=10)
plt.show()

df_2022.to_excel('iss_2022.xlsx')
