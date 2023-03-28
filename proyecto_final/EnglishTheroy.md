# MARCO TEÓRICO 

# Terminos importantes 

Bias:
Biases are the underlying assumptions that are made by data to simplify the target function. Bias does help us generalize the data better and make the model less sensitive to single data points. It also decreases the training time because of the decrease in complexity of target function High bias suggest that there is more assumption taken on target function. This leads to the underfitting of the model sometimes.
Examples of High bias Algorithms include Linear Regression, Logistic Regression etc.

Variance:
In machine learning, Variance is a type of error that occurs due to a model’s sensitivity to small fluctuations in the dataset. The high variance would cause an algorithm to model the outliers/noise in the training set. This is most commonly referred to as overfitting. In this situation, the model basically learns every data point and does not offer good prediction when it tested on a novel dataset.
Examples of High variance Algorithms include Decision Tree, KNN etc.

![image](https://user-images.githubusercontent.com/88351465/228051759-5fa20141-391e-40e2-b644-a6cfe10aad01.png)

![image](https://user-images.githubusercontent.com/88351465/228051810-ceaacd40-0ddf-48b4-af2f-2a2a9695f41e.png)


# Linear Regression

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


# GLMNET (Ridge Regression y Lasso Regression)

## Ridge Regression 

Ridge regression is very similar to least squares, except that the coefficients ridge
regression are estimated by minimizing a slightly different quantity
In particular, the ridge regression coefficient estimates βˆR are the values that minimize
![image](https://user-images.githubusercontent.com/88351465/228047089-f5c18fe4-1cc8-405a-a1f9-85a3928f86e2.png)

where λ ≥ 0 is a tuning parameter, to be determined separately. 
The tuning parameter λ serves to control
the relative impact of these two terms on the regression coefficient estimates. When λ = 0, the penalty term has no effect, and ridge regression
will produce the least squares estimates. However, as λ → ∞, the impact of
the shrinkage penalty grows, and the ridge regression coefficient estimates
will approach zero.
Selecting a good value for λ is critical. One optimal option is to try a bunch of values for λ and use cross-validation, to determine which one results in the lowest variance. 

Why Does Ridge Regression Improve Over Least Squares?
Ridge regression’s advantage over least squares is rooted in the bias-variance
trade-off. As λ increases, the flexibility of the ridge regression fit decreases,
leading to decreased variance but increased bias.


## Lasso Regression 

The lasso is a relatively recent alternative to ridge regression. Formula: 
![image](https://user-images.githubusercontent.com/88351465/228049230-f9f6a8e0-804b-4e0e-88ae-94eae70106b1.png)

we see that the lasso and ridge regression have similar formulations.
The only difference is that the βj^2 term in the ridge
regression penalty has been replaced by |βj| in the lasso penalty
As with ridge regression, the lasso shrinks the coefficient estimates towards zero.

Lasso produces simpler and more interpretable models that involve only a
subset of the predictors.

## Comparative Analysis of Lasso and Ridge Regression
Ridge and Lasso regression uses two different penalty functions for regularisation. Ridge regression uses L2 on the other hand lasso regression go uses L1 regularisation technique. In ridge regression, the penalty is equal to the sum of the squares of the coefficients and in the Lasso, penalty is considered to be the sum of the absolute values of the coefficients. In lasso regression, it is the shrinkage towards zero using an absolute value (L1 penalty or regularization technique) rather than a sum of squares(L2 penalty or regularization technique).


## Selecting the Tuning Parameter

implementing ridge regression and the lasso requires a method for selecting
a value for the tuning parameter λ
Cross-validation provides a simple way to tackle this problem. We choose a grid of λ values, and compute
the cross-validation error for each value of λ. We
then select the tuning parameter value for which the cross-validation error
is smallest. Finally, the model is re-fit using all of the available observations
and the selected value of the tuning parameter. 


![image](https://user-images.githubusercontent.com/88351465/228054986-c136aeca-847d-4815-af62-5af935a41db7.png)


> Left: Ten-fold cross-validation MSE for the lasso, applied to
> the sparse simulated data set. Right: The corresponding lasso
> coefficient estimates are displayed. The two signal variables are shown in color,
> and the noise variables are in gray. The vertical dashed lines indicate the lasso
> fit for which the cross-validation error is smallest


# Boosting 

Boosting is the ensemble learning method where we build multiple weak learners (same  algorithms) in a parallel manner.

 All these weak learners take the previous models’ feedback to improve their power in accurately predicting the miss classified classes. At the end, the algorithm uses all these weak learners to build the final model. 

The final model predictions use the majority voting approach for classification problems. Whereas for regression kind of problem. The final value is the average value of all the week learning models.

Can a strong model be accomplished from many models that are relatively poor and simply also called as weak learners?
In other words, can the multiple weak learners form a strong model to predict the future or test dataset?

By saying "weak models". We're not saying about simple basic models like decision trees.

But models with low-performance accuracy, where low is a bit better than random.

How can we build such models then?
A positive mathematical response to this question took a few years to create a fully-functional, algorithms based solution. 

In short, this algorithm works in a few steps in a greedy approach. 

At first, they construct a linear combination of simple models (basic algorithms) by re-weighting input data. The model (usually the decision tree) assigns larger weights for the incorrectly predicted items.

Going forward, the algorithm amplifies the incorrectly predicted classes and tries to predict them accurately. The loss function intends to minimize the errors for the incorrect classes than the overall dataset.


### What is a Gradient boosting Algorithm?
Gradient Boosting, Gradient Tree Boosting o Gradient Boosted Regression Trees (GBRT), es una familia de algoritmos usados tanto en clasificación como en regresión basados en la combinación de modelos predictivos débiles (weak learners) -normalmente árboles de decisión- para crear un modelo predictivo fuerte. La generación de los árboles de decisión débiles se realiza de forma secuencial, creándose cada árbol de forma que corrija los errores del árbol anterior. Los aprendices suelen ser árboles "poco profundos" (shallow trees), de apenas uno, dos o tres niveles de profundidad, típicamente.

Uno de los parámetros de este tipo de argumentos es el learning rate o tasa de aprendizaje, que controla el grado de mejora de un árbol respecto del anterior. Una tasa de aprendizaje pequeña supone una mejora más lenta pero adaptándose mejor a los datos, lo que se traduce generalmente en mejoras en el resultado a costa de un mayor consumo de recursos.


The main idea behind this algorithm is to build models sequentially and these subsequent models try to reduce the errors of the previous model. But how do we do that? How do we reduce the error? This is done by building a new model on the errors or residuals of the previous model.

When the target column is continuous, we use Gradient Boosting Regressor whereas when it is a classification problem, we use Gradient Boosting Classifier. The only difference between the two is the “Loss function”. The objective here is to minimize this loss function by adding weak learners using gradient descent. Since it is based on loss function hence for regression problems, we’ll have different loss functions like Mean squared error (MSE) and for classification, we will have different for e.g log-likelihood.

## How Gradient Boosting Works


Gradient boosting approach can use for both the regression and classification problems. These teaching techniques generate a prediction model in the form of a series of weak prediction models, usually in the way of decision trees. 

Three components are involved in gradient boosting:

 - An optimized loss function.
 - A lousy indicator learner.
 - An additive model that reduces failure cases.


### Loss Function
The function of loss depends on the type of problem we are going to resolve.

It has to be differentiable. However, you should describe your own loss functions and help them.

Regression may use a squared error, for instance. In contrast, the classification may require a logarithmic loss.

The benefit of the gradient booster framework is that for each loss function, you may decide to use, the new booster algorithm does not need to extract. 

Instead, the framework is general enough to enable any differentiable loss function.

### Weak Learner
Decision trees are used in gradient boosting as weak learners.

Regression arborescences split values and add the output to them together to allow for the inclusion of results of the next models and to "right" the residuals in the predictions.

### Additive Model
Trees are introduced one at a time. The current trees in the model are not updated. A gradient descent technique minimizes losses when adding trees.

Traditionally, gradient descent minimizes the number of parameters, such as the regression equation coefficients or the neural network weights. 

After measuring the error or loss, the values are updated to minimize the error.

Instead of parameters, we have poor learning sub-models or, more precisely, decision trees. After calculating the loss, we have to add a tree to the model that decreases the loss (i.e., follows the gradient) to perform the gradient descent process. 

This is achieved by parameterizing the tree. Changing the tree parameters and heading in the right direction (reducing the residual loss).

This method is commonly referred to as functional gradient descent or gradient descent with functions.


## Algoritmo de Gradient Boosting

### Catboost

CatBoost is based on gradient boosted decision trees. During training, a set of decision trees is built consecutively. Each successive tree is built with reduced loss compared to the previous trees.

The number of trees is controlled by the starting parameters. To prevent overfitting, use the overfitting detector. When it is triggered, trees stop being built.

According to the CatBoost documentation, CatBoost supports numerical, categorical, and text features but has a good handling technique for categorical data. 

The CatBoost algorithm has quite a number of parameters to tune the features in the processing stage.

"Boosting" in CatBoost refers to the gradient boosting machine learning. Gradient boosting is a machine learning technique for regression and classification problems. 
Which produces a prediction model in an ensemble of weak prediction models, typically decision trees. 


Here we would look at the various features the CatBoost algorithm offers and why it stands out.

### Robust
CatBoost can improve the performance of the model while reducing overfitting and the time spent on tuning.  

CatBoost has several parameters to tune. Still, it reduces the need for extensive hyper-parameter tuning because the default parameters produce a great result.

Overfitting is a common problem in gradient boosting, especially when the dataset is small or noisy. CatBoost has several features that help reduce overfitting.

One of them is a novel gradient-based regularization technique called ordered boosting, which penalizes complex models that overfit the data. Another feature is the use of per-iteration learning rate, which allows the model to adapt to the complexity of the problem at each iteration.

### Automatic Handling of Missing Values
Missing values are a common problem in real-world datasets. Traditional gradient boosting frameworks require imputing missing values before training the model. CatBoost, however, can handle missing values automatically. 

During training, it learns the optimal direction to move along the gradient for each missing value, based on the patterns in the data.

### Accuracy
The CatBoost algorithm is a high performance and greedy novel gradient boosting implementation. 

Hence, CatBoost (when implemented well) either leads or ties in competitions with standard benchmarks.

### Categorical Features Support
The key features of CatBoost is one of the significant reasons why it was selected by many boosting algorithms such as LightGBM,  XGBoost algorithm ..etc 

With other machine learning algorithms. After preprocessing and cleaning your data, the data has to be converted into numerical features so that the machine can understand and make predictions.

This is same like, for any text related models we convert the text data into to numerical data it is know as word embedding techniques.

This process of encoding or conversion is time-consuming. CatBoost supports working with non-numeric factors, and this saves some time plus improves your training results.

### Easy Implementation
CatBoost offers easy-to-use interfaces. The CatBoost algorithm can be used in Python with scikit-learn, R, and command-line interfaces.

Fast and scalable GPU version: the researchers and machine learning engineers designed CatBoost at Yandex to work on data sets as large as tens of thousands of objects without lagging. 

Training your model on GPU gives a better speedup when compared to training the model on CPU. 

To crown this improvement, the larger the dataset is, the more significant the speedup. CatBoost efficiently supports multi-card configuration. So, for large datasets, use a multi-card configuration.

### Faster Training & Predictions
Before the improvement of servers, the maximum number of GPUs per server is 8 GPUs. Some data sets are more extensive than that, but CatBoost uses distributed GPUs. 

This feature enables CatBoost to learn faster and make predictions 13-16 times faster than other algorithms.

### Interpretability
CatBoost provides some level of interpretability. It can output feature importance scores, which can help understand which features are most relevant for the prediction. 

It also supports visualization of decision trees, which can help understand the structure of the model.

### Supporting Community of Users
The non-availability of a team to contact when you encounter issues with a product you consume can be very annoying. This is not the case for CatBoost. 

CatBoost has a growing community where the developers lookout for feedbacks and contributions.

There is a Slack community, a Telegram channel (with English and Russian versions), and Stack Overflow support. If you ever discover a bug, there is a page via GitHub for bug reports.

### Is tuning required in CatBoost?
The answer is not straightforward because of the type and features of the dataset. The default settings of the parameters in CatBoost would do a good job. 

CatBoost produces good results without extensive hyper-parameter tuning. However, some important parameters can be tuned in CatBoost to get a better result. 

These features are easy to tune and are well-explained in the CatBoost documentation. Here are some of the parameters that can be optimized for a better result;

- cat_ features, 
- one_hot_max_size, 
- learning_rate & n_estimators,
- max_depth, 
- subsample, 
- colsample_bylevel, 
- colsample_bytree, 
- colsample_bynode, 
- l2_leaf_reg, 
- random_strength.

### When To Use CatBoost
#### Short training time on a robust data
Unlike some other machine learning algorithms, CatBoost performs well with a small data set. 

However, it is advisable to be mindful of overfitting. A little tweak to the parameters might be needed here.

#### Working on a small data set
This is one of the significant strengths of the CatBoost algorithm. Suppose your data set has categorical features, and converting it to numerical format seems to be quite a lot of work.

In that case, you can capitalize on the strength of CatBoost to make the process of building your model easy.

#### When you are working on a categorical dataset
CatBoost is incredibly faster than many other machine learning algorithms. The splitting, tree structure, and training process are optimized to be faster on GPU and CPU. 

Training on GPU is 40 times faster than on CPU, two times faster than LightGBM, and 20 times faster than XGBoost.

### When To Not Use CatBoost
There are not many disadvantages of using CatBoost for whatever data set. 

So far, the hassle why many do not consider using CatBoost is because of the slight difficulty in tuning the parameters to optimize the model for categorical features.
