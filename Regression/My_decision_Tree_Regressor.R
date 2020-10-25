#Decision Tree Regression
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]


# Splitting the dataset into the Training set and Test set
# install.packages('caTools')

# We need rpart Libarary
# Build your own Regression Model
# Create a Regressor here

regressor = rpart(formula = Salary~.,
                  data = dataset,
                  control = rpart.control(minsplit = 1))

# Prediction by your Regressor
y_poly_pred = predict(regressor, data.frame(Level = 6.5))




library(ggplot2)
X_grid = seq(min(dataset$Level),max(dataset$Level),0.008)
# Plot your own Regressor Here
ggplot()+
  geom_point(aes(x= dataset$Level, y=dataset$Salary))+
  geom_line(aes(x= X_grid,y=predict(regressor,newdata = data.frame(Level = X_grid))),
            colour='red')+
  ggtitle('Decision Tree Regressor')+
  xlab('Level')+
  ylab('Salary')
