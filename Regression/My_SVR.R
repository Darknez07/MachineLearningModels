# Polynomial Regression
# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]


# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(e1071)
# Build your own Regression Model
# Create a Regressor here
SVR = svm(formula = Salary~.,
          data = dataset,
          type = 'eps-regression')

# Prediction by your Regressor
y_poly_pred = predict(SVR, data.frame(Level = 6.5))




library(ggplot2)
# Plot your own Regressor Here
ggplot(dataset,aes(x=Level,y=Salary))+
  geom_point()+
  geom_line(aes(x=Level,y=predict(SVR,newdata = dataset)),colour='red')+
  ggtitle('Support Vector Regressor')+
  xlab('Level')+
  ylab('Salary')
