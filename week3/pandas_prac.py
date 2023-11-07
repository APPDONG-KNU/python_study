# #시리즈

import pandas as pd
import numpy as np

a=pd.Series(['a','b','c','d','e'], index=['1','2','3','4','5'])
print(a)
#인덱스 지정 안할 경우 0부터 할당됨
b=pd.Series(['a','b','c','d','e'])
print(b)

print(a.index) #dtype 과 같이 출력
print(a.values)
a.index.name='번호'

print(a[0:3]) 

print("1" in a)   # 인덱스에 있냐~?

#연산 --> 시리즈 값에만 ,, 인덱스는 상관없
#인덱싱 , 슬라이싱  --> 값이 나옴   , *문자열 슬라이싱의 경우 마지막거도 포함 (다른 자료랑은 차이 )

for key,values in a.items():
    print(f'{key}={values}')




#데이터 프레임
#일단 데이터 형태는 열방향의 딕셔너리

data={'name':['kim','lee','park'],
      'age':[17,19,18],
      'grade':['A',"C","B"]}


c=pd.DataFrame(data,index=[1,2,3])

#head는 앞에서 ()인자 안의 행 출력 tail은 끝에서 부터 출력 
head_rows=c.head()
# print(head_rows)
tail_rows=c.tail(2)
print(tail_rows)
print(c.values)
print(c.T)
print(c[:2])

pd.read_csv("")

#가져올 자료 중 스킵할 거는 skiprows[0,1]이런식으로 

c.to_csv('')

#loc --> 특정 라벨 가져올 때 사용 
selected_1=c.loc[1]
print(selected_1)

#iloc 
# iloc은 판다스에서 정수 기반의 인덱스를 사용하여 특정 행이나 열을 선택

import pandas as pd

data = {'name': ['kim', 'lee', 'park'],
        'age': [17, 19, 18],
        'grade': ['A', 'C', 'B']}

c = pd.DataFrame(data, index=[1, 2, 3])

# # # iloc을 사용하여 첫 번째 행 선택
first_row = c.iloc[0]
print("First Row using iloc:\n", first_row)




selected_2=c.loc[1]['name']
print(selected_2)

# isin은 특정 조건에 맞는 행을 쉽게 선택할 수 있게 해줌
# # 데이터프레임을 필터링하거나 특정 조건을 만족하는 데이터를 추출하는 데 유용합니다.

print(c['name'].isin(['kim','lee']))


df = pd.DataFrame(np.arange(10, 22).reshape(3, 4),
                  index=["a", "b", "c"],
                  columns=["A", "B", "C", "D"])

# print(df)

# # np.arange(10, 22).reshape(3, 4)는
# # 넘파이 배열을 생성하고 모양을 변경하는 코드입니다. 
# # 이 코드는 np.arange() 함수로 10부터 21까지의 정수로 이루어진 1차원 배열을 만들고,
# # 그 후에 reshape(3, 4) 메서드를 사용하여 이를 3행 4열의 2차원 배열로 모양을 변경

import pandas as pd
import numpy as np

s = pd.Series(range(10))
s[3] = np.nan
print(s)
print(s.count())


#sum - 합계 
#sum(axis=0)---> 열방향 , 인자 생략 가능 , sum(axis=1) ---> 행방향


import pandas as pd

# # 예제 데이터프레임 생성
data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}

df = pd.DataFrame(data)

# # 각 열에 제곱을 계산하는 함수 정의
def square(x):
    return x ** 2

# # 각 열에 함수 적용
result = df.apply(square)
print("Result applying square function to each column:\n", result)


# # 각 행에 합계를 계산하는 함수 정의
def row_sum(row):
    return row.sum()

# # 각 행에 함수 적용
row_sums = df.apply(row_sum, axis=1)
print("\nResult applying row_sum function to each row:\n", row_sums)


# # 예제 시리즈 생성
series = pd.Series([1, 2, 3, 4, 5])

# # 시리즈의 각 원소에 제곱근을 계산하는 함수 정의
def sqrt(x):
    return x ** 0.5

# # 시리즈에 함수 적용
result_series = series.apply(sqrt)
print("\nResult applying sqrt function to each element in the series:\n", result_series)

