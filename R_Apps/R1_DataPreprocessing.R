# UDEMY

####################  DATA PROPROCESSING #####################

#A-  importing library
# ihtiyac duyulan library burdan indirilebilir.

# importing the dataset
# R da index degeri 1,2,3 seklinde BIRden baslar.
dataset= read.csv('Data.csv')

#B- MISSING DATA

# yas verisindekini manipule ettik.
# ayni seyi Salary icin de yapmaliyiz.

dataset$Age = ifelse (is.na(dataset$Age),
                      ave(dataset$Age, FUN = function(x) mean (x, na.rm = TRUE)),
                      dataset$Age)

dataset$Salary = ifelse (is.na(dataset$Salary),
                      ave(dataset$Salary, FUN = function(x) mean (x, na.rm = TRUE)),
                      dataset$Salary)

# C- Encoding Categorical/non-numeric Data

# ulke verilerini ceviriyoruz
dataset$Country = factor(dataset$Country,
                         levels = c('France', 'Spain', 'Germany'),
                         labels= c (1,2,3))

# Dependent value/class verilerini donusturelim
dataset$Purchased = factor(dataset$Purchased,
                         levels = c('No', 'Yes'),
                         labels= c (0,1))

## Boylece verileri sayisal ifadelere cevirdik.
#Bundan Sonra onlar uzerinde islem yapmak oldukca basitlesiyor.

# D SPLITTING THE DATA INTO THE TRAINNING SET AND TEST SET
# Manual veya install.packages ('caTools') yuklenir.
# prograamda kullanmak icin lib ile onu cagirmamiz lazim.

library(caTools)
set.seed(1234)
split= sample.split(dataset$Purchased, SplitRatio= 0.8) # Classa gore veri secilir, trainning orani 80% verdik
training_set= subset(dataset, split== TRUE)
test_set= subset(dataset, split== FALSE)

# E   FEATURE SCALLING
# burada kategorik olan ulke ve class sinifina dokunmuyoruz.
# scalling icin sadece Age ve Salary columns dikkate alinir
training_set [,2:3]= scale(training_set [,2:3])
test_set [,2:3]= scale(test_set [,2:3])






  
  
  
  
  
  
  




