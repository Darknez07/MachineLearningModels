# Please Load the dataset

dataset = read.csv("Mall_Customers.csv")
x = dataset[4:5]

#Using dendogram to find the number of clusters
dendo = hclust(dist(x, method = 'euclidean'), method = 'ward.D')
plot(dendo,
     main = paste("Here lies dendogram"),
     xlab = "Points",
     ylab = "Distance")
abline(h = 800, col = "black", lty = 2, lwd= 3)
text(y = 900, x = 100,"5 Clusters",lwd=4)

# Create optimum clustering model

hc = hclust(dist(x), method = 'ward.D')
y_hc = cutree(hc, 5)

# Visualization of clusters
library(cluster)
clusplot(x,
         y_hc,
         lines =0,
         shade = TRUE,
         color = TRUE,
         labels = 2,
         span = TRUE,
         main = paste("Clusters"),
         xlab = "Annual Income",
         ylab = "Spending score")