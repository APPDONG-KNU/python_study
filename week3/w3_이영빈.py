#https://datascienceschool.net/01%20python/04.03%20%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%94%84%EB%A0%88%EC%9E%84%20%EA%B3%A0%EA%B8%89%20%EC%9D%B8%EB%8D%B1%EC%8B%B1.html
#https://seong6496.tistory.com/364
#https://mizykk.tistory.com/132


import pandas as pd

df = pd.read_excel("weather.xlsx", engine="openpyxl", header=7,
                   names=['date', 'position', 'avtemp', 'mintemp', 'maxtemp'])
print(df, "\n")

data1 = df.loc[3]
data2 = df.loc[2:4]

print(data1, "\n")
print(type(data1), "\n")
print(data2, "\n")
print(type(data2), "\n")

data3 = df.avtemp
print(data3)
print(type(data3))

data4 = data3.to_frame()
print(data4)

data5 = data4.T   #data5 = data4.transpose()
data5.columns = ['231030', '231031', '231101', '231102','231103']
data5.index = ['평균기온']
print(data5)
data5.to_excel('AverageTemp.xlsx')