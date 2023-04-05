install.packages('readr')
install.packages('ggplot2')
install.packages('mlbench')
install.packages('corrplot')
install.packages('Amelia')
install.packages('caret')
install.package('plotly')
install.packages('caTools')
install.packages('reshape2')
install.packages('dplyr')

library(readr)
library(ggplot2)#for visualisation
library(corrplot)#for visualisation of correlation
library(mlbench) 
library(Amelia)
library(plotly)#converting ggplot to plotly
library(reshape2)
library(caret)
library(caTools)#for splittind data into testing and training data
library(dplyr) #manipulating dataframe
library(mlbench)

#check if mlbench is installed
system.file(package='mlbench')

#check if Amelia is installed
system.file(package='Amelia')


data("BostonHousing")


housing <- BostonHousing

#Preparing the data
#Checking for NA and missing values and removing them.
numberOfNA <- length(which(is.na(housing)==T))
numberOfNA
if(numberOfNA>0) {
  housing <- housing[complete.cases(housing),]
}

#Check for any NA’s in the dataframe.
missmap(housing,col=c('yellow','black'),y.at=1,y.labels='',legend=TRUE)
#The above plot clearly shows that the data is free from NA’s.

str(housing) #gives the structure of data

#Here we can see that the variables ‘chas’ is non numeric

#Let’s convert ‘chas’ to numeric
housing$chas <- as.numeric(housing$chas)
str(housing$chas)



#CRIM: per capita crime rate by town
#ZN: proportion of residential land zoned for lots over 25,000 sq.ft.
#INDUS: proportion of non-retail business acres per town
#CHAS: Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
#NOX: nitric oxides concentration (parts per 10 million)
#RM: average number of rooms per dwelling
#AGE: proportion of owner-occupied units built prior to 1940
#DIS: weighted distances to five Boston employment centers
#RAD: index of accessibility to radial highways
#TAX: full-value property-tax rate per $10,000
#PTRATIO: pupil-teacher ratio by town
# B = 1000(Bk – 0.63)2 where Bk is the proportion of Blacks/African Americans per town according to the census.
#LSTAT: % lower status of the population
#MEDV: Median value of owner-occupied homes in $1000s




head(housing)#returns the first six rows of data 
head(housing,9)

dim(housing)

summary(housing)  #gives the basic statistics of your dataset like mean, median, 1st quartile, 2nd quartile etc.
#In the above image we can see that variable ‘crim’ and ‘b’ take wide range of values.

#Variables ‘crim’, ‘zn’, ‘rm’ and ‘black’ have a large difference between their median and mean which indicates lot of outliers in respective variables.

par(mfrow = c(1, 4))
boxplot(housing$crim, main='crim',col='Sky Blue')
boxplot(housing$zn, main='zn',col='Sky Blue')
boxplot(housing$rm, main='rm',col='Sky Blue')
boxplot(housing$black, main='b',col='Sky Blue')

#As suggested earlier variables ‘crim’, ‘zn’, ‘rm’ and ‘black’ do have a lot of outliers.


pairs(housing[,1:13])
# Looking at the plots, we can see that:
# Some of the correlated attributes like ‘nox and age’, ‘nox and dis’ do show predictable curved relationships.


#Finding correlation
#Correlation is a statistical measure that suggests the level of linear dependence between two variables that occur in pair. Its value lies between -1 to +1

#If above 0 it means positive correlation i.e. X is directly proportional to Y.
#If below 0 it means negative correlation i.e. X is inversly proportional to Y.
#Value 0 suggests weak relation.
#Usually we would use the function ‘cor’ to find correlation between two variables, but since we have 14 variables here, it is easier to examine the correlation between different varables using corrplot function in library ‘corrplot’.

#Correlation plots are a great way of exploring data and seeing the level of interaction between the variables.
library(corrplot)

corrplot(cor(housing))

#Looking at the plots, we can see that (except for the diagnal):
#Attributes like ‘tax and rad’, ‘nox and tax’, ‘age and indus’ have positive correlation. Larger darker blue dots suggest storng positive relationship.
#Attributes like ‘dis and nox’, ‘dis and indus’, ‘age and dis’ have negative correlation. Larger darker red dots suggest storng negative relationship.

#Let’s split the loaded dataset into train and test sets. We will use 80% of the data to train our models and 20% will be used to test the models..

set.seed(101)
split <- sample.split(housing,SplitRatio =0.75)
train <- subset(housing,split==TRUE)
test <- subset(housing,split==FALSE)

dim(housing)
dim(train)

dim(test)

summary(train)

model <- lm(medv ~ lstat , data = train) # fit a simple linear regression model
summary(model)


#Multiple Linear Regression
#Lets build our model considering that crim,rm,tax,lstat as the major influencers on the target variable.
model2 <- lm(medv ~ crim + rm + tax + lstat , data = train)
summary(model2)
model2



test$predicted.medv <- predict(model,test)

error <- test$medv-test$predicted.medv
rmse <- sqrt(mean(error)^2)
rmse




test$predicted2.medv <- predict(model2,test)

error2 <- test$medv-test$predicted2.medv
rmse2 <- sqrt(mean(error2)^2)
rmse2


# Remove Highly Correlated Variables and build models
# Highly correlated variables
correlated <- cor(housing[,1:13])
highCorr <- findCorrelation(correlated, cutoff=0.70)

# Identify variables that are highly correlated
names(train[highCorr])
# Create new dataset w/o highly correlated variables
corr_data <- train[,-highCorr]

model3 <- lm(medv ~ . , data = corr_data) # fit a simple linear regression model
summary(model3)
test$predicted3.medv <- predict(model3,test)

error3 <- test$medv-test$predicted3.medv
rmse3 <- sqrt(mean(error3)^2)
rmse3



#Creating GLMNET  regression

#converting dataframe into matrix
library(glmnet)
x <- data.matrix(train[,1:13])
y <- train$medv


control <- trainControl(method = "cv",
                        number = 5)

lineer <- train(medv~.,
                data = train,
                method = "lm",
                trControl = control )

# summary(lineer)


#Ridge regression - glmnet parameter alpha=0 for ridge regression


ridge <- train(medv~.,
               data = train,
               method = "glmnet",
               tuneGrid = expand.grid(alpha = 0,
                                      lambda = seq(0.0001,1,length=50)),
               trControl = control )


# Lasso Regression

lasso <- train(medv~.,
               data = train,
               method = "glmnet",
               tuneGrid = expand.grid(alpha = 1,
                                      lambda = seq(0.0001,1,length=50)),
               trControl = control )



# Test RMSE
p <- predict(lineer,test)
lineer_t <- rmse(test$medv,p)



# Ridge Regression
# Train RMSE
p <- predict(ridge,train)
ridge_e <- rmse(train$medv,p)
# Test RMSE
p <- predict(ridge,test)
ridge_t<- rmse(test$medv,p)



# Lasso Regression
# Train RMSE
p <- predict(lasso,train)
lasso_e <- rmse(train$medv,p)
# Test RMSE
p <- predict(lasso,test)
lasso_t<- rmse(test$medv,p)



model_liste <- list(LM = lineer,
                    Ridge = ridge, Lasso = lasso)
                    

resamp <- resamples(model_liste)
summary(resamp)
