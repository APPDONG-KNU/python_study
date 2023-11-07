import pandas as pd
import numpy as np

# 가상의 타이타닉 데이터 생성
data = {
    'PassengerId': np.arange(1, 11),
    'Survived': np.random.choice([0, 1], size=10),
    'Pclass': np.random.choice([1, 2, 3], size=10),
    'Name': ['John', 'Jane', 'Bob', 'Alice', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry'],
    'Gender': np.random.choice(['male', 'female'], size=10),
    'Age': np.random.randint(18, 60, size=10),
    'Fare': np.random.uniform(20, 200, size=10)
}

# 데이터프레임 생성
titanic = pd.DataFrame(data)

# 처음 5개의 행 출력
print(titanic.head())

# 생존자 수 계산
survived_count = titanic['Survived'].sum()
print("\nNumber of Survivors:", survived_count)

# 성별에 따른 생존자 수 계산
survived_by_gender = titanic.groupby('Sex')['Survived'].sum()
print("\nSurvivors by Gender:\n", survived_by_gender)

# 나이가 30세 미만인 승객 선택
young_passengers = titanic[titanic['Age'] < 30]
print("\nPassengers Younger than 30:\n", young_passengers.head())

# 1등급 객실에 탑승한 승객 선택
first_class_passengers = titanic[titanic['Pclass'] == 1]
print("\nFirst Class Passengers:\n", first_class_passengers.head())

