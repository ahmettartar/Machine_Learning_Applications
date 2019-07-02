
#                            REGRESSION TEMPLATE

#A                                               Data Preprocessing

dataset= read.csv('Position_Salaries.csv')

dataset = dataset[2:3]


# Splitting NO needed

# Feature Scalling No needed

# Encoding categorical data No needed

# library(caTools)
# set.seed(1234)
# split= sample.split(dataset$Profit, SplitRatio= 0.8) # Classa gore veri secilir, trainning orani 80% verdik
# training_set= subset(dataset, split== TRUE)
# test_set= subset(dataset, split== FALSE)

# #    FEATURE SCALLING
# # burada kategorik olan ulke ve class sinifina dokunmuyoruz.
# # scalling icin sadece Age ve Salary columns dikkate alinir
# training_set [,2:3]= scale(training_set [,2:3])
# test_set [,2:3]= scale(test_set [,2:3])


# B                                          CREATE YOUR REGRESSION MODEL HERE
# #Fitting Linear Regression to the dataset
# lin_reg= lm (formula = Salary ~ .,
#              data = dataset) # splitting olmadigindan tum dataset yoksa training_set olacakti. 
# 
# summary(lin_reg)
# 
# 
# #       Fitting Polynomial Regression to the dataset
# dataset$Level2= dataset$Level^2 #Xkare degeri
# dataset$Level3= dataset$Level^3 #Xkup degeri
# dataset$Level4= dataset$Level^4 
# 
# poly_reg= lm (formula = Salary ~ .,
#              data = dataset) # splitting olmadigindan tum dataset yoksa training_set olacakti. 
# 
# summary(poly_reg)


## D                                               Predicting Value
# 
# # Predicting anew result with Linear Regression
# 
# y_pred = predict(lin_reg, data.frame(Level=6.5))
# 
# 
# # Predicting anew result with Linear Regression
# 
# y_pred = predict(poly_reg, data.frame(Level=6.5,
#                                       Level2=6.5^2,
#                                       Level3=6.5^3,
#                                       Level4=6.5^4))

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
  
  
  
  




