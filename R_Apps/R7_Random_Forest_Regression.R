
#                            RANDOM FOREST REGRESSION

#A                                 Data Preprocessing

dataset= read.csv('Position_Salaries.csv')

dataset = dataset[2:3]


# Splitting NO needed

# Feature Scalling No needed

# Encoding categorical data No needed

# B                          CREATE YOUR RANDOM FOREST REGRESSION MODEL HERE
library(randomForest)
regressor = randomForest(x= dataset [1], # matrix or dataframe
                         y= dataset$Salary,# vector
                         ntree= 100) # 10, 100, 300


## D                                 Predicting Value
# Predicting a new result
 y_pred = predict(regressor, data.frame(Level=6.5))


# C                                 DATA VISUALIZATION

# Visualising the RANDOM FOREST REGRESSION results (FOR HIGHER RESOLUTION AND SMOOTHER CURVE)

library(ggplot2) # kullanmak icin lib'den cagiriyoruz.
X_grid= seq(min(dataset$Level), max(dataset$Level), 0.01)
ggplot()+
  geom_point(aes(x= dataset$Level, y= dataset$Salary),
             colour= 'red')+
  geom_line(aes(x = X_grid, y = predict(regressor, newdata = data.frame (Level = X_grid))),
            colour= 'blue')+
  ggtitle('Truth or Bluff (RANDOM FOREST REGRESSION)')+
  xlab('Levels')+
  ylab('Salary')


###     END    ###

# rm(list = ls()) Onceki Verileri silme. // Cleanup the previous variables
  
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
