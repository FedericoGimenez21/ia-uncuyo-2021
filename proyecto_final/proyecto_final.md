# Introducción

Mediante el presente trabajo se pretende investigar y aprender técnicas de inteligencia artificial que no hayan sido vistas durante el cursado de la materia y aplicarlas en un caso práctico el cual será: a partir de un conjunto de datos referentes al mercado inmobiliario crear un modelo y entrenarlo. 
Una vez conseguido un buen ajuste, utilizaremos este modelo para predecir el precio de viviendas en esa área.

El objetivo principal del proyecto es expandir los conocimientos de machine learning investigando 3 posibles algoritmos a implementar, entre ellos, linear regression, glment y catboost.

En las siguientes secciones se explicarán todos aquellos conceptos teóricos utilizados por cada algoritmo y se explicarán las implementaciones para resolver el problema, así como comparaciones entre los distintos algoritmos aplicados. 

# Marco teórico


## Linear Regression
La regresión lineal simple hace honor a su nombre: es un método muy sencillo para predecir una respuesta cuantitativa Y a partir de una única variable de predicción X. Asume que existe aproximadamente una relación lineal entre X e Y .
El análisis de regresión lineal se utiliza para predecir el valor de una variable a partir del valor de otra variable.
La variable que se desea predecir se denomina variable dependiente. La variable que se utiliza para predecir el valor de la otra variable se denomina variable independiente.

Esta forma de análisis estima los coeficientes de la ecuación lineal, en la que intervienen una o más variables independientes, que mejor predicen el valor de la variable dependiente.
La regresión lineal ajusta una línea recta o superficie que minimiza las discrepancias entre los valores de salida predichos y los reales. Existen calculadoras de regresión lineal sencillas que utilizan un método de "mínimos cuadrados" para descubrir la línea que mejor se ajusta a un conjunto de datos emparejados. Luego, se estima el valor de X (variable dependiente) a partir de Y (variable independiente).

Es posible realizar el método de regresión lineal en una variedad de programas y entornos, entre los que se incluyen:

- R regresión lineal
- Regresión lineal MATLAB
- Regresión lineal Python
- Regresión lineal Excel

### ¿Por qué es importante la regresión lineal?
Los modelos de regresión lineal son relativamente sencillos y proporcionan una fórmula matemática fácil de interpretar que puede generar predicciones. 
La regresión lineal puede aplicarse a diversas áreas en los negocios y el estudio académico. Se utiliza en todos los campos, desde las ciencias biológicas, del comportamiento, medioambientales y sociales hasta los negocios. 
Los modelos de regresión lineal se han convertido en una forma probada de predecir el futuro de forma científica y fiable. Dado que la regresión lineal es un procedimiento estadístico establecido desde hace mucho tiempo, las propiedades de los modelos de regresión lineal se comprenden bien y pueden entrenarse muy rápidamente.

Matemáticamente, podemos escribir esta relación lineal como la formula presentada en la figura 1 *Formula de regresion lineal*: 


  
<p align="center" style="margin-bottom: 0px !important;">
  <img width="200" src="https://user-images.githubusercontent.com/88351465/228034735-21d214a8-09cf-4943-83ee-02c1da9d981f.png" alt="Formula de regresion lineal" align="center">
</p>
<p align="center" >Figura 1. Formula de regresion lineal</p>

Podemos leer "≈" como "se modela aproximadamente como" 

En conjunto, β0 y β1 se conocen como coeficientes o parámetros del modelo. Una vez que hemos utilizado nuestros
datos de entrenamiento para obtener las estimaciones βˆ0 y βˆ1 de los coeficientes del modelo, podemos predecir las ventas futuras en función de un valor concreto de la publicidad televisiva calculando la formula de prediccion presentada en la figura 2. *Formula de prediccion*: 

<p align="center" style="margin-bottom: 0px !important;">
  <img width="200" src="https://user-images.githubusercontent.com/88351465/228034991-73ce2857-6dba-4857-8ce9-b52a4192730f.png" alt="Formula de prediccion lineal" align="center">
</p>

<p align="center" >Figura 2. Formula de prediccion</p>

donde ˆy indica una predicción de Y sobre la base de X = x. Aquí utilizamos un símbolo de sombrero, ˆ , para denotar el valor estimado para un parámetro o coeficiente desconocido, o para denotar el valor predicho de la respuesta.

No todos los problemas pueden resolverse con el mismo algoritmo. En este caso, la regresión lineal supone que existe una relación lineal entre la variable de respuesta y las variables explicativas. Esto significa que se puede ajustar una línea entre las dos (o más variables).


<p align="center" style="margin-bottom: 0px !important;">
  <img width="400" src="https://user-images.githubusercontent.com/88351465/228036888-d6d48b36-231b-4eec-936c-6b7f7aa19b2e.png" alt="Formula de prediccion lineal" align="center">
</p>
<p align="center" >Figura 3. Relacion lineal</p>


El gráfico presentado en la Figura 3,  muestra la relación lineal entre la variable de salida (y) y las variables predictoras (X).  La línea azul se denomina línea recta de mejor ajuste. A partir de los puntos de datos dados, intentamos trazar una línea que se ajuste lo mejor posible a los puntos.

Para calcular la recta de mejor ajuste, la regresión lineal utiliza una forma tradicional de pendiente-intersección que se indica a continuación,

Yi = β0 + β1Xi 

donde Yi = Variable dependiente, β0 = Intercepción, β1 = Pendiente, Xi = Variable independiente.
Este algoritmo explica la relación lineal entre la variable dependiente (output) Y y la variable independiente (predictor) X utilizando una línea recta Y= B0 + B1 X. En la imagen siguiente, Figura 4, se observa como se relacionan y actuan los componentes mencionados (intercepcion, variable independiente y dependiente y pendiente). 

<p align="center" style="margin-bottom: 0px !important;">
  <img width="400" src="https://user-images.githubusercontent.com/88351465/228037271-1e463a58-8ad9-4785-872c-aefc25aa6ba9.png" alt="Regresion lineal" align="center">
</p>
<p align="center" >Figura 4. Componentes de relacion lineal</p>



Pero, ¿cómo averigua la regresión lineal cuál es la recta de mejor ajuste?
El objetivo del algoritmo de regresión lineal es obtener los mejores valores de B0 y B1 para encontrar la recta de mejor ajuste. La línea de mejor ajuste es una línea que tiene el menor error, lo que significa que el error entre los valores predichos y los valores reales debe ser mínimo.

Residuos
Una buena forma de comprobar la calidad del ajuste del modelo es observar los residuos o las diferencias entre los valores reales y los valores predichos. La línea recta de la Figura 5 representa los valores previstos. En la misma imagen, la línea vertical roja que va de la línea recta al valor de los datos observados es el residuo.

<p align="center" style="margin-bottom: 0px !important;">
  <img width="400" src="https://user-images.githubusercontent.com/88351465/228037812-0ae63623-167c-4003-80e1-94a6f45f1d70.png" alt="Residuo" align="center">
</p>
<p align="center" >Figura 5. Residuo</p>


La idea es que la suma de los residuos sea aproximadamente cero o lo más baja posible. En la vida real, la mayoría de los casos no seguirán una línea perfectamente recta, por lo que es de esperar que haya residuos.

### ¿Qué es la recta de mejor ajuste?
En términos sencillos, la línea de mejor ajuste es una línea que se ajusta de la mejor manera al diagrama de dispersión dado. Matemáticamente, la línea de mejor ajuste se obtiene minimizando la suma residual de cuadrados (RSS).

La calidad del ajuste de una regresión lineal suele evaluarse mediante dos magnitudes relacionadas: el error estándar residual (RSE) y el estadístico R2. RSE: En términos generales, es la desviación media de la respuesta con respecto a la línea de regresión real. Se calcula mediante la fórmula:

<p align="center" style="margin-bottom: 0px !important;">
  <img width="400" src="https://user-images.githubusercontent.com/88351465/228039774-549a2d0a-f6af-4179-bbe9-633ee7abb680.png" alt="RSE" align="center">
</p>
<p align="center" >Figura 6. Formula de RSE</p>


Teniendo en cuenta que RSS es: 

<p align="center" style="margin-bottom: 0px !important;">
  <img width="300" src="https://user-images.githubusercontent.com/88351465/228039870-d0b43267-aede-4610-8dca-a36912d4ddd4.png" alt="RSS" align="center">
</p>
<p align="center" >Figura 7. Formula de RSS</p>

