#https://wikidocs.net/185024  plotly 사용법 정리
#https://data101.oopy.io/plolty-tutorial-guide-in-korean#7a8adb06-f8cb-419b-990f-0cdc8282dc96
#https://chancoding.tistory.com/119

import pandas as pd

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots


pldb =pd.read_csv('Programming_title.csv')

del pldb['Unnamed: 0']
pldb = pldb.sort_values(by = 'usage')
pldb['CountRank'] = pldb.groupby('usage')['Count'].rank(method = 'min', ascending=False)
pldb['UserRank'] = pldb.groupby('usage')['Users'].rank(method = 'min', ascending=False)
pldb['JobRank'] = pldb.groupby('usage')['Jobs'].rank(method = 'min', ascending=False)
pldb['SalaryRank'] = pldb.groupby('usage')['Salary'].rank(method = 'min', ascending=False)
rank_columns = ['CountRank', 'UserRank', 'JobRank', 'SalaryRank']
pldb['Rank'] = pldb[rank_columns].mean(axis=1)
pldb = pldb.sort_values(by = 'Rank')
print(pldb)
print(pldb.index, pldb.columns)

fig = make_subplots(rows=2, cols=4, specs=[[{}, {}, {}, {}], [{"colspan" : 2}, None, {"colspan":2}, None]],
                    subplot_titles=("Count of PL", "Users of PL", "Jobs of PL", "Salary of PL", "Popular PL", "Good PL to work"))
pldb = pldb.sort_values(by = 'Count')
fig.add_trace(go.Bar(x=pldb.title.to_list(), y=pldb['Count'].to_list(), name = "Count"), row=1, col=1)
pldb = pldb.sort_values(by = 'Users')
fig.add_trace(go.Bar(x=pldb.title.to_list(), y=pldb['Users'].to_list(), name = "Users"), row=1, col=2)
pldb = pldb.sort_values(by = 'Jobs')
fig.add_trace(go.Bar(x=pldb.title.to_list(), y=pldb['Jobs'].to_list(), name = "Jobs"), row=1, col=3)
pldb = pldb.sort_values(by = 'Salary')
fig.add_trace(go.Bar(x=pldb.title.to_list(), y=pldb['Salary'].to_list(), name = "Salary"), row=1, col=4)

fig.add_trace(go.Scatter(x=pldb['Users'].to_list(), y=pldb['Count'].to_list(), mode='markers+text',
                         text = pldb.title.to_list(), textposition="bottom center",textfont=dict(size = 8),
                         name = "Users/Count"), row=2, col=1)
fig.add_trace(go.Scatter(x=pldb['Salary'].to_list(), y=pldb['Jobs'].to_list(), mode='markers+text',
                         text = pldb.title.to_list(), textposition="bottom center", textfont = dict(size = 8),
                         name = "Salary/Jobs"), row=2, col=3)

fig.update_xaxes(title_text = "Users", row = 2, col = 1)
fig.update_xaxes(title_text = "Salary", row = 2, col = 3)
fig.update_yaxes(title_text = "Count", row = 1, col = 1)
fig.update_yaxes(title_text = "Users", row = 1, col = 2)
fig.update_yaxes(title_text = "Jobs", row = 1, col = 3)
fig.update_yaxes(title_text = "Salary", row = 1, col = 4)
fig.update_yaxes(title_text = "Count", row = 2, col = 1)
fig.update_yaxes(title_text = "Jobs", row = 2, col = 3)

fig.show()



