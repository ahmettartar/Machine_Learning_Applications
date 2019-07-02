
#                                        ASSOCIATION RULE LEARNING
                                            
#                                                APRIORI

# A                                 DATA PREPROCESSING
# Importing the dataset
#install.packages('arules')
library(arules)

dataset <- read.csv('Market_Basket_Optimisation.csv', header = FALSE) # Baslik bulunmuyor 

# Sparse Matrix will be created
dataset = read.transactions('Market_Basket_Optimisation.csv', sep = ',', rm.duplicates = TRUE)
summary(dataset)

# Top items graphs
itemFrequencyPlot(dataset, topN= 10) # ilk 100 veya 10 encok satilan




# B              Training Apriori on the dataset

rules = apriori(data = dataset, parameter = list(support = 0.003, confidence = 0.2)) # support 3*7/7500   281 rules
#rules = apriori(data = dataset, parameter = list(support = 0.003, confidence = 0.8)) # support 3*7/7500, confidence=0.8 then 0 rules



# C                Visualising the results
inspect(sort(rules, by = 'lift')[1:10])


## end

