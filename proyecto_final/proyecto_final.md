# Introducción

Mediante el presente trabajo se pretende investigar y aprender técnicas de inteligencia artificial que no hayan sido vistas durante el cursado de la materia y aplicarlas en un caso práctico el cual será: a partir de un conjunto de datos referentes al mercado inmobiliario crear un modelo y entrenarlo. 
Una vez conseguido un buen ajuste, utilizaremos este modelo para predecir el precio de viviendas en esa área.

El objetivo principal del proyecto es expandir los conocimientos de machine learning investigando 3 posibles algoritmos a implementar, entre ellos, linear regression, glment y catboost.

En las siguientes secciones se explicarán todos aquellos conceptos teóricos utilizados por cada algoritmo y se explicarán las implementaciones para resolver el problema, así como comparaciones entre los distintos algoritmos aplicados. 

# Marco teórico



# Diseño experimental 


## Metricas
Se recuerda que en el presente trabajo se aplicaron varios algoritmos, motivo por el cual debemos de contar con metricas para comparar el funcionamiento  y eficiencia de cada implementacion. De manera de poder decidir cual implementacion es mejor.  
Las metricas a utilizar son:
- (R-squared) metric: R-cuadrado (R² o coeficiente de determinación) es una medida estadística de un modelo de regresión que determina la proporción de varianza
de la variable dependiente que puede explicar la variable independiente. En otras palabras, r-cuadrado muestra lo bien que se ajustan los datos al modelo de regresión.
Es la métrica de evaluación más popular para los modelos de regresión. R-cuadrado puede tomar cualquier valor entre 0 y 1.
Esta medida se define por la proporción de la variabilidad total explicada por el modelo de regresión: 
![image](https://user-images.githubusercontent.com/88351465/230745972-0bbc0a0a-4844-4325-8aaf-271188d82b63.png)

La interpretación más común de r-cuadrado es lo bien que el modelo de regresión explica los datos observados. 
Por ejemplo, una r-cuadrado del 60% indica que el modelo de regresión explica el 60% de la variabilidad observada en la variable objetivo. 
En general, una r-cuadrado más alta indica que el modelo explica más variabilidad.
En el presente trabajo se espera que los modelos con r-cuadrado mas alta representaran mejor los datos observados. 

- RMSE (Root Mean Squared Error): es la raíz cuadrada de la varianza de los residuos. 
Especifica el ajuste absoluto del modelo a los datos, es decir, lo cerca que están los puntos de datos observados de los valores predichos.
Matematicamente puede ser representada:
![image](https://user-images.githubusercontent.com/88351465/228042735-94668220-b84b-46e0-a3c2-3f915c17430a.png)
La idea básica es medir lo malas/erróneas que son las predicciones del modelo cuando se comparan con los valores reales observados. 
Así, un RMSE alto es "malo" y un RMSE bajo es "bueno". En la fórmula, la diferencia entre los valores observados y los predichos se denomina residuo. 
El error cuadrático medio (MSE) es la media de todos los residuos al cuadrado. 
Entonces, el RMSE simplemente toma la raíz cuadrada de eso, lo que devuelve la métrica a la escala de la variable de respuesta.
## Herramientas utilizadas
El lenguaje de programacion utilizado para la implementacion del presente trabajo es R. Implementando el proyecto en RStudio.
El motivo por el cual se decidio trabajar con estas herramientas es que cuentan con gran variedad de librerias utiles para implementar el presente trabajo.


## Detalle y justificacion

En primer lugar, el proyecto incluye una seccion de instalacion e importacion de las librerias a utilizar. 
Luego se procedio a cargar el dataset "BostonHousing", que incluye datos de vivienda de 506 secciones censales de Boston del censo de 1970.
Los datos originales son 506 observaciones sobre 14 variables, siendo medv la variable objetivo: 

crim:	per capita crime rate by town
zn:	proportion of residential land zoned for lots over 25,000 sq.ft
indus:	proportion of non-retail business acres per town
chas:	Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
nox:	nitric oxides concentration (parts per 10 million)
rm:	average number of rooms per dwelling
age:	proportion of owner-occupied units built prior to 1940
dis:	weighted distances to five Boston employment centres
rad:	index of accessibility to radial highways
tax:	full-value property-tax rate per USD 10,000
ptratio:	pupil-teacher ratio by town
b:	1000(B - 0.63)^2 where B is the proportion of blacks by town
lstat:	percentage of lower status of the population
medv:	median value of owner-occupied homes in USD 1000's

Luego procedi a comprobar si el dataset tenia valores faltantes, lo cual habria modificado los resultados finales. 
Satisfactoriamente no se encontro ningun valor faltante. Por lo tanto el siguiente paso fue analizar el dataset.
Ejecutando summary del dataset obtenemos estadisticas basicas del mismo, por ejemplo la media, promedio, 1st quartile, etc.

![image](https://user-images.githubusercontent.com/88351465/230747076-9966a3ad-3dd4-470f-908d-b572a2cb1a32.png)

En la imagen podemos observar que ‘crim’, ‘zn’, ‘rm’ and ‘black’ tienen gran diferencia entre su mediana y media, lo cual indica que es posible que tengan valores "outliers" valores atípicos. 

Realizando boxplots de las variables mencionadas podemos observar que tienen gran cantidad de valores outliers: 
![image](https://user-images.githubusercontent.com/88351465/230747197-d194e2fb-00c5-44fd-97e2-697c29dadee4.png)

A continuacion analice el Correlation plots, lo cual es un una buena manera de explorar los datos y examinar el nivel de interaccion entre las variables. 
La correlación es una medida estadística que sugiere el nivel de dependencia lineal entre dos variables que se dan en pareja. Su valor oscila entre -1 y +1.
Si es superior a 0 significa correlación positiva, es decir, X es directamente proporcional a Y.
Si es inferior a 0, significa correlación negativa, es decir, X es inversamente proporcional a Y.
Utilizando corrplot es posible obtener el siguiente grafico: 
![image](https://user-images.githubusercontent.com/88351465/230747298-a2cdf9b5-2b03-4fb7-a873-ac7c0650b199.png)

Analizando el plot podemos observar lo siguiente: 
 - Los atributos/variables ‘tax and rad’, ‘nox and tax’, ‘age and indus’ tienen correlacion positiva
 - Los atributos/variables ‘dis and nox’, ‘dis and indus’, ‘age and dis’ tienen correlacion negativa. 

Procedi a dividir el dataset en train y test, y teniendo en cuenta el analisis general realizado,  estaba en condiciones de implementar los modelos

A continuación se presentan los resultados de predicción de los modelos implementados: 
-	Linear Regression, utilizando medv como variable dependiente y lstat como variable independiente. 
 ![image](https://user-images.githubusercontent.com/88351465/230801532-b50bda9d-b03a-421c-95c3-e1118bfb1372.png)

-	Linear Regression, utilizando medv como variable dependiente y crim + rm + tax + lstat como variables independientes. 
 ![image](https://user-images.githubusercontent.com/88351465/230801597-43583cc5-2b82-48f1-abfd-355383eda9a8.png)

-	Linear Regression, utilizando medv como variable dependiente y utilizando todas las variables excepto aquellas variables que son altamente correlacionadas ("indus" "nox"   "tax"   "dis"  ). 
 ![image](https://user-images.githubusercontent.com/88351465/230801607-3fef6248-b1c7-4172-bd5b-ef9d40cf8438.png)

-	Linear Regression utilizando medv como variable dependiente y  las demás variables como independientes, con 10-fold cross validation. 
 ![image](https://user-images.githubusercontent.com/88351465/230801647-4a136e4e-86fc-4be3-82d9-5a77c8f8f8ac.png)

-	 Ridge Regression utilizando medv como variable dependiente y demás variables como independientes, con 10-fold cross validation.
 ![image](https://user-images.githubusercontent.com/88351465/230801672-31d43a75-6115-4249-8fcd-5ce6d3bf5ca6.png)

-	Lasso Regression utilizando medv como variable dependiente y demás variables como independientes, con 10-fold cross validation.
 ![image](https://user-images.githubusercontent.com/88351465/230801684-88ae8ca7-95aa-497b-8f3a-4fa9295f26c3.png)

-	Catboost Regression, utilizando learning_rate=0.01(La tasa de aprendizaje, se utiliza para reducir el paso de gradiente.), iterations=500 (Número máximo de árboles que se pueden construir al resolver problemas de aprendizaje automático), depth=10 (profundidad del árbol), loss_function=”RMSE” (la métrica a utilizar). 
 ![image](https://user-images.githubusercontent.com/88351465/230801705-15763d94-3bf5-4d7a-b152-d53fbfd8b12d.png)

Plots de prediccion de los modelos: 
- Linear regression simple: 

![image](https://user-images.githubusercontent.com/88351465/230802502-023d5783-69af-4d9b-9c05-6a92555f2a26.png)
- Linear regression multiple


![image](https://user-images.githubusercontent.com/88351465/230802547-71588e5a-17c2-470e-8ac4-a0ed32e9fc3a.png)

- Linear regression con CV


![image](https://user-images.githubusercontent.com/88351465/230802560-7a4fa001-99ef-4df4-91b8-b845910f8edc.png)

- Ridge regression con CV


![image](https://user-images.githubusercontent.com/88351465/230802606-1a35c80c-9e11-4245-a042-42f7f39d18da.png)

- Lasso regression con CV


![image](https://user-images.githubusercontent.com/88351465/230802576-62f3aca3-d589-4f4a-b28c-747cbe618eaa.png)

- Catboost


![image](https://user-images.githubusercontent.com/88351465/230802620-93c17efa-1e5e-4c22-b763-eb2aea9cb5e6.png)


# Análisis y discusión de resultados
Recordando del marco teórico, un RMSE bajo presenta mejor performance frente a un RMSE alto. Por otro lado un R2 mayor presenta mejor performance frente a un R2 menor. Teniendo en cuenta lo mencionado, podemos observar lo siguiente: 
El modelo que obtuvo menor performance, comparando las métricas de RMSE y Rsquared es Linear Regression. Aunque podemos ver que al aplicar cross validation obtenemos resultados muy similares a Lasso y Ridge regression (con cv). 
Por otro lado, el vencedor de los modelos es Catboost Regression con una notable mejora con un RMSE menor y un Rsquared mucho mayor (0.8808 aprox) frente al primer Rsquared obtenido por Linear regression (0.5945 aprox). Analizando los plots claramente el vencedor tambien es catboost. La prediccion refleja una curva que representa gran cantidad de los datos. 
A continuación modificaré el modelo de Catboost, con el objetivo de obtener mejores resultados. 

# Conclusiones finales