El RSE se considera una medida de la falta de ajuste del modelo a los datos. Si las predicciones obtenidas con el modelo se aproximan mucho a los verdaderos valores de los resultados -es decir, si ˆyi ≈ yi para i = 1,...,n-, el RSE será pequeño y podremos concluir que el modelo se ajusta muy bien a los datos. Por otro lado, si ˆyi está muy lejos de yi para una o más observaciones, entonces el RSE puede ser bastante grande, lo que indica que el modelo no se ajusta bien a los datos.

## GLMNET (Ridge Regression y Lasso Regression)

### Ridge Regression 
Ridge regression es muy similar a la de mínimos cuadrados, salvo que los coeficientes de ridge regression se estiman minimizando una cantidad ligeramente diferente. En particular, las estimaciones de los coeficientes de regresión de cresta βˆR son los valores que minimizan. Su formula se presenta en la figura 8 *Formula de Ridge Regression*: 


<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/228047089-f5c18fe4-1cc8-405a-a1f9-85a3928f86e2.png" alt="RSS" align="center">
</p>
<p align="center" >Figura 8. Formula de Ridge Regression</p>


donde λ ≥ 0 es un parámetro de ajuste, que se determinará por separado. 
El parámetro de ajuste λ sirve para controlar el impacto relativo de estos dos términos en las estimaciones del coeficiente de regresión. Cuando λ = 0, el término de penalización no tiene efecto, y la regresión ridge producirá las estimaciones por mínimos cuadrados. Sin embargo, a medida que λ → ∞, el impacto de la penalización por contracción crece, y las estimaciones del coeficiente de la regresión ridge se aproximarán a cero. 

Seleccionar un buen valor para λ es fundamental. Una opción óptima es probar un montón de valores para λ y utilizar la validación cruzada, para determinar cuál da lugar a la varianza más baja. 

¿Por qué la regresión Ridge es mejor que la de mínimos cuadrados?
La ventaja de la regresión Ridge sobre los mínimos cuadrados se basa en el equilibrio sesgo-varianza. A medida que aumenta λ, disminuye la flexibilidad del ajuste de ridge regression, lo que conduce a una disminución de la varianza pero a un aumento del sesgo.

### Lasso Regression 

Es una alternativa relativamente reciente a Ridge regression. Formula presentada en figura 9 *Formula de lasso regression*: 

<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/228049230-f9f6a8e0-804b-4e0e-88ae-94eae70106b1.png" alt="lasso regression" align="center">
</p>
<p align="center" >Figura 9. Formula de lasso regression</p>


Es observable que la regresión lasso y la regresión ridge tienen formulas similares.

La única diferencia es que el término βj^2 en la regresión ridge ha sido sustituido por |βj| en la penalización del lazo.
Al igual que en la regresión ridge, lasso reduce las estimaciones de los coeficientes hacia cero.

Lasso produce modelos más sencillos e interpretables en los que sólo interviene un subconjunto de predictores.

### Análisis comparativo de la regresión Lasso y Ridge
La regresión Ridge y Lasso utilizan dos funciones de penalización diferentes para la regularización. La regresión Ridge utiliza L2, mientras que la regresión Lasso utiliza la técnica de regularización L1. En la regresión ridge, la penalización es igual a la suma de los cuadrados de los coeficientes y en la Lasso, la penalización se considera la suma de los valores absolutos de los coeficientes. En la regresión lasso, es la contracción hacia cero utilizando un valor absoluto (penalización L1 o técnica de regularización) en lugar de una suma de cuadrados (penalización L2 o técnica de regularización).

### Selección del parámetro de ajuste

La implementación de la regresión ridge y el lazo requiere un método para seleccionar un valor para el parámetro de ajuste λ. La validación cruzada proporciona una forma sencilla de abordar este problema. Elegimos una cuadrícula de valores de λ y calculamos el error de validación cruzada para cada valor de λ. A continuación, seleccionamos el valor del parámetro de ajuste para el que el error de validación cruzada es menor. Por último, se vuelve a ajustar el modelo utilizando todas las observaciones disponibles y el valor seleccionado del parámetro de ajuste. 

## Boosting

Es un método de aprendizaje conjunto en el que construimos múltiples aprendices débiles (mismos algoritmos) de forma paralela.
Todos estos aprendices débiles toman la retroalimentación de los modelos anteriores para mejorar su capacidad de predecir con precisión las clases mal clasificadas. Al final, el algoritmo utiliza todos estos aprendices débiles para construir el modelo final.
Las predicciones del modelo final utilizan el enfoque de votación por mayoría para los problemas de clasificación. Mientras que para el tipo de problema de regresión, el valor final es el valor promedio de todos los modelos de aprendizaje débiles.

¿Puede lograrse un modelo fuerte a partir de muchos modelos que son relativamente pobres y que simplemente también se denominan aprendices débiles? En otras palabras, ¿pueden los múltiples aprendices débiles formar un modelo fuerte para predecir el futuro o el conjunto de datos de prueba?
Al decir "modelos débiles" no nos referimos a modelos básicos simples como los árboles de decisión. Sino modelos con una precisión de bajo rendimiento, donde bajo es un poco mejor que aleatorio.

¿Cómo podemos construir entonces tales modelos? Una respuesta matemática positiva a esta pregunta tardó unos cuantos años en crear una solución totalmente funcional basada en algoritmos.

En resumen, este algoritmo funciona en unos pocos pasos con un enfoque codicioso.

Al principio, construyen una combinación lineal de modelos simples (algoritmos básicos) reponderando los datos de entrada. El modelo (normalmente el árbol de decisión) asigna pesos mayores a los elementos predichos incorrectamente.

### ¿Qué es un algoritmo de aumento gradual (Gradient boosting Algorithm)?

Gradient Boosting, Gradient Tree Boosting o Gradient Boosted Regression Trees (GBRT), es una familia de algoritmos usados tanto en clasificación como en regresión basados en la combinación de modelos predictivos débiles (weak learners) -normalmente árboles de decisión- para crear un modelo predictivo fuerte. La generación de los árboles de decisión débiles se realiza de forma secuencial, creándose cada árbol de forma que corrija los errores del árbol anterior. Los aprendices suelen ser árboles "poco profundos" (shallow trees), de apenas uno, dos o tres niveles de profundidad, típicamente.

Uno de los parámetros de este tipo de argumentos es el learning rate o tasa de aprendizaje, que controla el grado de mejora de un árbol respecto del anterior. Una tasa de aprendizaje pequeña supone una mejora más lenta pero adaptándose mejor a los datos, lo que se traduce generalmente en mejoras en el resultado a costa de un mayor consumo de recursos.

La idea principal de este algoritmo es construir modelos secuencialmente y que estos modelos posteriores intenten reducir los errores del modelo anterior. Pero, ¿cómo lo hacemos? ¿Cómo reducimos el error? Esto se hace construyendo un nuevo modelo sobre los errores o residuos del modelo anterior.

Cuando la columna objetivo es continua, utilizamos el Gradient Boosting Regressor, mientras que cuando se trata de un problema de clasificación, utilizamos el Gradient Boosting Classifier. La única diferencia entre ambos es la "función de pérdida". El objetivo aquí es minimizar esta función de pérdida añadiendo aprendices débiles utilizando el descenso de gradiente. Dado que se basa en la función de pérdida, para los problemas de regresión, tendremos diferentes funciones de pérdida como el error cuadrático medio (MSE) y para la clasificación, tendremos diferentes funciones.

### ¿Cómo funciona el refuerzo por gradiente (Gradient Boosting)?

Gradient Boosting puede utilizarse tanto para problemas de regresión como de clasificación. Estas técnicas de enseñanza generan un modelo de predicción en forma de una serie de modelos de predicción débiles, normalmente en forma de árboles de decisión.

En el gradient boosting intervienen tres componentes:

- Una función de pérdida optimizada.
- Un aprendiz de indicadores débiles.
- Un modelo aditivo que reduce los casos de fallo.

#### Función de pérdida
La función de pérdida depende del tipo de problema que vayamos a resolver.

Tiene que ser diferenciable. Sin embargo, es conveniente describir las propias funciones de pérdida y ayudarnos de ellas.

La regresión puede utilizar un error al cuadrado, por ejemplo. En cambio, la clasificación puede requerir una pérdida logarítmica.

La ventaja del marco de refuerzo de gradiente es que para cada función de pérdida que decida utilizar, no es necesario extraer el nuevo algoritmo de refuerzo.

En su lugar, el marco es lo suficientemente general como para permitir cualquier función de pérdida diferenciable.

#### Aprendiz débil
Las arborescencias de regresión (regression arborescences) dividen los valores y les suman la salida para permitir la inclusión de los resultados de los modelos siguientes y "enderezar" los residuos en las predicciones.

#### Modelo aditivo
Los árboles se introducen de uno en uno. Los árboles actuales del modelo no se actualizan. Una técnica de descenso por gradiente minimiza las pérdidas al añadir árboles.

