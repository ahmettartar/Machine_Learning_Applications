
#                            DECISION TREE REGRESSION

#A                                 Data Preprocessing

dataset= read.csv('Position_Salaries.csv')

dataset = dataset[2:3]


# Splitting NO needed

# Feature Scalling No needed

# Encoding categorical data No needed

# B                          CREATE YOUR DECISION TREE REGRESSION MODEL HERE
library(rpart)
regressor = rpart(formula = Salary ~ .,
                data= dataset,
                control = rpart.control(minsplit = 1)) # linearlik problemini giderdik, grafikteki.


## D                                 Predicting Value
# Predicting a new result
 y_pred = predict(regressor, data.frame(Level=6.5))


# C                                 DATA VISUALIZATION

# Visualising the Decision Tree Regression results (FOR HIGHER RESOLUTION AND SMOOTHER CURVE)

library(ggplot2) # kullanmak icin lib'den cagiriyoruz.
X_grid= seq(min(dataset$Level), max(dataset$Level), 0.01)
ggplot()+
  geom_point(aes(x= dataset$Level, y= dataset$Salary),
             colour= 'red')+
  geom_line(aes(x = X_grid, y = predict(regressor, newdata = data.frame (Level = X_grid))),
            colour= 'blue')+
  ggtitle('Truth or Bluff (Decision Tree Regression)')+
  xlab('Levels')+
  ylab('Salary')


###     END    ###
  
# # Visualising Regression model
# library(ggplot2) # kullanmak icin lib'den cagiriyoruz.
# ggplot()+
#   geom_point(aes(x= dataset$Level, y= dataset$Salary),
#              colour= 'red')+
#   geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)),
#             colour= 'blue')+
#   ggtitle('Truth or Bluff (Decision Tree Regression)')+
#   xlab('Levels')+
#   ylab('Salary')
