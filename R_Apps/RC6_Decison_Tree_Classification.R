
#                            DECISION TREE CLASSIFICATION

#A                                Data Preprocessing

dataset= read.csv('Social_Network_Ads.csv')

dataset = dataset[,3:5] # 3 4 5 KOLONLAR


# ENCODING THE TARGET FEATURE AS FACTOR
# factor olarak tanimlamamiz lazim. Aksi halde normal veri, naive bayes de calismiyor.

dataset$Purchased = factor(dataset$Purchased, levels = c(0,1))



# B               Splitting the dataset into the Training set and Test set
library(caTools)
set.seed(123)
split= sample.split(dataset$Purchased, SplitRatio = 0.75)
training_set = subset(dataset, split== TRUE)
test_set = subset(dataset, split== FALSE)

# Feature Scalling
training_set [, 1:2]= scale(training_set[, 1:2])
test_set [, 1:2]= scale(test_set[, 1:2])


# B             CREATE YOUR  DECISION TREE CLASSIFIER MODEL HERE
library(rpart)
classifier= rpart(formula = Purchased ~ .,
                  data = training_set)

#C                Predicting the Test Set Results

#y_pred = predict(classifier, newdata = test_set[-3])

# 2 boyutlu 0.96 0.04 seklinde veriyor.
# yuksek deger olan taraftaki sinif alinmasi gerekir 0-1
#bunun icin type belirliyoruz.

y_pred = predict(classifier, newdata = test_set[-3], type = 'class')


#D   Making the Confusion Matrix
cm = table(test_set[,3], y_pred) # actual value predicted value



# E                                 DATA VISUALIZATION


# Visualising the Training set results
library(ElemStatLearn)
set = training_set
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('Age', 'EstimatedSalary')
y_grid = predict(classifier, newdata = grid_set, type = 'class')
plot(set[, -3],
     main = 'DECISION TREE CLASSIFICATION (Training set)',
     xlab = 'Age', ylab = 'Estimated Salary',
     xlim = range(X1), ylim = range(X2))

contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))


# Visualising the Test set results

library(ElemStatLearn)
set = test_set
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('Age', 'EstimatedSalary')
y_grid = predict(classifier, newdata = grid_set, type = 'class')
plot(set[, -3],
     main = 'DECISION TREE CLASSIFICATION (Test set)',
     xlab = 'Age', ylab = 'Estimated Salary',
     xlim = range(X1), ylim = range(X2))

contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))

###     END    ###

# rm(list = ls()) Onceki Verileri silme. // Cleanup the previous variables
# Ctrl+l console temizler.



################ DECISION TREE VISUALIZATION #####################################
# Feature scaling yapmiyoruz.

#A                                Data Preprocessing

dataset= read.csv('Social_Network_Ads.csv')
dataset = dataset[,3:5] # 3 4 5 KOLONLAR

# ENCODING THE TARGET FEATURE AS FACTOR

dataset$Purchased = factor(dataset$Purchased, levels = c(0,1))

# B               Splitting the dataset into the Training set and Test set
library(caTools)
set.seed(123)
split= sample.split(dataset$Purchased, SplitRatio = 0.75)
training_set = subset(dataset, split== TRUE)
test_set = subset(dataset, split== FALSE)

# B             CREATE YOUR  DECISION TREE CLASSIFIER MODEL HERE
library(rpart)
classifier= rpart(formula = Purchased ~ .,
                  data = training_set)

# Plotting Decision Tree Visulisation
plot(classifier)
text(classifier)

## END