Tradicionalmente, el descenso de gradiente minimiza el número de parámetros, como los coeficientes de la ecuación de regresión o los pesos de la red neuronal.

Tras medir el error o la pérdida, los valores se actualizan para minimizar el error.

En lugar de parámetros, tenemos submodelos de aprendizaje pobres o, más exactamente, árboles de decisión. Tras calcular la pérdida, tenemos que añadir al modelo un árbol que disminuya la pérdida (es decir, que siga el gradiente) para realizar el proceso de descenso gradiente.

Esto se consigue parametrizando el árbol. Cambiando los parámetros del árbol y dirigiéndonos en la dirección correcta (reduciendo la pérdida residual).

Este método se conoce comúnmente como descenso de gradiente funcional o descenso de gradiente con funciones.

### Algoritmo de Gradient Boosting

#### Catboost 
CatBoost se basa en árboles de decisión potenciados por gradiente. Durante el entrenamiento, se construye consecutivamente un conjunto de árboles de decisión. Cada árbol sucesivo se construye con una pérdida reducida en comparación con los árboles anteriores.

El número de árboles se controla mediante los parámetros iniciales. Para evitar el sobreajuste, se utiliza el detector de sobreajuste. Cuando se activa, los árboles dejan de construirse.

Según la documentación de CatBoost, este algoritmo admite características numéricas, categóricas y de texto, pero tiene una buena técnica de manejo de datos categóricos.

El algoritmo CatBoost dispone de un gran número de parámetros para ajustar las características en la fase de procesamiento.

"Boosting" en CatBoost se refiere al aprendizaje automático de gradiente. Gradient boosting es una técnica de aprendizaje automático para problemas de regresión y clasificación. Produce un modelo de predicción en un conjunto de modelos de predicción débiles, normalmente árboles de decisión.

Aquí veremos las distintas características que ofrece el algoritmo CatBoost y por qué destaca.

##### Robusto
CatBoost puede mejorar el rendimiento del modelo a la vez que reduce el sobreajuste y el tiempo dedicado al ajuste.

CatBoost tiene varios parámetros que ajustar. Aún así, reduce la necesidad de un ajuste exhaustivo de los hiperparámetros porque los parámetros por defecto producen un gran resultado.

El sobreajuste es un problema común en el refuerzo de gradiente, especialmente cuando el conjunto de datos es pequeño o ruidoso. CatBoost tiene varias características que ayudan a reducir el sobreajuste.

Una de ellas es una novedosa técnica de regularización basada en el gradiente denominada boosting ordenado, que penaliza los modelos complejos que se ajustan en exceso a los datos. Otra característica es el uso de una tasa de aprendizaje por iteración, que permite al modelo adaptarse a la complejidad del problema en cada iteración.

##### Tratamiento automático de los valores perdidos
Los valores perdidos son un problema común en los conjuntos de datos del mundo real. Los sistemas tradicionales de refuerzo por gradiente requieren imputar los valores perdidos antes de entrenar el modelo. CatBoost, sin embargo, puede manejar los valores perdidos automáticamente.

Durante el entrenamiento, aprende la dirección óptima para moverse a lo largo del gradiente para cada valor perdido, basándose en los patrones de los datos.

##### Precisión
El algoritmo CatBoost es una novedosa implementación de gradient boosting de alto rendimiento y codiciosa.

Por lo tanto, CatBoost (cuando está bien implementado) lidera o empata en competiciones con benchmarks estándar.

##### Soporte de características categóricas
Las características clave de CatBoost es una de las razones significativas por las que fue seleccionado por muchos algoritmos de boosting como LightGBM, XGBoost algorithm ..etc

Con otros algoritmos de aprendizaje automático. Después de preprocesar y limpiar los datos, hay que convertirlos en características numéricas para que la máquina pueda entenderlos y hacer predicciones.

Para cualquier modelo relacionado con texto, convertimos los datos de texto en datos numéricos, lo que se conoce como técnicas de incrustación de palabras.

Este proceso de codificación o conversión requiere mucho tiempo. CatBoost permite trabajar con factores no numéricos, lo que ahorra tiempo y mejora los resultados del entrenamiento.

##### Fácil implementación
CatBoost ofrece interfaces fáciles de usar. El algoritmo CatBoost puede utilizarse en Python con scikit-learn, R e interfaces de línea de comandos.

Versión para GPU rápida y escalable: los investigadores e ingenieros de aprendizaje automático de Yandex diseñaron CatBoost para trabajar con conjuntos de datos de hasta decenas de miles de objetos sin sufrir retrasos.

El entrenamiento del modelo en la GPU proporciona una mayor velocidad en comparación con el entrenamiento del modelo en la CPU.

Para coronar esta mejora, cuanto mayor sea el conjunto de datos, más significativa será la aceleración. CatBoost soporta eficientemente la configuración multitarjeta. Por tanto, para grandes conjuntos de datos, utilice una configuración multitarjeta.

##### Entrenamiento y predicciones más rápidos
Antes de la mejora de los servidores, el número máximo de GPUs por servidor era de 8 GPUs. Algunos conjuntos de datos son más extensos que eso, pero CatBoost utiliza GPUs distribuidas.

Esta característica permite a CatBoost aprender más rápido y realizar predicciones entre 13 y 16 veces más rápido que otros algoritmos.

##### Interpretabilidad
CatBoost ofrece cierto nivel de interpretabilidad. Puede mostrar puntuaciones de importancia de las características, lo que puede ayudar a entender qué características son las más relevantes para la predicción.

También permite la visualización de árboles de decisión, lo que puede ayudar a entender la estructura del modelo.

##### Apoyo a la comunidad de usuarios
La no disponibilidad de un equipo con el que contactar cuando se encuentran problemas con un producto que se consume puede ser muy molesto. Este no es el caso de CatBoost.

CatBoost tiene una comunidad en crecimiento donde los desarrolladores están atentos a los comentarios y contribuciones.

Hay una comunidad Slack, un canal Telegram (con versiones en inglés y ruso) y soporte Stack Overflow. Si alguna vez descubres un error, hay una página a través de GitHub para informes de errores.

##### ¿Es necesario el ajuste en CatBoost?
La respuesta no es sencilla debido al tipo y las características del conjunto de datos. Los ajustes por defecto de los parámetros en CatBoost harían un buen trabajo.

CatBoost produce buenos resultados sin un ajuste exhaustivo de los hiperparámetros. Sin embargo, algunos parámetros importantes pueden ajustarse en CatBoost para obtener mejores resultados.

Estos parámetros son fáciles de afinar y están bien explicados en la documentación de CatBoost. Estos son algunos de los parámetros que pueden optimizarse para obtener un mejor resultado;
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

#### ¿Cuándo utilizar CatBoost?

##### Corto tiempo de entrenamiento en un conjunto de datos robusto
A diferencia de otros algoritmos de aprendizaje automático, CatBoost funciona bien con un conjunto de datos pequeño.

Sin embargo, es aconsejable tener cuidado con el sobreajuste. En este caso, puede ser necesario un pequeño ajuste de los parámetros.

##### Trabajar con un conjunto de datos pequeño
Este es uno de los puntos fuertes del algoritmo CatBoost. Supongamos que su conjunto de datos tiene características categóricas, y convertirlas a formato numérico parece mucho trabajo.

En ese caso, puede aprovechar el potencial de CatBoost para facilitar el proceso de construcción de su modelo.

##### Cuando se trabaja con un conjunto de datos categóricos
CatBoost es increíblemente más rápido que muchos otros algoritmos de aprendizaje automático. La división, la estructura de árbol y el proceso de entrenamiento están optimizados para ser más rápidos en GPU y CPU.

El entrenamiento en GPU es 40 veces más rápido que en CPU, dos veces más rápido que LightGBM y 20 veces más rápido que XGBoost.

#### ¿Cuándo no usar CatBoost?
No hay muchos inconvenientes en utilizar CatBoost para cualquier conjunto de datos.

Hasta ahora, la molestia por la que muchos no consideran usar CatBoost es por la ligera dificultad en sintonizar los parámetros para optimizar el modelo para características categóricas.

### Algoritmo de regresión lineal (lm en R)
Se puede calcular una regresión lineal en R con el comando lm. El comando lm toma las variables en el formato

`lmData= lm([objetivo] ~ [predictor / características]`, datos = [fuente de datos])

Con el comando `summary(lmData)` se puede ver información detallada sobre el rendimiento y los coeficientes del modelo.

### Glmnet en R (regresión lasso y ridge)
Glmnet en R (regresión lasso y ridge)
Regresión Ridge - glmnet parámetro alpha=0 para la regresión ridge. Para predicción numérica elija familia - gaussiana, para clasificación familia = binomial, glmnet por defaut elige 100 valores lambda que dependen de los datos

