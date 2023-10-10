#http://www.kocw.net/home/search/kemView.do?kemId=1380589&ar=relateCourse
#https://toward-the-future.tistory.com/entry/Python-파이참Pycharm-설치-및-아나콘다anaconda-가상환경-연동하기
#https://ybworld.tistory.com/42

import pandas as pd


sub = pd.Series(['국어', '수학', '영어'], index = [0, 1, 2])


subs = ['국어', '수학', '영어']
scores = [96, 88, 70]

DataSet = list(zip(subs, scores))
df1 = pd.DataFrame(data = DataSet, columns = ['과목', '점수'])


df2 = pd.read_excel("score.xlsx", engine = "openpyxl", sheet_name="Sheet1", header = 0)
df3 = pd.read_excel("score.xlsx", engine="openpyxl", usecols="A, B", names=['subjects', 'scores'])

print(df3)

df2.to_excel('test_score.xlsx')