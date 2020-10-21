# Polynomial Regression
# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]


# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
# Linear Regression Model
Simple = lm(formula = Salary~., 
            data = dataset)

#Build a polynomial Regression Model
# Polynomial Regressor need levels
# Add columns 3 Level or power 3
dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4
Poly = lm(formula = Salary~ .,
          data = dataset)

library(ggplot2)
ggplot(dataset,aes(x=Level,y=Salary))+
  geom_point()+
    geom_line(aes(x=Level,y=predict(Simple,newdata = dataset)),colour = 'red')+
    ggtitle('Simple Linear Reg')+
    xlab('Level')+
    ylab('Salary')


ggplot(dataset,aes(x=Level,y=Salary))+
  geom_point()+
  geom_line(aes(x=Level,y=predict(Poly,newdata = dataset)),colour='red')+
  ggtitle('Polynomial Regression')+
  xlab('Level')+
  ylab('Salary')

# Prediction by Simple Linear regression
y_pred = predict(Simple, data.frame(Level = 6.5))

# Prediction by Polynomial Regressor
y_poly_pred = predict(Poly, data.frame(Level = 6.5,
                                       Level2 = 6.5^2,
                                       Level3 = 6.5^3,
                                       Level4 = 6.5^4))