`l_ridge <- glmnet(x, y, family="gaussian", alpha=0)`

Regresión Lasso - glmnet parámetro alpha=1 para regresión Lasso glmnet(x, y, alpha = 1)

# Diseño experimental 


## Métricas
Se recuerda que en el presente trabajo se aplicaron varios algoritmos, motivo por el cual debemos de contar con métricas para comparar el funcionamiento  y eficiencia de cada implementación. De manera de poder decidir cuál implementación es mejor.  
Las métricas a utilizar son:
- (R-squared) metric: R-cuadrado (R² o coeficiente de determinación) es una medida estadística de un modelo de regresión que determina la proporción de varianza de la variable dependiente que puede explicar la variable independiente. En otras palabras, r-cuadrado muestra lo bien que se ajustan los datos al modelo de regresión.
Es la métrica de evaluación más popular para los modelos de regresión. R-cuadrado puede tomar cualquier valor entre 0 y 1.
Esta medida se define por la proporción de la variabilidad total explicada por el modelo de regresión: 

<p align="center" style="margin-bottom: 0px !important;">
  <img width="400" src="https://user-images.githubusercontent.com/88351465/230745972-0bbc0a0a-4844-4325-8aaf-271188d82b63.png" alt="Formula de Rsquared" align="center">
</p>
<p align="center" >Figura 10. Formula de Rsquared</p>



La interpretación más común de r-cuadrado es lo bien que el modelo de regresión explica los datos observados. 
Por ejemplo, una r-cuadrado del 60% indica que el modelo de regresión explica el 60% de la variabilidad observada en la variable objetivo. 
En general, una r-cuadrado más alta indica que el modelo explica más variabilidad.
En el presente trabajo se espera que los modelos con r-cuadrado más alta representaran mejor los datos observados. 

- RMSE (Root Mean Squared Error): es la raíz cuadrada de la varianza de los residuos. 
Especifica el ajuste absoluto del modelo a los datos, es decir, lo cerca que están los puntos de datos observados de los valores predichos.
Matemáticamente puede ser representada:

<p align="center" style="margin-bottom: 0px !important;">
  <img width="400" src="https://user-images.githubusercontent.com/88351465/228042735-94668220-b84b-46e0-a3c2-3f915c17430a.png" alt="Formula de RMSE" align="center">
</p>
<p align="center" >Figura 11. Formula de RMSE</p>

La idea básica es medir lo malas/erróneas que son las predicciones del modelo cuando se comparan con los valores reales observados. 
Así, un RMSE alto es "malo" y un RMSE bajo es "bueno". En la fórmula, la diferencia entre los valores observados y los predichos se denomina residuo. 
El error cuadrático medio (MSE) es la media de todos los residuos al cuadrado. 
Entonces, el RMSE simplemente toma la raíz cuadrada de eso, lo que devuelve la métrica a la escala de la variable de respuesta.
## Herramientas utilizadas
El lenguaje de programación utilizado para la implementación del presente trabajo es R. Implementando el proyecto en RStudio.
El motivo por el cual se decidió trabajar con estas herramientas es que cuentan con gran variedad de librerías útiles para implementar el presente trabajo.

## Forma de evaluación de los modelos
Recordando que el objetivo del proyecto es poder comprobar el funcionamiento de los algoritmos y comparar resultados, la forma de evaluación de los modelos será la misma para todos. La cual será aplicar split en train/test a cada dataset, luego realizar los modelos ya sea linear regression, lasso, ridge o catboost, aplicando cross validation con 10-fold y presentar los resultados de Rsquared y RMSE. También se realizaran boxplot de los resultados y se presentaran métricas como media y desviación estándar, las cuales serán consideradas con gran énfasis al momento de comparar los algoritmos. 
Por lo tanto será importante recordar qué es y qué representa la desviación estándar a continuación: La desviación estándar mide la dispersión de una distribución de datos. Entre más dispersa está una distribución de datos, más grande es su desviación estándar. Es interesante que la desviación estándar no puede ser negativa. Una desviación estándar cercana a 0 indica que los datos tienden a estar más cerca a la media. Entre más lejos estén los datos de la media, más grande es la desviación estándar.

## Detalle y justificacion

### BostonHousing dataset

#### Analisis de BostonHousing 
En primer lugar, el proyecto incluye una sección de instalación e importación de las librerías a utilizar. 
Luego se procedió a cargar el dataset "BostonHousing", que incluye datos de vivienda de 506 secciones censales de Boston del censo de 1970.
Los datos originales son 506 observaciones sobre 14 variables, siendo `medv` la variable objetivo: 

- `crim`:	per capita crime rate by town
- `zn`:	proportion of residential land zoned for lots over 25,000 sq.ft
- `indus`:	proportion of non-retail business acres per town
- `chas`:	Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
- `nox`:	nitric oxides concentration (parts per 10 million)
- `rm`:	average number of rooms per dwelling
- `age`:	proportion of owner-occupied units built prior to 1940
- `dis`:	weighted distances to five Boston employment centres
- `rad`:	index of accessibility to radial highways
- `tax`:	full-value property-tax rate per USD 10,000
- `ptratio`:	pupil-teacher ratio by town
- `b`:	1000(B - 0.63)^2 where B is the proportion of blacks by town
- `lstat`:	percentage of lower status of the population
- `medv`:	median value of owner-occupied homes in USD 1000's

A continuación se comprobó si el dataset tenía valores faltantes, lo cual habría modificado los resultados finales. 
Satisfactoriamente no se encontró ningún valor faltante. Por lo tanto el siguiente paso fue analizar el dataset.
Ejecutando `summary` del dataset se obtienen estadísticas básicas del mismo, por ejemplo la media, promedio, 1st quartile, etc.

<p align="center" style="margin-bottom: 0px !important;">
  <img width="1000" src="https://user-images.githubusercontent.com/88351465/230747076-9966a3ad-3dd4-470f-908d-b572a2cb1a32.png"  align="center">
</p>
<p align="center" >Figura 12. `Summary` de BostonHousing</p>

En la figura 12 *Summary de BostonHousing* las variables `crim`, `zn`, `rm` and `black` tienen gran diferencia entre su mediana y media, lo cual indica que es posible que tengan valores "outliers" valores atípicos. 

Realizando boxplots de las variables mencionadas podemos observar que tienen gran cantidad de valores outliers: 

<p align="center" style="margin-bottom: 0px !important;">
  <img width="300" src="https://user-images.githubusercontent.com/88351465/230747197-d194e2fb-00c5-44fd-97e2-697c29dadee4.png"  align="center">
</p>
<p align="center" >Figura 13. Boxplot de variables `crim`, `zn`, `rm` and `black` de BostonHousing</p>


A continuación se analizó el Correlation plots, el cual es un una buena manera de explorar los datos y examinar el nivel de interacción entre las variables. 
La correlación es una medida estadística que sugiere el nivel de dependencia lineal entre dos variables que se dan en pareja. Su valor oscila entre -1 y +1.
Si es superior a 0 significa correlación positiva, es decir, X es directamente proporcional a Y.
Si es inferior a 0, significa correlación negativa, es decir, X es inversamente proporcional a Y.
Utilizando corrplot es posible obtener el grafico presentado en la imagen 14 *Correlation plot de BostonHousing*: 

<p align="center" style="margin-bottom: 0px !important;">
  <img width="300" src="https://user-images.githubusercontent.com/88351465/230747298-a2cdf9b5-2b03-4fb7-a873-ac7c0650b199.png"  align="center">
</p>
<p align="center" >Figura 14. Correlation plot de BostonHousing</p>



Analizando el plot de la figura 14 *Correlation plot de BostonHousing*  es posible observar lo siguiente: 
 - Los atributos/variables `tax and rad`, `nox and tax`, `age and indus` tienen correlación positiva
 - Los atributos/variables `dis and nox`, `dis and indus`, `age and dis` tienen correlación negativa. 

Luego se procedió a dividir el dataset en train y test, y teniendo en cuenta el análisis general realizado,  se comenzó a implementar los modelos. 


#### Evaluación linear regression de BostonHousing

-	Linear Regression utilizando `medv` como variable dependiente y  demás variables como independientes, con 10-fold cross validation. 

<p align="center" style="margin-bottom: 0px !important;">
  <img width="300" src="https://user-images.githubusercontent.com/88351465/234431881-fdcef957-2231-4f29-8e8f-175bbc06cb0e.png" alt="" align="center">
</p>
<p align="center" >Figura 15. Resultados Linear CV BostonHousing</p>

