# Group Members : Diego Bobrow, Nicholas Tincani Ueki, Brandon Zhang

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load the data from a CSV file and exclude specific columns
data = pd.read_csv('shooting_stats_cleaned.csv', usecols=['G', 'MP', 'FG%', 'Dist.', '%2PA', '0-3A', '3-10A', '10-16A', '16-3PA', '%3PA', '%2PM', '0-3M', '3-10M', '10-16M', '16-3PM', '%3PM', '%2PAst\'d', '%3PAst\'d', '%DunksA', 'DunkM', '%C3A', 'C3%'])


inertias = []
# Normalize specific columns using StandardScaler
scaler = StandardScaler()
data[['G', 'MP', 'Dist.', 'DunkM']] = scaler.fit_transform(data[['G', 'MP', 'Dist.', 'DunkM']])
K = range(1, 10)
for k in K:
    # Apply KMeans clustering to the data
    kmeans = KMeans(n_clusters=k)
    labels = kmeans.fit_predict(data)

    # Calculate the sum of squared distances
    ssd = kmeans.inertia_
    print('Sum of Squared Distance:', ssd)

    inertias.append(ssd)


plt.figure(figsize=(16,8))
plt.plot(K, inertias, 'bx-')
plt.xlabel('k')
plt.ylabel('Inertia')
plt.title('The Elbow Method showing the optimal k')
plt.show()
