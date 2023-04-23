import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import mplcursors

# Load the data from a CSV file and exclude specific columns
data = pd.read_csv('shooting_stats_cleaned.csv', usecols=['Player', 'G', 'MP', 'FG%', 'Dist.', '%2PA', '0-3A', '3-10A', '10-16A', '16-3PA', '%3PA', '%2PM', '0-3M', '3-10M', '10-16M', '16-3PM', '%3PM', '%2PAst\'d', '%3PAst\'d', '%DunksA', 'DunkM', '%C3A', 'C3%'])

# Normalize specific columns using StandardScaler
scaler = StandardScaler()
data[['G', 'MP', 'Dist.', 'DunkM']] = scaler.fit_transform(data[['G', 'MP', 'Dist.', 'DunkM']])

# Apply KMeans clustering to the data
kmeans = KMeans(n_clusters=7)
labels = kmeans.fit_predict(data.drop('Player', axis=1))

# Calculate the silhouette score
silhouette_avg = silhouette_score(data.drop('Player', axis=1), labels)
print('Silhouette Score:', silhouette_avg)

# Calculate the sum of squared distances
ssd = kmeans.inertia_
print('Sum of Squared Distance:', ssd)

# Apply PCA to reduce the dimensions of the data to 2 dimensions
pca = PCA(n_components=3)
data_reduced = pca.fit_transform(data.drop('Player', axis=1))

# Plot the data points with their cluster labels
fig, ax = plt.subplots()
scatter = ax.scatter(data_reduced[:, 0], data_reduced[:, 1], data_reduced[:, 2], c=labels)

# Add annotations to the scatter plot using mplcursors
mplcursors.cursor(hover=True).connect(
    "add", lambda sel: sel.annotation.set_text(data.loc[sel.target.index]['Player']))

plt.title('Clustering Results')
plt.xlabel('PC1')
plt.ylabel('PC2')

plt.show()