<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/234611632-2250af0b-5c51-413a-94d0-9ddcf940f971.png" alt="" align="center">
</p>
<p align="center" >Figura 16. Plot mejor prediccion de Linear BostonHousing</p>



<p align="center" style="margin-bottom: 0px !important;">
  <img width="600" src="https://user-images.githubusercontent.com/88351465/234432123-93a025d8-db70-4711-a6e4-24c41c0fce6f.png" alt="" align="center">
</p>
<p align="center" >Figura 17. Boxplot BostonHousing Linear CV Rsquared y RMSE</p>



<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/235268207-68ccbbb5-e1e3-43ff-bdd8-9306e98baa4d.png" alt="" align="center">
</p>
<p align="center" >Figura 18. Metricas de Linear CV obtenidas de BostonHousing</p>




#### Evaluación Ridge regression de BostonHousing
-	 Ridge Regression utilizando `medv` como variable dependiente y demás variables como independientes, con 10-fold cross validation. Con 50 valores de lambda tomando valores desde 0.0001 hasta 1. 



<p align="center" style="margin-bottom: 0px !important;">
  <img width="300" src="https://user-images.githubusercontent.com/88351465/234432743-50722662-f92a-4648-886f-031e113ef1c0.png" alt="" align="center">
</p>
<p align="center" >Figura 19. Resultados de Ridge CV regression BostonHousing</p>


<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/234613338-f291d0bc-5c5d-415e-bc13-5d8db58101db.png" alt="" align="center">
</p>
<p align="center" >Figura 20. Plot mejor prediccion de Ridge BostonHousing</p>




<p align="center" style="margin-bottom: 0px !important;">
  <img width="600" src="https://user-images.githubusercontent.com/88351465/234432834-576d8445-c018-44c8-a48b-d445ba9be423.png" alt="" align="center">
</p>
<p align="center" >Figura 21. Boxplot BostonHousing Ridge CV Rsquared y RMSE</p>

<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/235268251-26640dc3-c67c-48ca-a2ea-5c5cd6daa1b7.png" alt="" align="center">
</p>
<p align="center" >Figura 22. Metricas de Ridge CV obtenidas de BostonHousing</p>


#### Evaluación Lasso regression de BostonHousing

-	Lasso Regression utilizando `medv` como variable dependiente y demás variables como independientes, con 10-fold cross validation. Con 50 valores de lambda tomando valores desde 0.0001 hasta 1. 




<p align="center" style="margin-bottom: 0px !important;">
  <img width="300" src="https://user-images.githubusercontent.com/88351465/234433555-a5d43091-c10f-4316-b1b6-aafea51ed786.png" alt="" align="center">
</p>
<p align="center" >Figura 23. Resultados de Lasso CV regression BostonHousing</p>

<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/234614524-e4eb4a64-be20-44c8-b98e-d76e6e77ccbb.png" alt="" align="center">
</p>
<p align="center" >Figura 24. Plot mejor prediccion de Lasso BostonHousing</p>


<p align="center" style="margin-bottom: 0px !important;">
  <img width="600" src="https://user-images.githubusercontent.com/88351465/234433634-cc620986-17a7-4bf1-990e-25d8b528ccfe.png" alt="" align="center">
</p>
<p align="center" >Figura 25. Boxplot BostonHousing Lasso CV Rsquared y RMSE</p>

<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/235268315-e2bda4d3-0e13-4262-b83f-f8a8e24112cb.png" alt="" align="center">
</p>
<p align="center" >Figura 26. Metricas de Lasso CV obtenidas de BostonHousing</p>





#### Evaluación Catboost regression de BostonHousing

- Catboost Regression CON CROSS VALIDATION (10-FOLD), utilizando learning_rate=0.01(La tasa de aprendizaje, se utiliza para reducir el paso de gradiente.), iterations=500 (Número máximo de árboles que se pueden construir al resolver problemas de aprendizaje automático), depth=10 (profundidad del árbol), loss_function=”RMSE” (la métrica a utilizar). 


<p align="center" style="margin-bottom: 0px !important;">
  <img width="300" src="https://user-images.githubusercontent.com/88351465/234434153-289c7c94-f978-49c1-a626-09229a3c9364.png" alt="" align="center">
</p>
<p align="center" >Figura 27. Resultados de Catboost regression BostonHousing</p>

<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/234616682-02d3b233-8056-43e9-96b5-5c6ec6440e8f.png" alt="" align="center">
</p>
<p align="center" >Figura 28. Plot mejor prediccion de Catboost BostonHousing</p>



<p align="center" style="margin-bottom: 0px !important;">
  <img width="600" src="https://user-images.githubusercontent.com/88351465/234434472-f896ea57-0db6-4107-853f-a0db64e3df72.png" alt="" align="center">
</p>
<p align="center" >Figura 29. Boxplot BostonHousing Catboost Rsquared y RMSE</p>



<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/235268379-9d0fe3f6-cb53-4ef8-9426-6c834a1541b2.png" alt="" align="center">
</p>
<p align="center" >Figura 30. Metricas de Catboost CV obtenidas de BostonHousing</p>




 - Catboost regression CON CROSS VALIDATION (10-FOLD), utilizando learning_rate=0.01(La tasa de aprendizaje, se utiliza para reducir el paso de gradiente.), iterations=500 (Número máximo de árboles que se pueden construir al resolver problemas de aprendizaje automático), depth=10 (profundidad del árbol), loss_function=”RMSE” (la métrica a utilizar). `Medv` como variable dependiente y demás variables como independientes (excepto `tax`). 

<p align="center" style="margin-bottom: 0px !important;">
  <img width="300" src="https://user-images.githubusercontent.com/88351465/234434916-d7164d69-eaaf-4bcd-8fbe-bb2198d1f7b5.png" alt="" align="center">
</p>
<p align="center" >Figura 31. Resultados de Catboost CV w/o correlated variables regression BostonHousing</p>

<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/234619611-34453c8f-c4b5-4e53-8aa5-3d3c2cbc459e.png" alt="" align="center">
</p>
<p align="center" >Figura 32. Plot mejor prediccion de Catboost w/o corr variables BostonHousing</p>



<p align="center" style="margin-bottom: 0px !important;">
  <img width="600" src="https://user-images.githubusercontent.com/88351465/234435039-ee06bb32-7853-4c45-b97c-d6c80097df52.png" alt="" align="center">
</p>
<p align="center" >Figura 33. Boxplot BostonHousing Catboost CV w/o correlated variables Rsquared y RMSE</p>


<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/235268426-d64f2927-abc0-49b3-83b0-b922f9993ead.png" alt="" align="center">
</p>
<p align="center" >Figura 34. Metricas de Catboost CV w/o correlated variables obtenidas de BostonHousing</p>


### AmsterdamHousing dataset

#### Análisis de AmsterdamHousing

En primer lugar, el proyecto incluye una sección de instalación e importación de las librerías a utilizar. 
A continuación se procedió a cargar el dataset "AmsterdamHousing", que incluye datos de viviendas de Amsterdam. Los datos originales son 924 observaciones sobre 8 variables, siendo Price la variable objetivo. Las variables son: 

- `X1`: numero de fila
- `Address`: direccion
- `Zip`: codigo postal
- `Price`: precio
- `Area`: Superficie residencial en metros cuadrados.
- `Room`: Cantidad de habitaciones    
- `Lon`
- `Lat`

El siguiente paso fue comprobar si el dataset tenía valores faltantes, lo cual habría modificado los resultados finales. Se encontraron 4 NA y se eliminaron esos registros. Se eliminaron las columnas de id, Zip y address ya que no fueron consideradas relevantes para el proyecto. 


Luego se realizó boxplot de las variables con el fin de encontrar valores outliers. 

<p align="center" style="margin-bottom: 0px !important;">
  <img width="400" src="https://user-images.githubusercontent.com/88351465/234599076-8c4c5cc2-4421-478f-a87a-586b21ccaad2.png"  align="center">
</p>
<p align="center" >Figura 35. Boxplot de variables de AmsterdamHousing</p>


Luego se procedió a analizar el Correlation plots, el cual es un una buena manera de explorar los datos y examinar el nivel de interacción entre las variables. Utilizando corrplot es posible obtener el gráfico presentado en la imagen 36 *Correlation plot de AmsterdamHousing* : 

<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/234595450-977ebe04-5b04-4b14-b1c2-12cbbf20bf43.png"  align="center">
</p>
<p align="center" >Figura 36. Correlation plot de AmsterdamHousing</p>

Analizando la figura 36 *Correlation plot de AmsterdamHousing* se observa que todas las variables representan correlación positiva. 

