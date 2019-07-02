
###                                             DEEP LEARNING

##                                      ARTIFICIAL NEURAL NETWORK (ANN)


## PART 1

# Importing the dataset
dataset = read.csv('Churn_Modelling.csv')
dataset = dataset[4:14]

# Encoding the categorical variables as factors
dataset$Geography = as.numeric(factor(dataset$Geography,
                                      levels = c('France', 'Spain', 'Germany'),
                                      labels = c(1, 2, 3)))
dataset$Gender = as.numeric(factor(dataset$Gender,
                                   levels = c('Female', 'Male'),
                                   labels = c(1, 2)))

## PART 2

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Exited, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
training_set[-11] = scale(training_set[-11]) # class haric
test_set[-11] = scale(test_set[-11])


## PART 3

# Fitting ANN to the Training set
# install.packages('h2o')
library(h2o)
h2o.init(nthreads = -1) #server
classifier = h2o.deeplearning(y = 'Exited',
                         training_frame = as.h2o(training_set),
                         activation = 'Rectifier',
                         hidden = c(5,5), # c(6,6)
                         epochs = 100,
                         train_samples_per_iteration = -2) # parameter tuning 0 -1 -2(default)


## PART 4


# Predicting the Test set results
y_pred = h2o.predict(classifier, newdata = as.h2o(test_set[-11]))
y_pred = (y_pred > 0.5) # 0 ve 1 yapiyor.
y_pred = as.vector(y_pred) # 1x2000 sutun vektor

# Making the Confusion Matrix
cm = table(test_set[, 11], y_pred)

# h2o.shutdown() Disconnect yapmak gerekiyor.

### end