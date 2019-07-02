
#                            SIMPLE LINEAR REGRESSION

#A       Read te data and importing library

dataset= read.csv('Salary_Data.csv')


# B      SPLITTING THE DATA INTO THE TRAINNING SET AND TEST SET

library(caTools)
set.seed(1234)
split= sample.split(dataset$Salary, SplitRatio= 2/3) # Classa gore veri secilir, trainning orani 80% verdik
training_set= subset(dataset, split== TRUE)
test_set= subset(dataset, split== FALSE)

# # E   FEATURE SCALLING
# # burada kategorik olan ulke ve class sinifina dokunmuyoruz.
# # scalling icin sadece Age ve Salary columns dikkate alinir
# training_set [,2:3]= scale(training_set [,2:3])
# test_set [,2:3]= scale(test_set [,2:3])


# c      Fitting Simple Linear Regression to the Training set

regressor = lm (formula = Salary ~ YearsExperience,
               data = training_set) # lm: linear model= Simple linear model


# D     Predicting the Test set results

y_pred= predict(regressor, newdata = test_set)


## E    Data Visulization

# Visualising the Training set results

# install.packages ("ggplot2") Visualisation icin paketi indirdik.
library(ggplot2) # kullanmak icin lib'den cagiriyoruz.
ggplot()+
  geom_point(aes(x= training_set$YearsExperience, y= training_set$Salary),
             colour= 'red')+
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            colour= 'blue')+
  ggtitle('Salary vs Experience (Training Set)')+
  xlab('Years of Experience')+
  ylab('Salary')


# Visualising the Test set results

library(ggplot2) # kullanmak icin lib'den cagiriyoruz.
ggplot()+
  geom_point(aes(x= test_set$YearsExperience, y= test_set$Salary),
             colour= 'red')+
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            colour= 'blue')+
  ggtitle('Salary vs Experience (Test Set)')+
  xlab('Years of Experience')+
  ylab('Salary')
  

###     END    ###
  
  
  
  