También fue importante el uso de la funcion `findCorrelation` de Caret  que evalúa las correlaciones entre pares de todas las variables, marcando las variables que están muy correlacionadas. De los pares identificados, la función recomienda la eliminación de la variable con la correlación absoluta media más alta en todo el conjunto de datos. La recomendación fue eliminar la columna `Area`. 

A continuación se dividió el dataset en train y test, y teniendo en cuenta el análisis general realizado,  se comenzó con la implementación de los modelos. 


#### Evaluación linear regression de AmsterdamHousing

- Linear Regression Cross validation 10-fold utilizando `Price` como variable dependiente y demás variables como independientes. 

<p align="center" style="margin-bottom: 0px !important;">
  <img width="300" src="https://user-images.githubusercontent.com/88351465/234584961-22d5dcae-b4b4-429a-8ed4-18a8affc6942.png" alt="" align="center">
</p>
<p align="center" >Figura 37. Resultados Linear CV AmsterdamHousing</p>

<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/233480190-d0a8ae23-8da4-4e1f-b5f1-2b468fd613a3.png" alt="" align="center">
</p>
<p align="center" >Figura 38. Plot mejor predicción de Linear AmsterdamHousing</p>


<p align="center" style="margin-bottom: 0px !important;">
  <img width="600" src="https://user-images.githubusercontent.com/88351465/234585286-c00117c7-79b9-4c62-a256-a57999bf81c7.png" alt="" align="center">
</p>
<p align="center" >Figura 39. Boxplot AmsterdamHousing Linear CV Rsquared y RMSE</p>

<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/235268800-1fd1585e-38ec-4ad8-ad50-f0797ce1df56.png" alt="" align="center">
</p>
<p align="center" >Figura 40. Metricas de Linear CV obtenidas de AmsterdamHousing</p>

#### Evaluación Ridge regression de AmsterdamHousing
- Ridge Regression utilizando `Price` como variable dependiente y demás variables como independientes, con 10-fold cross validation. Con 50 valores de lambda tomando valores desde 0.0001 hasta 1. 



<p align="center" style="margin-bottom: 0px !important;">
  <img width="300" src="https://user-images.githubusercontent.com/88351465/234586766-a540034b-275b-4f72-b612-c8ace202ad12.png" alt="" align="center">
</p>
<p align="center" >Figura 41. Resultados Ridge CV AmsterdamHousing</p>

<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/233480300-1fe046cc-894d-4413-9442-d91d50fa62eb.png" alt="" align="center">
</p>
<p align="center" >Figura 42. Plot mejor predicción de Ridge AmsterdamHousing</p>


<p align="center" style="margin-bottom: 0px !important;">
  <img width="600" src="https://user-images.githubusercontent.com/88351465/234586981-177b0691-594b-493c-8a77-78adcdf67270.png" alt="" align="center">
</p>
<p align="center" >Figura 43. Boxplot AmsterdamHousing Ridge CV Rsquared y RMSE</p>

<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/235268893-afc11751-fd17-4a14-9d22-3e8ec3fcaae7.png" alt="" align="center">
</p>
<p align="center" >Figura 44. Metricas de Ridge CV obtenidas de AmsterdamHousing</p>


#### Evaluación Lasso regression de AmsterdamHousing

- Lasso Regression utilizando `Price` como variable dependiente y demás variables como independientes, con 10-fold cross validation. Con 50 valores de lambda tomando valores desde 0.0001 hasta 1. 



<p align="center" style="margin-bottom: 0px !important;">
  <img width="300" src="https://user-images.githubusercontent.com/88351465/234587616-af56947b-a538-4dc8-9e43-3b4c0b2edcdf.png" alt="" align="center">
</p>
<p align="center" >Figura 45. Resultados Lasso CV AmsterdamHousing</p>

<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/233480369-2828cab7-8f56-463e-8c6e-c416107598f8.png" alt="" align="center">
</p>
<p align="center" >Figura 46. Plot mejor prediccion de Lasso  AmsterdamHousing</p>

<p align="center" style="margin-bottom: 0px !important;">
  <img width="600" src="https://user-images.githubusercontent.com/88351465/234587778-a0c605a7-bc56-4816-9482-af892157bca8.png" alt="" align="center">
</p>
<p align="center" >Figura 47. Boxplot AmsterdamHousing Lasso CV Rsquared y RMSE</p>

<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/235268968-7e9a15f6-d529-437e-8478-f338c7637afe.png" alt="" align="center">
</p>
<p align="center" >Figura 48. Metricas de Lasso CV obtenidas de AmsterdamHousing</p>

#### Evaluación Catboost regression de AmsterdamHousing

- Catboost regression utilizando `Price` como variable dependiente y demás variables como independientes. CON CROSS VALIDATION (10-FOLD), utilizando learning_rate=0.01(La tasa de aprendizaje, se utiliza para reducir el paso de gradiente.), iterations=500 (Número máximo de árboles que se pueden construir al resolver problemas de aprendizaje automático), depth=10 (profundidad del árbol), loss_function=”RMSE” (la métrica a utilizar).


<p align="center" style="margin-bottom: 0px !important;">
  <img width="300" src="https://user-images.githubusercontent.com/88351465/234588759-208d7145-ddff-4865-9a81-69441581b76a.png" alt="" align="center">
</p>
<p align="center" >Figura 49. Resultados Catboost CV AmsterdamHousing</p>

<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/233480401-3cd773ff-2866-4b02-ab9d-0155c753f11d.png" alt="" align="center">
</p>
<p align="center" >Figura 50. Plot mejor predicción de Catboost  AmsterdamHousing</p>

<p align="center" style="margin-bottom: 0px !important;">
  <img width="600" src="https://user-images.githubusercontent.com/88351465/234588990-234f5b40-bbc5-4393-8abd-37fb84433e91.png" alt="" align="center">
</p>
<p align="center" >Figura 51. Boxplot AmsterdamHousing Catboost CV Rsquared y RMSE</p>


<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/235269009-c6191545-00c7-4a4a-b612-f20ccb6d1778.png" alt="" align="center">
</p>
<p align="center" >Figura 52. Metricas de Catboost CV obtenidas de AmsterdamHousing</p>



### KingCounty Housing

#### Análisis de KingCounty

En primer lugar, el proyecto incluye una sección de instalación e importación de las librerías a utilizar. 
Luego se procedió a cargar el dataset KingCounty, que incluye 21613 datos de viviendas de King County. Las variables que incluye son:  

- `id` : A notation for a house

- `date`: Date house was sold

- `price`: Price is prediction target

- `bedrooms`: Number of bedrooms

- `bathrooms`: Number of bathrooms

- `sqft_living`: Square footage of the home (Metros cuadrados de la vivienda)

- `sqft_lot`: Square footage of the lot (Metros cuadrados de la parcela)

- `floors` :Total floors (levels) in house

- `waterfront` :House which has a view to a waterfront

- `view`: Has been viewed

- `condition` :How good the condition is overall

- `grade`: overall grade given to the housing unit, based on King County grading system

- `sqft_above `: Square footage of house apart from basement (Metros cuadrados de la casa aparte del sótano)

- `sqft_basement`: Square footage of the basement (Metros cuadrados del sótano)

- `yr_built` : Built Year

- `yr_renovated`: Year when house was renovated

- `zipcode`: Zip code

- `lat`: Latitude coordinate

- `long`: Longitude coordinate

- `sqft_living15` : Living room area in 2015(implies-- some renovations) This might or might not have affected the lotsize area

- `sqft_lot15` : LotSize area in 2015(implies-- some renovations)

Ejecutando `summary` del dataset obtenemos estadísticas básicas del mismo, por ejemplo la media, promedio, 1st quartile, etc.

<p align="center" style="margin-bottom: 0px !important;">
  <img width="1000" src="https://user-images.githubusercontent.com/88351465/234643261-2fd74b4b-8dae-4f0b-a752-6f9e512432ee.png"  align="center">
</p>
<p align="center" >Figura 53. `Summary` de KingCounty</p>


El siguiente paso fue comprobar si el dataset tenía valores faltantes, lo cual habría modificado los resultados finales. En este caso no se encontraron valores faltantes. Se eliminaron las columnas de `id` y `date` ya que no fueron consideradas relevantes para el proyecto. Y generamos una variable `age` (antiguedad). 

A continuación se presenta el Correlation plots, lo cual es un una buena manera de explorar los datos y examinar el nivel de interaccion entre las variables.
<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/234642279-e4fc9049-d6f4-43cb-96b9-f05b271acda9.png"  align="center">
</p>
<p align="center" >Figura 54. Correlation plot de KingCounty</p>


También fue importante el uso de la funcion `findCorrelation` de Caret  que evalúa las correlaciones entre pares de todas las variables, marcando las variables que están muy correlacionadas. De los pares identificados, la función recomienda la eliminación de la variable con la correlación absoluta media más alta en todo el conjunto de datos. La recomendación fue eliminar la columna `sqft_living`. 

