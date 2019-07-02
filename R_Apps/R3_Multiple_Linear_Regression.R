
#                            MULTIPLE LINEAR REGRESSION

#A       Read te data and importing library

dataset= read.csv('50_Startups.csv')

#B Encoding categorical data

dataset$State = factor(dataset$State,
                       levels = c('New York', 'California', 'Florida'),
                       labels= c(1,2,3))

# c      SPLITTING THE DATA INTO THE TRAINNING SET AND TEST SET

library(caTools)
set.seed(1234)
split= sample.split(dataset$Profit, SplitRatio= 0.8) # Classa gore veri secilir, trainning orani 80% verdik
training_set= subset(dataset, split== TRUE)
test_set= subset(dataset, split== FALSE)

# # E   FEATURE SCALLING
# # burada kategorik olan ulke ve class sinifina dokunmuyoruz.
# # scalling icin sadece Age ve Salary columns dikkate alinir
# training_set [,2:3]= scale(training_set [,2:3])
# test_set [,2:3]= scale(test_set [,2:3])


# D     Fitting Simple Linear Regression to the Training set

regressor = lm (formula = Profit ~ ., # Tum degiskenler yerine .nokta kullandik
               data = training_set) # lm: linear model= Simple linear model
#regressor = lm (formula = Profit ~ R.D.Spend + Admisnistration + Marketing.Spend + Sate, # veya hepsini yazmak gerekir

# summary(regressor) Bilgi Dokumu almak icin.



# E     Predicting the Test set results

y_pred= predict(regressor, newdata = test_set)


# F Building the optimal model using Backward Elimination

regressor = lm (formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
                data = dataset) # Tum veri setine uyguluyoruz
summary(regressor)

# En yuksek p degeri olan, istatistik olarak onemsiz olandir. State2 ve State3 yani State kaldiralim.
# Bu sekilde hep devam edip 0.05 seviyesinin altina dusunceye kadar devam edilir.

regressor = lm (formula = Profit ~ R.D.Spend + Administration + Marketing.Spend,
                data = dataset) # Tum veri setine uyguluyoruz
summary(regressor)

# Administration kaldirildi
regressor = lm (formula = Profit ~ R.D.Spend + Marketing.Spend,
                data = dataset) # Tum veri setine uyguluyoruz
summary(regressor)

# Marketing.Spend kaldirildi. Bu sekilde 0.05 degerinden kucuk olanlari (statistically valueable) bulmus olduk.
regressor = lm (formula = Profit ~ R.D.Spend,
                data = dataset) # Tum veri setine uyguluyoruz
summary(regressor)



#### An automatic implementation of Backward Elimination in R

# backwardElimination <- function(x, sl) {
#   numVars = length(x)
#   for (i in c(1:numVars)){
#     regressor = lm(formula = Profit ~ ., data = x)
#     maxVar = max(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"])
#     if (maxVar > sl){
#       j = which(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"] == maxVar)
#       x = x[, -j]
#     }
#     numVars = numVars - 1
#   }
#   return(summary(regressor))
# }
# 
# SL = 0.05
# dataset = dataset[, c(1,2,3,4,5)]
# backwardElimination(training_set, SL)


###     END    ###
  
  
  
  




