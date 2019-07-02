
#                            SUPPORT VECTOR REGRESSION (SVR)

#A                                               Data Preprocessing

dataset= read.csv('Position_Salaries.csv')

dataset = dataset[2:3]


# Splitting NO needed

# Feature Scalling No needed

# Encoding categorical data No needed

# B                                          CREATE YOUR REGRESSION MODEL HERE
library(e1071)
regressor = svm(formula = Salary ~ .,
                data= dataset,
                type = 'eps-regression') # svr: eps-regression SVM: c-classification


## D                                               Predicting Value
# Predicting a new result
 y_pred = predict(regressor, data.frame(Level=6.5))


# C                                             DATA VISUALIZATION
# Visualising Regression model
library(ggplot2) # kullanmak icin lib'den cagiriyoruz.
ggplot()+
  geom_point(aes(x= dataset$Level, y= dataset$Salary),
             colour= 'red')+
  geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)),
            colour= 'blue')+
  ggtitle('Truth or Bluff (Regression)')+
  xlab('Levels')+
  ylab('Salary')


# Visualising the Regression results (FOR HIGHER RESOLUTION AND SMOOTHER CURVE)

library(ggplot2) # kullanmak icin lib'den cagiriyoruz.
X_grid= seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot()+
  geom_point(aes(x= dataset$Level, y= dataset$Salary),
             colour= 'red')+
  geom_line(aes(x = X_grid, y = predict(regressor, newdata = data.frame (Level = X_grid))),
            colour= 'blue')+
  ggtitle('Truth or Bluff (Regression)')+
  xlab('Levels')+
  ylab('Salary')


###     END    ###
  
  
  
  