Luego se procedió a dividir el dataset en train y test, y teniendo en cuenta el análisis general realizado,  se comenzó con la implementación de los modelos. 

#### Evaluación linear regression de KingCounty


- Linear regression cross validation (10-fold) utilizando `price` como variable dependiente y demás variables como independientes. 

<p align="center" style="margin-bottom: 0px !important;">
  <img width="300" src="https://user-images.githubusercontent.com/88351465/234430191-35050710-1ac6-49db-bbad-828562259c93.png" alt="" align="center">
</p>
<p align="center" >Figura 55. Resultados de Linear CV regression KingCounty</p>


<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/233667448-daad70d0-b051-4041-99f2-bfbc2e45d35d.png" alt="" align="center">
</p>
<p align="center" >Figura 56. Plot mejor predicción de Linear KingCounty</p>

<p align="center" style="margin-bottom: 0px !important;">
  <img width="600" src="https://user-images.githubusercontent.com/88351465/234430334-13afabe1-0ddd-4a04-ac58-8d6e5e703f1b.png" alt="" align="center">
</p>
<p align="center" >Figura 57. Boxplot KingCounty LinearCV Rsquared y RMSE</p>

<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/235269058-0de59612-30fa-40ed-b083-15896bc33022.png" alt="" align="center">
</p>
<p align="center" >Figura 58. Metricas de Linear CV obtenidas de KingCounty</p>



#### Evaluación Ridge regression de KingCounty
- Ridge Regression utilizando `price` como variable dependiente y demás variables como independientes, con 10-fold cross validation. Con 50 valores de lambda tomando valores desde 0.0001 hasta 1. 


<p align="center" style="margin-bottom: 0px !important;">
  <img width="300" src="https://user-images.githubusercontent.com/88351465/234429499-6bcdafc5-5be5-4644-8798-169ee3d6476b.png" alt="" align="center">
</p>
<p align="center" >Figura 59. Resultados de Ridge regression KingCounty</p>

<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/233667736-9f5f363a-74d3-43e1-97d3-25da4572c8c9.png" alt="" align="center">
</p>
<p align="center" >Figura 60. Plot mejor predicción de Ridge KingCounty</p>


<p align="center" style="margin-bottom: 0px !important;">
  <img width="600" src="https://user-images.githubusercontent.com/88351465/234429917-bbe79ffb-9a3c-46d4-80fe-f19bbf1b439b.png" alt="" align="center">
</p>
<p align="center" >Figura 61. Boxplot KingCounty Ridge Rsquared y RMSE</p>

<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/235269093-cc8859b3-23d9-4a49-aa42-6d9331192a62.png" alt="" align="center">
</p>
<p align="center" >Figura 62. Metricas de Ridge CV obtenidas de KingCounty</p>


#### Evaluación Lasso regression de KingCounty
- Lasso Regression utilizando `price` como variable dependiente y demás variables como independientes, con 10-fold cross validation. Con 50 valores de lambda tomando valores desde 0.0001 hasta 1. 


<p align="center" style="margin-bottom: 0px !important;">
  <img width="300" src="https://user-images.githubusercontent.com/88351465/234428706-f4091122-918d-49ca-8cb1-eb7a0c7ce8d3.png" alt="" align="center">
</p>
<p align="center" >Figura 63. Resultados de Lasso regression KingCounty</p>

<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/233667879-5429d85b-5cab-4737-84d6-b6df018145f7.png" alt="" align="center">
</p>
<p align="center" >Figura 64. Plot mejor predicción de Catboost KingCounty</p>


<p align="center" style="margin-bottom: 0px !important;">
  <img width="600" src="https://user-images.githubusercontent.com/88351465/234428937-723b3685-8c78-4942-a948-2dc070c89498.png" alt="" align="center">
</p>
<p align="center" >Figura 65. Boxplot KingCounty Lasso Rsquared y RMSE</p>


<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/235269139-cd7ddc4a-5f1e-4e98-8db9-a8c871a8fda2.png" alt="" align="center">
</p>
<p align="center" >Figura 66. Metricas de Lasso CV obtenidas de KingCounty</p>


#### Evaluación Catboost regression de KingCounty


- Catboost regression utilizando `price` como variable dependiente y demás variables como independientes. CON CROSS VALIDATION (10-FOLD), utilizando learning_rate=0.01(La tasa de aprendizaje, se utiliza para reducir el paso de gradiente.), iterations=500 (Número máximo de árboles que se pueden construir al resolver problemas de aprendizaje automático), depth=10 (profundidad del árbol), loss_function=”RMSE” (la métrica a utilizar).

<p align="center" style="margin-bottom: 0px !important;">
  <img width="300" src="https://user-images.githubusercontent.com/88351465/234427752-d781ce13-f07e-449d-b907-6a73210679c4.png" alt="" align="center">
</p>
<p align="center" >Figura 67. Resultados de Catboost KingCounty</p>


<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/233668001-b4a9b330-89bf-411b-ada9-e9635c4efb7e.png" alt="" align="center">
</p>
<p align="center" >Figura 68. Plot mejor predicción de Catboost KingCounty</p>


<p align="center" style="margin-bottom: 0px !important;">
  <img width="600" src="https://user-images.githubusercontent.com/88351465/234427969-ea35bbb4-78db-406f-9825-dbcdd7bb3df0.png" alt="" align="center">
</p>
<p align="center" >Figura 69. Boxplot KingCounty Catboost Rsquared y RMSE</p>


<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/235269175-fbfe606a-75a0-4eac-8db8-554e7832da53.png" alt="" align="center">
</p>
<p align="center" >Figura 70. Metricas de Catboost CV obtenidas de KingCounty</p>


- Catboost regression utilizando `price` como variable dependiente y demas variables como independientes (EXCEPTO LAS VARIABLES CON ALTA CORRELACION). CON CROSS VALIDATION (10-FOLD), utilizando learning_rate=0.01(La tasa de aprendizaje, se utiliza para reducir el paso de gradiente.), iterations=500 (Número máximo de árboles que se pueden construir al resolver problemas de aprendizaje automático), depth=10 (profundidad del árbol), loss_function=”RMSE” (la métrica a utilizar).


<p align="center" style="margin-bottom: 0px !important;">
  <img width="300" src="https://user-images.githubusercontent.com/88351465/234426720-f8a8b888-c10b-4574-b58c-98e62161d583.png" alt="" align="center">
</p>
<p align="center" >Figura 71. Resultados de Catboost without correlated variables KingCounty</p>



<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/234664718-8705c047-0f04-477c-aef6-d5a70de596e6.png" alt="" align="center">
</p>
<p align="center" >Figura 72. Plot mejor predicción de Catboost KingCounty</p>


<p align="center" style="margin-bottom: 0px !important;">
  <img width="600" src="https://user-images.githubusercontent.com/88351465/234428117-af929cee-1e34-46a8-9c04-3450df893f49.png" alt="" align="center">
</p>
<p align="center" >Figura 73. Boxplot KingCounty Catboost without correlated Rsquared y RMSE</p>


<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://user-images.githubusercontent.com/88351465/235269223-9975aa7b-6a19-45be-a7bc-796673f1a05a.png" alt="" align="center">
</p>
<p align="center" >Figura 74. Metricas de Catboost w/o correlated variables CV obtenidas de KingCounty</p>


## Análisis y discusión de resultados

### BostonHousing

**Presentación de resultados BostonHousing**

<p align="center" style="margin-bottom: 0px !important;">
  <img width="600" src="https://user-images.githubusercontent.com/88351465/234873927-c0e1a1c8-2f10-41d9-b239-27104fd47658.png" alt="" align="center">
</p>
<p align="center" >Figura 75. Resultados de métricas de BostonHousing</p>

<p align="center" style="margin-bottom: 0px !important;">
  <img width="600" src="https://user-images.githubusercontent.com/88351465/235272614-7c6dcce5-aee2-4131-98b8-38a79310387a.png" alt="" align="center">
</p>
<p align="center" >Figura 76. Boxplot resultados finales Rsquared de BostonHousing</p>

<p align="center" style="margin-bottom: 0px !important;">
  <img width="600" src="https://user-images.githubusercontent.com/88351465/235272710-3099099b-5c9e-46ba-bbe8-6c02c386e134.png" alt="" align="center">
</p>
<p align="center" >Figura 77. Boxplot resultados finales RMSE de BostonHousing</p>


**Análisis**

