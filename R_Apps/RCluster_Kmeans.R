
# K-Means Clustering

# Importing the dataset

dataset <- read.csv('Mall_Customers.csv')
X <- dataset[4:5]

# # Using the elbow method to find the optimal number of clusters

set.seed(6)
wcss = vector()
for (i in 1:10) wcss[i] = sum(kmeans(X, i)$withinss) # withinss karelerinin toplami

plot(1:10, wcss, type = 'b', main = paste('The Elbow Method'), xlab = 'Number of clusters', ylab = 'WCSS')

# Buradan optimum number 5 bulundu.


# Applying k-means to the dataset
set.seed(29)
kmeans= kmeans(X, 5, iter.max = 300, nstart = 10)


# Visualising the clusters

library(cluster)
clusplot(X,
         kmeans$cluster,
         lines = 0, #1 clusterlar arasinda cizgi cizer. 
         shade = T, #T icini cizgili F ise cizgisiz yapar
         color = T, # T coklu renk F tekrenk
         labels = 2, #1 point koyar, 
         plotchar = F,
         span = T, # Ellipsler ortusmez, ayri ayri.
         main = paste('Clusters of customers'),
         xlab = 'Annual Income',
         ylab = 'Spending Score')

## end

