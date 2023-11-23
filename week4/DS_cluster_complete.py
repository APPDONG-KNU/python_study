import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

data=pd.read_excel('과제/DS_cluster_data.xlsx')  

income_data=data['Annual Income (k$)']
spending_score_data=data['Spending Score (1-100)']

using_data=pd.concat([income_data,spending_score_data],axis=1)
using_data.columns=['Annual Income (k$)' , 'Spending Score (1-100)']
print(using_data)

# features = data[['Annual Income (k$)', 'Spending Score (1-100)']]

# print(features)

linkage_data=linkage(using_data,method='complete')

dendrogram(linkage_data, labels=data.index+1)
plt.title('complete cluster')
plt.xlabel('Customer ID')
plt.ylabel('Distance')
plt.savefig('complete cluster_+1_3.png')
plt.show()

from sklearn.cluster import AgglomerativeClustering

num_clusters = 4
# AgglomerativeClustering 모델 생성
model = AgglomerativeClustering(n_clusters=num_clusters)

data['Cluster'] = model.fit_predict(using_data)

# 'Gender' 열을 숫자로 변환 (Male을 0, Female을 1로 매핑)
data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})

cluster_stats = data.groupby('Cluster').mean()

#시각화(맷플롯립 매개변수 c - color (할당된 cluster에 색 지정) , s- 사이즈를 50으로 지정)
plt.scatter(data['Annual Income (k$)'], data['Spending Score (1-100)'],
             c=data['Cluster'], cmap='viridis', s=50)
plt.title('Customer Segmentation')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.savefig('cluster n_2_complete')
plt.show()

print(cluster_stats)