Recordando del marco teórico, un RMSE bajo presenta mejor performance frente a un RMSE alto. Por otro lado un R2 mayor presenta mejor performance frente a un R2 menor. Teniendo en cuenta lo mencionado, es posible comparar las métricas obtenidas analizando la figura 75 *Resultados de métricas de BostonHousing*:

Comparando la métrica de RMSE, el modelo de menor performance es aquel que obtuvo mayor valor de promedio, es decir, Linear CV con promedio de 4.820555. A continuación le sigue Lasso CV con valor promedio de 4.796933 y destacable que obtuvo el menor valor de desviación estándar, lo cual indica que es el modelo que obtuvo más datos cercanos al promedio. Analizando su gráfico de caja *Boxplot BostonHousing Lasso CV Rsquared y RMSE*, podemos ver que su mediana se sitúa aproximadamente en el centro, lo cual indicaría que su mediana y media coinciden aproximadamente. Por otro lado Ridge CV presenta promedio de RMSE menor (4.751065) pero una desviación estándar mayor 0.8642813, es decir que la distribución de los datos no se encuentran cercanos a la media. Su grafico de caja *Boxplot BostonHousing Lasso CV Rsquared y RMSE* presenta una mediana baja, lo cual indica que hay una cantidad favorable de datos que se sitúan en los valores inferiores. Finalmente los últimos valores presentados son de Catboost, donde el modelo de mejor performance fue Catboost CV w/o correlated variables, el cual obtuvo menor promedio de RMSE 3.529282. Nuevamente analizando su grafico de cajas *Boxplot BostonHousing Catboost CV w/o correlated variables Rsquared y RMSE* se observa que su mediana es baja, es decir, representa una distribución ‘asimétrica positiva’ lo cual indica que la mayoría de sus valores son bajos. 

Comparando la métrica Rsquared, el modelo de menor performance es aquel que obtuvo menor valor de promedio, es decir LassoCV con promedio de 0.732074. A continuación le siguen aproximadamente cerca los modelos Linear CV (promedio 0.7410739) y Ridge CV (promedio 0.7550372). Importante mencionar que el grafico de cajas *Boxplot BostonHousing Linear CV Rsquared y RMSE* presenta una distribución 'asimétrica negativa', es decir la mayoría de valores son superiores, lo cual podría deberse a un valor atípico inferior.
Finalmente los modelos de Catboost presentan la mejor performance comparando Rsquared, donde el mejor modelo comparando todos fue Catboost CV w/o correlated variables con promedio de 0.8953902 y desviación estándar baja, lo cual indica que gran mayoría de valores son representados por la media. En su grafico de cajas *Boxplot BostonHousing Catboost CV w/o correlated variables Rsquared y RMSE* es observable que su mediana presenta una distribución 'asimétrica negativa' con algún valor atípico.


### AmsterdamHousing

**Presentación de resultados AmsterdamHousing** 

<p align="center" style="margin-bottom: 0px !important;">
  <img width="600" src="https://user-images.githubusercontent.com/88351465/234874257-0c4a058d-7d82-4a4c-a16b-be9de7d89403.png" alt="" align="center">
</p>
<p align="center" >Figura 78. Resultados de métricas de AmsterdamHousing</p>


<p align="center" style="margin-bottom: 0px !important;">
  <img width="600" src="https://user-images.githubusercontent.com/88351465/235273025-caf0a361-1acc-48ca-9729-c690996e19b5.png" alt="" align="center">
</p>
<p align="center" >Figura 79. Boxplot resultados finales Rsquared de AmsterdamHousing</p>


<p align="center" style="margin-bottom: 0px !important;">
  <img width="600" src="https://user-images.githubusercontent.com/88351465/235272876-681a2607-e224-45ee-a02c-bd5e4df0bbcd.png" alt="" align="center">
</p>
<p align="center" >Figura 80. Boxplot resultados finales RMSE de AmsterdamHousing</p>


**Análisis**

Comparando la métrica de RMSE, el modelo de menor performance es aquel que obtuvo mayor valor de promedio, es decir, Linear CV con promedio de 276282.8. A continuación le sigue RidgeCV con valor promedio de 275627. Por otro lado Lasso CV presenta promedio de RMSE menor (272000.2). Su grafico de caja *Boxplot BostonHousing Lasso CV Rsquared y RMSE* es similar al de Linear CV y Catboost CV, los cuales presentan una mediana baja (distribución ‘asimétrica positiva’), lo cual indicaría que hay una cantidad favorable de datos que se sitúan en los valores inferiores. Finalmente los últimos valores presentados son de Catboost, que presenta mejor performance con menor promedio de RMSE 245764.4. 

Comparando la métrica Rsquared, el modelo de menor performance es aquel que obtuvo menor valor de promedio, es decir LassoCV con promedio de 0.6847414 y mayor valor de desviación estándar 0.1886495. A continuación le siguen aproximadamente cerca los modelos Linear CV (promedio 0.7030398) y Ridge CV (promedio 0.712939). 
Finalmente el modelo de Catboost presenta la mejor performance comparando Rsquared, con promedio de 0.8231122 y desviación estándar baja 0.0720727, lo cual indica que gran mayoría de valores son representados por la media. En su grafico de cajas *Boxplot AmsterdamHousing Catboost CV Rsquared y RMSE* es observable ver que su mediana se sitúa aproximadamente en el centro, lo cual indicaría que su mediana y media son aproximadamente similares.


### KingCountyHousing

**Presentación de resultados KingCountyHousing**

<p align="center" style="margin-bottom: 0px !important;">
  <img width="600" src="https://user-images.githubusercontent.com/88351465/234874797-434dd9f0-de10-4195-a097-078be6b937ed.png" alt="" align="center">
</p>
<p align="center" >Figura 77. Resultados de metricas de KingCountyHousing</p>

**Análisis**


Comparando la métrica de RMSE, el modelo de menor performance es aquel que obtuvo mayor valor de promedio, es decir, Ridge CV con promedio de 215917. A continuación le sigue LassoCV con valor promedio de 214933.1, su grafico de caja *Boxplot BostonHousing Lasso CV Rsquared y RMSE* muestra una amplia distribución de valores de RMSE con una mediana situada aproximadamente en el centro. Por otro lado Linear CV presenta promedio de RMSE menor (214599.9). Finalmente los últimos valores presentados son de Catboost, por un lado Catboost CV w/o correlated variables presenta valor promedio de RMSE de 166747.4 y Catboost CV promedio de 149384.6. Comparando todos los modelos con respecto a la métrica RMSE, es observable ver que el de mejor performance es Catboost CV. 

Comparando la métrica Rsquared, el modelo de menor performance es aquel que obtuvo menor valor de promedio, es decir Ridge CV con promedio de 0.6463276 aunque presenta el menor valor de desviación estándar 0.01500145. A continuación le siguen aproximadamente cerca los modelos Lasso CV (promedio 0.6495735) y Linear CV (promedio 0.6500709). 
Finalmente los modelos de Catboost presentan la mejor performance comparando Rsquared, donde el mejor modelo comparando todos fue Catboost CV con promedio de 0.8470585 y desviación estándar de 0.01838136, lo cual indica que gran mayoría de valores son representados por la media. 

# Conclusiones finales

## Análisis general 
Comparando los resultados obtenidos, se observa que linear regression es generalmente el modelo de menor precisión. Podría considerarse como el modelo de entrada a la hora de aplicar regresión lineal. Es útil para obtener resultados base o iniciales de un proyecto/investigación, a partir de estos podremos obtener mejores resultados. Aplicando ridge y lasso regression se obtendrían resultados con mayor precisión (en general resultados muy similares entre ambos). En todos los modelos aplicados a lo largo del proyecto, el mejor modelo con mayor precisión (considerando Rsquared) fue Catboost. El mismo obtuvo los mejores resultados y con amplia ventaja comparándolo con linear regression. Estos mejores resultados obtenidos por Catboost vienen condicionados por la cantidad de parámetros a modificar, como también por la cantidad de recursos de cómputo que utiliza. La mayor cantidad de tiempo de procesamiento pertenece a los modelos de catboost. 



## Análisis personal
En conclusión a la hora de implementar los modelos, el modelo linear regresión no presento grandes dificultades más que aprender cómo es la sintaxis en el lenguaje de programación elegido, en este caso en R. Lasso y ridge regression presentaron dificultades a la hora de entender cómo funcionaban y se implementaban. Por otro lado con respecto a Catboost fue un caso totalmente distinto. Catboost cuenta con gran cantidad de parámetros a modificar, y considero que cuenta con poca documentación y aplicaciones de ejemplo. Hay poco soporte/documentación de problemas de regresión lineal aplicados con catboost, específicamente en R. Esto fue un buen incentivo para realizar investigación de posibles soluciones a los problemas que se presentaron a lo largo del proyecto.   
