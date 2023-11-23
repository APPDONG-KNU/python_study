import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

data=pd.read_excel('/Users/kangmin/Desktop/Study/python/DS_class/과제/DS_cluster_data.xlsx')

income_data=data['Annual Income (k$)']
spending_score_data=data['Spending Score (1-100)']

using_data=pd.concat([income_data,spending_score_data],axis=1)
using_data.columns=['Annual Income (k$)' , 'Spending Score (1-100)']
print(using_data)

# features = data[['Annual Income (k$)', 'Spending Score (1-100)']]

# print(features)

linkage_data=linkage(using_data,method='single')

dendrogram(linkage_data, labels=data.index)
plt.title('single cluster')
plt.xlabel('Customer ID')
plt.ylabel('Distance')
plt.savefig('single cluster.png')
plt.show()

from sklearn.cluster import AgglomerativeClustering

# 클러스터 수 결정
num_clusters = 4

# AgglomerativeClustering 모델 생성
model = AgglomerativeClustering(n_clusters=num_clusters)

# 모델 학습 및 클러스터 할당
data['Cluster'] = model.fit_predict(using_data)

# 'Gender' 열을 숫자로 변환 (예: Male을 0, Female을 1로 변환)
data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})
# 클러스터별 통계량 확인
cluster_stats = data.groupby('Cluster').mean()

# 클러스터별 특성 시각화
plt.scatter(data['Annual Income (k$)'], data['Spending Score (1-100)'], c=data['Cluster'], cmap='viridis', s=50)
plt.title('Customer Segmentation')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.savefig('cluster n_2_single')
plt.show()


# 클러스터별 통계량 출력
print(cluster_stats)

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 클러스터 수를 증가시키면서 KMeans 모델을 학습하고, 각 클러스터링 결과에 대한 이너셔 값을 저장
inertia_values = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(using_data)
    inertia_values.append(kmeans.inertia_)

# 이너셔 값을 시각화하여 엘보우 메서드를 적용
plt.plot(range(1, 11), inertia_values, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()
