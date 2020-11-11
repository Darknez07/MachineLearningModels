# Importing the dataset
dataset<-read.csv('Mall_Customers.csv')
x<-dataset[4:5]

#Using K-Means
set.seed(6)
# Faster way for optimal k value
wcss<-vector()
for (k in 1:10) {
  wcss[k]<-sum(kmeans(x, k)$withinss)
}

plot(1:10, wcss,type = 'b', main = paste("Clusters of client"),
     xlab = "Clusters", ylab = "WCSS")

# Getting right amount of clusters
set.seed(29)
clusters <- kmeans(x, 5,  iter.max = 300, nstart = 10)

#Visualizing clusters
library(cluster)
clusplot(x,
         clusters$cluster,
         lines =0,
         shade = TRUE,
         color = TRUE,
         labels = 2,
         span = TRUE,
         main = paste("Clusters"),
         xlab = "Annual Income",
         ylab = "Spending score")