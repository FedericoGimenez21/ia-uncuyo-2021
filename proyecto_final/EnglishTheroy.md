# MARCO TEÓRICO 

## Linear Regression

Simple linear regression lives up to its name: it is a very straightforward approach for predicting a quantitative response Y on the basis of a single predictor variable X. It assumes that there is approximately a linear
relationship between X and Y .
Linear regression analysis is used to predict the value of a variable based on the value of another variable.
The variable you want to predict is called the dependent variable. The variable you are using to predict the other variable's value is called the independent variable.

This form of analysis estimates the coefficients of the linear equation, involving one or more independent variables that best predict the value of the dependent variable.
Linear regression fits a straight line or surface that minimizes the discrepancies between predicted and actual output values. There are simple linear regression calculators that use a “least squares” method to discover the best-fit line for a set of paired data. You then estimate the value of X (dependent variable) from Y (independent variable).

You can perform the linear regression method in a variety of programs and environments, including:

- R linear regression
- MATLAB linear regression
- Linear regression Python
- Excel linear regression

## Why linear regression is important?
Linear-regression models are relatively simple and provide an easy-to-interpret mathematical formula that can generate predictions. 
Linear regression can be applied to various areas in business and academic study.
You’ll find that linear regression is used in everything from biological, behavioral, environmental and social sciences to business. 
Linear-regression models have become a proven way to scientifically and reliably predict the future. Because linear regression is a long-established statistical procedure, the properties of linear-regression models are well understood and can be trained very quickly.


Mathematically, we can write this linear
relationship as
![image](https://user-images.githubusercontent.com/88351465/228034735-21d214a8-09cf-4943-83ee-02c1da9d981f.png)

You might read “≈” as “is approximately modeled as”

Together, β0 and β1 are known as the model coefficients or parameters. Once we have used our
training data to produce estimates βˆ0 and βˆ1 for the model coefficients, we
can predict future sales on the basis of a particular value of TV advertising
by computing
![image](https://user-images.githubusercontent.com/88351465/228034991-73ce2857-6dba-4857-8ce9-b52a4192730f.png)
where ˆy indicates a prediction of Y on the basis of X = x. Here we use a
hat symbol, ˆ , to denote the estimated value for an unknown parameter
or coefficient, or to denote the predicted value of the response.



Not every problem can be solved with the same algorithm. In this case, linear regression assumes that there exists a linear relationship between the response variable and the explanatory variables. 
This means that you can fit a line between the two (or more variables).

![image](https://user-images.githubusercontent.com/88351465/228036888-d6d48b36-231b-4eec-936c-6b7f7aa19b2e.png)


The above graph presents the linear relationship between the output(y) variable and predictor(X) variables.  The blue line is referred to as the best fit straight line. Based on the given data points, we attempt to plot a line that fits the points the best.

To calculate best-fit line linear regression uses a traditional slope-intercept form which is given below,

Yi = β0 + β1Xi 

where Yi = Dependent variable,  β0 = Intercept, β1 = Slope, Xi = Independent variable.

This algorithm explains the linear relationship between the dependent(output) variable y and the independent(predictor) variable X using a straight line  Y= B0 + B1 X.
![image](https://user-images.githubusercontent.com/88351465/228037271-1e463a58-8ad9-4785-872c-aefc25aa6ba9.png)


## But how the linear regression finds out which is the best fit line?

The goal of the linear regression algorithm is to get the best values for B0 and B1 to find the best fit line. The best fit line is a line that has the least error which means the error between predicted values and actual values should be minimum.



## Residuals
A good way to test the quality of the fit of the model is to look at the residuals or the differences between the real values and the predicted values.
The straight line in the image above represents the predicted values. The red vertical line from the straight line to the observed data value is the residual.

![image](https://user-images.githubusercontent.com/88351465/228037812-0ae63623-167c-4003-80e1-94a6f45f1d70.png)
The idea here is that the sum of the residuals is approximately zero or as low as possible. In real life, most cases will not follow a perfectly straight line, so residuals are expected. 

## What is the best fit line?
In simple terms, the best fit line is a line that fits the given scatter plot in the best way. Mathematically, the best fit line is obtained by minimizing the Residual Sum of Squares(RSS).

The quality of a linear regression fit is typically assessed
using two related quantities: the residual standard error (RSE) and the R2 statistic.
RSE: Roughly speaking, it is the average amount that the response will deviate from the true regression line. It is computed using the formula: 
![image](https://user-images.githubusercontent.com/88351465/228039774-549a2d0a-f6af-4179-bbe9-633ee7abb680.png)
Note that RSS was:
![image](https://user-images.githubusercontent.com/88351465/228039870-d0b43267-aede-4610-8dca-a36912d4ddd4.png)

The RSE is considered a measure of the lack of fit of the model to
the data. If the predictions obtained using the model are very close to the
true outcome values—that is, if ˆyi ≈ yi for i = 1,...,n—then RSE will
be small, and we can conclude that the model fits the data very well. On
the other hand, if ˆyi is very far from yi for one or more observations, then
the RSE may be quite large, indicating that the model doesn’t fit the data
well.

## R2 Statistic

The RSE provides an absolute measure of lack of fit of the model 
to the data. But since it is measured in the units of Y , it is not always
clear what constitutes a good RSE. The R2 statistic provides an alternative
measure of fit. It takes the form of a proportion—the proportion of variance explained—and so it always takes on a value between 0 and 1, and is
independent of the scale of Y .

How to Test if your Linear Model has a Good Fit
One measure very used to test how good your model is is the coefficient of determination or R². This measure is defined by the proportion of the total variability explained by the regression model.

![image](https://user-images.githubusercontent.com/88351465/228038223-b0daf65d-020f-48a8-b8f5-5745323ac450.png)

This can seem a little bit complicated, but in general, for models that fit the data well, R² is near 1. Models that poorly fit the data have R² near 0. 


## Root Mean Squared Error 
The Root Mean Squared Error is the square root of the variance of the residuals. It specifies the absolute fit of the model to the data i.e. how close the observed data points are to the predicted values. Mathematically it can be represented as,
![image](https://user-images.githubusercontent.com/88351465/228042735-94668220-b84b-46e0-a3c2-3f915c17430a.png)
The basic idea is to measure how bad/erroneous the model’s predictions are when compared to actual observed values. So a high RMSE is “bad” and a low RMSE is “good”.
In the formula, the difference between the observed and predicted values is called the residual. The mean squared error (MSE) is the average of all the squared residuals. Then the RMSE just takes the square root of that, which puts the metric back in the response variable scale.

R-squared is a better measure than RSME. Because the value of Root Mean Squared Error depends on the units of the variables (i.e. it is not a normalized measure), it can change with the change in the unit of the variables.

