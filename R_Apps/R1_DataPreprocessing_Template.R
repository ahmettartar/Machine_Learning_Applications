# UDEMY

####################  DATA PROPROCESSING #####################

#A-  importing library
# ihtiyac duyulan library burdan indirilebilir.

# importing the dataset
# R da index degeri 1,2,3 seklinde BIRden baslar.

dataset= read.csv('Data.csv')

# dataset = dataset [:, 2:3]

# D SPLITTING THE DATA INTO THE TRAINNING SET AND TEST SET
# Manual veya install.packages ('caTools') yuklenir.
# prograamda kullanmak icin lib ile onu cagirmamiz lazim.

library(caTools)
set.seed(1234)
split= sample.split(dataset$Purchased, SplitRatio= 0.8) # Classa gore veri secilir, trainning orani 80% verdik
training_set= subset(dataset, split== TRUE)
test_set= subset(dataset, split== FALSE)

# # E   FEATURE SCALLING
# # burada kategorik olan ulke ve class sinifina dokunmuyoruz.
# # scalling icin sadece Age ve Salary columns dikkate alinir
# training_set [,2:3]= scale(training_set [,2:3])
# test_set [,2:3]= scale(test_set [,2:3])






  
  
  
  
  
  
  




