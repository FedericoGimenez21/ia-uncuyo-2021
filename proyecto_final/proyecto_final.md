# Introducción

Mediante el presente trabajo se pretende investigar y aprender técnicas de inteligencia artificial que no hayan sido vistas durante el cursado de la materia y aplicarlas en un caso práctico el cual será: a partir de un conjunto de datos referentes al mercado inmobiliario crear un modelo y entrenarlo. 
Una vez conseguido un buen ajuste, utilizaremos este modelo para predecir el precio de viviendas en esa área.

El objetivo principal del proyecto es expandir los conocimientos de machine learning investigando 3 posibles algoritmos a implementar, entre ellos, linear regression, glment y catboost.

En las siguientes secciones se explicarán todos aquellos conceptos teóricos utilizados por cada algoritmo y se explicarán las implementaciones para resolver el problema, así como comparaciones entre los distintos algoritmos aplicados. 

# Marco teórico

## Terminos importantes

Bias: Los sesgos son las suposiciones subyacentes que hacen los datos para simplificar la función objetivo. Los sesgos nos ayudan a generalizar mejor los datos y hacen que el modelo sea menos sensible a puntos de datos individuales. También reduce el tiempo de entrenamiento debido a la disminución de la complejidad de la función objetivo Un sesgo elevado sugiere que se asumen más suposiciones sobre la función objetivo. Esto conduce a veces a un ajuste insuficiente del modelo. Algunos ejemplos de algoritmos de sesgo alto son la regresión lineal, la regresión logística, etc.

Variance: En el aprendizaje automático, la varianza es un tipo de error que se produce debido a la sensibilidad de un modelo a pequeñas fluctuaciones en el conjunto de datos. Una varianza elevada haría que un algoritmo modelase los valores atípicos/ruido en el conjunto de entrenamiento. Esto se conoce como sobreajuste. En esta situación, el modelo básicamente aprende cada punto de datos y no ofrece una buena predicción cuando se prueba en un nuevo conjunto de datos. Algunos ejemplos de algoritmos de alta varianza son el árbol de decisión, KNN, etc.

![image](https://user-images.githubusercontent.com/88351465/228051759-5fa20141-391e-40e2-b644-a6cfe10aad01.png)
![image](https://user-images.githubusercontent.com/88351465/228051810-ceaacd40-0ddf-48b4-af2f-2a2a9695f41e.png)

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

Matemáticamente, podemos escribir esta relación lineal como
![image](https://user-images.githubusercontent.com/88351465/228034735-21d214a8-09cf-4943-83ee-02c1da9d981f.png)

Podemos leer "≈" como "se modela aproximadamente como" 

En conjunto, β0 y β1 se conocen como coeficientes o parámetros del modelo. Una vez que hemos utilizado nuestros
datos de entrenamiento para obtener las estimaciones βˆ0 y βˆ1 de los coeficientes del modelo, podemos predecir las ventas futuras en función de un valor concreto de la publicidad televisiva
calculando

![image](https://user-images.githubusercontent.com/88351465/228034991-73ce2857-6dba-4857-8ce9-b52a4192730f.png)

donde ˆy indica una predicción de Y sobre la base de X = x. Aquí utilizamos un símbolo de sombrero, ˆ , para denotar el valor estimado para un parámetro o coeficiente desconocido, o para denotar el valor predicho de la respuesta.

No todos los problemas pueden resolverse con el mismo algoritmo. En este caso, la regresión lineal supone que existe una relación lineal entre la variable de respuesta y las variables explicativas. Esto significa que se puede ajustar una línea entre las dos (o más variables).

![image](https://user-images.githubusercontent.com/88351465/228036888-d6d48b36-231b-4eec-936c-6b7f7aa19b2e.png)

El gráfico anterior presenta la relación lineal entre la variable de salida (y) y las variables predictoras (X).  La línea azul se denomina línea recta de mejor ajuste. A partir de los puntos de datos dados, intentamos trazar una línea que se ajuste lo mejor posible a los puntos.

Para calcular la recta de mejor ajuste, la regresión lineal utiliza una forma tradicional de pendiente-intersección que se indica a continuación,

Yi = β0 + β1Xi 

donde Yi = Variable dependiente, β0 = Intercepción, β1 = Pendiente, Xi = Variable independiente.
Este algoritmo explica la relación lineal entre la variable dependiente (output) Y y la variable independiente (predictor) X utilizando una línea recta Y= B0 + B1 X.

![image](https://user-images.githubusercontent.com/88351465/228037271-1e463a58-8ad9-4785-872c-aefc25aa6ba9.png)

Pero, ¿cómo averigua la regresión lineal cuál es la recta de mejor ajuste?
El objetivo del algoritmo de regresión lineal es obtener los mejores valores de B0 y B1 para encontrar la recta de mejor ajuste. La línea de mejor ajuste es una línea que tiene el menor error, lo que significa que el error entre los valores predichos y los valores reales debe ser mínimo.

Residuos
Una buena forma de comprobar la calidad del ajuste del modelo es observar los residuos o las diferencias entre los valores reales y los valores predichos. La línea recta de la imagen siguiente representa los valores previstos. La línea vertical roja que va de la línea recta al valor de los datos observados es el residuo.

![image](https://user-images.githubusercontent.com/88351465/228037812-0ae63623-167c-4003-80e1-94a6f45f1d70.png)

La idea es que la suma de los residuos sea aproximadamente cero o lo más baja posible. En la vida real, la mayoría de los casos no seguirán una línea perfectamente recta, por lo que es de esperar que haya residuos.

### ¿Qué es la recta de mejor ajuste?
En términos sencillos, la línea de mejor ajuste es una línea que se ajusta de la mejor manera al diagrama de dispersión dado. Matemáticamente, la línea de mejor ajuste se obtiene minimizando la suma residual de cuadrados (RSS).

La calidad del ajuste de una regresión lineal suele evaluarse mediante dos magnitudes relacionadas: el error estándar residual (RSE) y el estadístico R2. RSE: En términos generales, es la desviación media de la respuesta con respecto a la línea de regresión real. Se calcula mediante la fórmula:

![image](https://user-images.githubusercontent.com/88351465/228039774-549a2d0a-f6af-4179-bbe9-633ee7abb680.png)

Teniendo en cuenta que RSS es: 
![image](https://user-images.githubusercontent.com/88351465/228039870-d0b43267-aede-4610-8dca-a36912d4ddd4.png)

El RSE se considera una medida de la falta de ajuste del modelo a los datos. Si las predicciones obtenidas con el modelo se aproximan mucho a los verdaderos valores de los resultados -es decir, si ˆyi ≈ yi para i = 1,...,n-, el RSE será pequeño y podremos concluir que el modelo se ajusta muy bien a los datos. Por otro lado, si ˆyi está muy lejos de yi para una o más observaciones, entonces el RSE puede ser bastante grande, lo que indica que el modelo no se ajusta bien a los datos.

## GLMNET (Ridge Regression y Lasso Regression)

### Ridge Regression 
La Ridge regression es muy similar a la de mínimos cuadrados, salvo que los coeficientes de ridge regression se estiman minimizando una cantidad ligeramente diferente. En particular, las estimaciones de los coeficientes de regresión de cresta βˆR son los valores que minimizan

![image](https://user-images.githubusercontent.com/88351465/228047089-f5c18fe4-1cc8-405a-a1f9-85a3928f86e2.png)

donde λ ≥ 0 es un parámetro de ajuste, que se determinará por separado. 
El parámetro de ajuste λ sirve para controlar el impacto relativo de estos dos términos en las estimaciones del coeficiente de regresión. Cuando λ = 0, el término de penalización no tiene efecto, y la regresión ridge producirá las estimaciones por mínimos cuadrados. Sin embargo, a medida que λ → ∞, el impacto de la penalización por contracción crece, y las estimaciones del coeficiente de la regresión ridge se aproximarán a cero. 

Seleccionar un buen valor para λ es fundamental. Una opción óptima es probar un montón de valores para λ y utilizar la validación cruzada, para determinar cuál da lugar a la varianza más baja. 

¿Por qué la regresión Ridge es mejor que la de mínimos cuadrados?
La ventaja de la regresión Ridge sobre los mínimos cuadrados se basa en el equilibrio sesgo-varianza. A medida que aumenta λ, disminuye la flexibilidad del ajuste de ridge regression, lo que conduce a una disminución de la varianza pero a un aumento del sesgo.

### Lasso Regression 

Es una alternativa relativamente reciente a Ridge regression. Formula: 
![image](https://user-images.githubusercontent.com/88351465/228049230-f9f6a8e0-804b-4e0e-88ae-94eae70106b1.png)

vemos que la regresión lasso y la regresión ridge tienen formulaciones similares.

La única diferencia es que el término βj^2 en la regresión ridge
ha sido sustituido por |βj| en la penalización del lazo.
Al igual que en la regresión ridge, lasso reduce las estimaciones de los coeficientes hacia cero.

Lasso produce modelos más sencillos e interpretables en los que sólo interviene un subconjunto de predictores.

### Análisis comparativo de la regresión Lasso y Ridge
La regresión Ridge y Lasso utilizan dos funciones de penalización diferentes para la regularización. La regresión Ridge utiliza L2, mientras que la regresión Lasso utiliza la técnica de regularización L1. En la regresión ridge, la penalización es igual a la suma de los cuadrados de los coeficientes y en la Lasso, la penalización se considera la suma de los valores absolutos de los coeficientes. En la regresión lasso, es la contracción hacia cero utilizando un valor absoluto (penalización L1 o técnica de regularización) en lugar de una suma de cuadrados (penalización L2 o técnica de regularización).

### Selección del parámetro de ajuste

La implementación de la regresión ridge y el lazo requiere un método para seleccionar un valor para el parámetro de ajuste λ. La validación cruzada proporciona una forma sencilla de abordar este problema. Elegimos una cuadrícula de valores de λ y calculamos el error de validación cruzada para cada valor de λ. A continuación, seleccionamos el valor del parámetro de ajuste para el que el error de validación cruzada es menor. Por último, se vuelve a ajustar el modelo utilizando todas las observaciones disponibles y el valor seleccionado del parámetro de ajuste. 

![image](https://user-images.githubusercontent.com/88351465/228054986-c136aeca-847d-4815-af62-5af935a41db7.png)

> Izquierda: MSE de validación cruzada de diez veces para el lazo, aplicado al conjunto de datos simulados dispersos. Derecha: Se muestran las correspondientes estimaciones del coeficiente del lazo. Las dos variables de señal se muestran en color y las variables de ruido en gris. Las líneas verticales discontinuas indican el ajuste del lazo cuyo error de validación cruzada es menor.

## Bosting

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

lmData= lm([objetivo] ~ [predictor / características], datos = [fuente de datos])

Con el comando summary(lmData) se puede ver información detallada sobre el rendimiento y los coeficientes del modelo.

### Glmnet en R (regresión lasso y ridge)
Glmnet en R (regresión lasso y ridge)
Regresión Ridge - glmnet parámetro alpha=0 para la regresión ridge. Para predicción numérica elija familia - gaussiana, para clasificación familia = binomial, glmnet por defaut elige 100 valores lambda que dependen de los datos

l_ridge <- glmnet(x, y, family="gaussian", alpha=0)

Regresión Lasso - glmnet parámetro alpha=1 para regresión Lasso glmnet(x, y, alpha = 1)

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

### BostonHousing dataset

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

Plot: 

![image](https://user-images.githubusercontent.com/88351465/230802502-023d5783-69af-4d9b-9c05-6a92555f2a26.png)

Segunda ejecucion:

![image](https://user-images.githubusercontent.com/88351465/233804163-3dcddc9a-e255-4a26-801c-422e66bb834c.png)


-	Linear Regression, utilizando medv como variable dependiente y crim + rm + tax + lstat como variables independientes. 

 ![image](https://user-images.githubusercontent.com/88351465/230801597-43583cc5-2b82-48f1-abfd-355383eda9a8.png)

Plot: 

![image](https://user-images.githubusercontent.com/88351465/230802547-71588e5a-17c2-470e-8ac4-a0ed32e9fc3a.png)

Segunda ejecucion:

![image](https://user-images.githubusercontent.com/88351465/233804174-d7098fe5-d17b-41af-b966-4b8607569323.png)


-	Linear Regression, utilizando medv como variable dependiente y utilizando todas las variables excepto aquellas variables que son altamente correlacionadas ("indus" "nox"   "tax"   "dis"  ). 

 ![image](https://user-images.githubusercontent.com/88351465/230801607-3fef6248-b1c7-4172-bd5b-ef9d40cf8438.png)

Segunda ejecucion:
![image](https://user-images.githubusercontent.com/88351465/233804204-520d65a0-1587-4101-910a-5c04a5fd3b8e.png)


-	Linear Regression utilizando medv como variable dependiente y  las demás variables como independientes, con 10-fold cross validation. 

 ![image](https://user-images.githubusercontent.com/88351465/230801647-4a136e4e-86fc-4be3-82d9-5a77c8f8f8ac.png)

Plot: 

![image](https://user-images.githubusercontent.com/88351465/230802560-7a4fa001-99ef-4df4-91b8-b845910f8edc.png)

Segunda ejecucion: 

![image](https://user-images.githubusercontent.com/88351465/233804227-ecc453d5-55d0-4d2a-8965-02bb93b3f71a.png)

-	 Ridge Regression utilizando medv como variable dependiente y demás variables como independientes, con 10-fold cross validation. Con 50 valores de lambda tomando valores desde 0.0001 hasta 1. 

 ![image](https://user-images.githubusercontent.com/88351465/230801672-31d43a75-6115-4249-8fcd-5ce6d3bf5ca6.png)

Plot: 

![image](https://user-images.githubusercontent.com/88351465/230802606-1a35c80c-9e11-4245-a042-42f7f39d18da.png)

Segunda ejecucion: 

![image](https://user-images.githubusercontent.com/88351465/233804253-b446beb7-e1f6-41df-b593-91bcbccd0385.png)

-	Lasso Regression utilizando medv como variable dependiente y demás variables como independientes, con 10-fold cross validation. Con 50 valores de lambda tomando valores desde 0.0001 hasta 1. 

 ![image](https://user-images.githubusercontent.com/88351465/230801684-88ae8ca7-95aa-497b-8f3a-4fa9295f26c3.png)

Plot:

![image](https://user-images.githubusercontent.com/88351465/230802576-62f3aca3-d589-4f4a-b28c-747cbe618eaa.png)

Segunda ejecucion: 

![image](https://user-images.githubusercontent.com/88351465/233804260-1e22a3de-1e03-4025-984b-73c9167d4870.png)


-	Catboost Regression SIN CROSS VALIDATION, utilizando learning_rate=0.01(La tasa de aprendizaje, se utiliza para reducir el paso de gradiente.), iterations=500 (Número máximo de árboles que se pueden construir al resolver problemas de aprendizaje automático), depth=10 (profundidad del árbol), loss_function=”RMSE” (la métrica a utilizar). 

 ![image](https://user-images.githubusercontent.com/88351465/230801705-15763d94-3bf5-4d7a-b152-d53fbfd8b12d.png)
 
 Plot:
 
 ![image](https://user-images.githubusercontent.com/88351465/230802620-93c17efa-1e5e-4c22-b763-eb2aea9cb5e6.png)
 
Segunda ejecucion: 

![image](https://user-images.githubusercontent.com/88351465/233804290-95385c6c-233f-4f18-8319-543545bfb09a.png)

- Catboost Regression CON CROSS VALIDATION (10-FOLD), utilizando learning_rate=0.01(La tasa de aprendizaje, se utiliza para reducir el paso de gradiente.), iterations=500 (Número máximo de árboles que se pueden construir al resolver problemas de aprendizaje automático), depth=10 (profundidad del árbol), loss_function=”RMSE” (la métrica a utilizar). 

![image](https://user-images.githubusercontent.com/88351465/233804374-47fd137d-e960-4b4b-837e-1caa51376048.png)

Segunda ejecucion: 

![image](https://user-images.githubusercontent.com/88351465/233805855-1611f881-dc09-4fba-9a34-dea20cbd0d48.png)

Tercera ejecucion: 

![image](https://user-images.githubusercontent.com/88351465/233806306-ae0da62b-70b5-4d43-b0a4-21ab5a464816.png)


 - Catboost regression, utilizando learning_rate=0.01(La tasa de aprendizaje, se utiliza para reducir el paso de gradiente.), iterations=500 (Número máximo de árboles que se pueden construir al resolver problemas de aprendizaje automático), depth=10 (profundidad del árbol), loss_function=”RMSE” (la métrica a utilizar). Medv como variable dependiente y demas variables como independientes (excepto "tax"). 
 
 ![image](https://user-images.githubusercontent.com/88351465/233696539-78e0de63-20b0-405d-ad27-fdc5c8f1f699.png)

Plot: 

![image](https://user-images.githubusercontent.com/88351465/233696596-49299717-a0ab-408e-a956-b8eeb120507e.png)

Segunda ejecucion: 
![image](https://user-images.githubusercontent.com/88351465/233804300-8b885d44-2c2c-4d90-a0ef-3f3584d684f1.png)

 - Catboost regression CON CROSS VALIDATION (10-FOLD), utilizando learning_rate=0.01(La tasa de aprendizaje, se utiliza para reducir el paso de gradiente.), iterations=500 (Número máximo de árboles que se pueden construir al resolver problemas de aprendizaje automático), depth=10 (profundidad del árbol), loss_function=”RMSE” (la métrica a utilizar). Medv como variable dependiente y demas variables como independientes (excepto "tax"). 

![image](https://user-images.githubusercontent.com/88351465/233805840-e6724222-f49d-4f7f-b219-1007f3f45cfc.png)

Segunda ejecucion: 

![image](https://user-images.githubusercontent.com/88351465/233805984-ff138c21-3cef-4587-b81a-f0163f9d0d41.png)

Tercera ejecucion: 

![image](https://user-images.githubusercontent.com/88351465/233806278-44a86b81-5ac5-40c2-a4dc-ed6cfd4c8456.png)


### AmsterdamHousing dataset

En primer lugar, el proyecto incluye una seccion de instalacion e importacion de las librerias a utilizar. 
Luego se procedio a cargar el dataset AmsterdamHousing

El siguiente paso fue comprobar si el dataset tenia valores faltantes, lo cual habria modificado los resultados finales. Se encontraron 4 NA y se eliminaron esos registros. Elimine las columnas de id, Zip y address ya que no fueron consideradas relevantes para el proyecto. 

A continuacion analice el Correlation plots, lo cual es un una buena manera de explorar los datos y examinar el nivel de interaccion entre las variables. Tambien fue importante el uso de la funcion findCorrelation de Caret  que evalúa las correlaciones entre pares de todas las variables, marcando las variables que están muy correlacionadas. De los pares identificados, la función recomienda la eliminación de la variable con la correlación absoluta media más alta en todo el conjunto de datos. La recomendacion fue eliminar la columna "Area". 

Procedi a dividir el dataset en train y test, y teniendo en cuenta el analisis general realizado,  estaba en condiciones de implementar los modelos


A continuación se presentan los resultados de predicción de los modelos implementados: 
-	Linear Regression, utilizando Price como variable dependiente y demas variables como independientes. 

![image](https://user-images.githubusercontent.com/88351465/233479459-282bd19d-0382-4183-9edc-d53aec4ca590.png)


Plot: 

![image](https://user-images.githubusercontent.com/88351465/233480190-d0a8ae23-8da4-4e1f-b5f1-2b468fd613a3.png)

Segunda ejecucion: 

![image](https://user-images.githubusercontent.com/88351465/233859653-df12c574-4ae0-4d91-998f-42e0a84ecbf9.png)

- Cross validation utilizando Price como variable dependiente y demas variables como independientes. 

![image](https://user-images.githubusercontent.com/88351465/233479728-d888873b-5edf-46d3-b3be-d6e418d899e9.png)


- Ridge Regression utilizando Price como variable dependiente y demás variables como independientes, con 10-fold cross validation. Con 50 valores de lambda tomando valores desde 0.0001 hasta 1. 

![image](https://user-images.githubusercontent.com/88351465/233479852-a7bf61fb-6632-42cf-9560-f304e9f07a8e.png)

Plot: 

![image](https://user-images.githubusercontent.com/88351465/233480300-1fe046cc-894d-4413-9442-d91d50fa62eb.png)

Segunda ejecucion: 

![image](https://user-images.githubusercontent.com/88351465/233859564-6e66ee26-0311-48db-b041-000efb85d92b.png)

- Lasso Regression utilizando Price como variable dependiente y demás variables como independientes, con 10-fold cross validation. Con 50 valores de lambda tomando valores desde 0.0001 hasta 1. 

![image](https://user-images.githubusercontent.com/88351465/233479949-f55afa48-f732-4519-a8f9-7cf894eb79dc.png)

Plot: 

![image](https://user-images.githubusercontent.com/88351465/233480369-2828cab7-8f56-463e-8c6e-c416107598f8.png)

Segunda ejecucion: 

![image](https://user-images.githubusercontent.com/88351465/233859570-93ab4cc7-2e37-414b-a3c5-daac4c7a1363.png)


- Catboost regression utilizando Price como variable dependiente y demas variables como independientes.

![image](https://user-images.githubusercontent.com/88351465/233480016-6b6466f7-0bfa-4850-a6ba-18ac06b20f77.png)

Plot: 

![image](https://user-images.githubusercontent.com/88351465/233480401-3cd773ff-2866-4b02-ab9d-0155c753f11d.png)

Segunda ejecucion: 

![image](https://user-images.githubusercontent.com/88351465/233859583-2a7a6bae-eb3a-4a0a-ab65-d3b69497eb7b.png)

- Catboost regression utilizando Price como variable dependiente y demas variables como independientes. CON CROSS VALIDATION (10-FOLD), utilizando learning_rate=0.01(La tasa de aprendizaje, se utiliza para reducir el paso de gradiente.), iterations=500 (Número máximo de árboles que se pueden construir al resolver problemas de aprendizaje automático), depth=10 (profundidad del árbol), loss_function=”RMSE” (la métrica a utilizar).

Primera ejecucion: 

![image](https://user-images.githubusercontent.com/88351465/233859167-bae6ea9c-00fc-4dc8-b668-9b4c423f41bb.png)

Segunda ejecucion: 

![image](https://user-images.githubusercontent.com/88351465/233859592-516f4b9f-24e4-4603-a7ee-324c9cc9b77e.png)


### KingCounty Housing

En primer lugar, el proyecto incluye una seccion de instalacion e importacion de las librerias a utilizar. 
Luego se procedio a cargar el dataset KingCounty

El siguiente paso fue comprobar si el dataset tenia valores faltantes, lo cual habria modificado los resultados finales. En este caso no se encontraron valores faltantes. Elimine las columnas de id y date ya que no fueron consideradas relevantes para el proyecto. Transforme las variables "waterfront", "view", "condition" que tenian formato de num a factor. Y generar una variable age (antiguedad). 

A continuacion analice el Correlation plots, lo cual es un una buena manera de explorar los datos y examinar el nivel de interaccion entre las variables. Tambien fue importante el uso de la funcion findCorrelation de Caret  que evalúa las correlaciones entre pares de todas las variables, marcando las variables que están muy correlacionadas. De los pares identificados, la función recomienda la eliminación de la variable con la correlación absoluta media más alta en todo el conjunto de datos. La recomendacion fue eliminar la columna "sqft_living". 

Procedi a dividir el dataset en train y test, y teniendo en cuenta el analisis general realizado,  estaba en condiciones de implementar los modelos

-	Linear Regression, utilizando Price como variable dependiente y demas variables como independientes. 

![image](https://user-images.githubusercontent.com/88351465/233667344-a585ee88-7488-4bd1-8988-e77605860a07.png)

Plot: 

![image](https://user-images.githubusercontent.com/88351465/233667448-daad70d0-b051-4041-99f2-bfbc2e45d35d.png)

Segunda ejecucion: 

![image](https://user-images.githubusercontent.com/88351465/233860712-20f7ec52-3b9a-4fd6-b2ea-2969d5f95c3b.png)


- Cross validation utilizando Price como variable dependiente y demas variables como independientes. 

![image](https://user-images.githubusercontent.com/88351465/233667583-f8656290-9170-4e84-b7ec-25bfbde7e797.png)

Plot: 

![image](https://user-images.githubusercontent.com/88351465/233667628-69da359d-a71d-4490-b214-82ec0042f702.png)

- Ridge Regression utilizando price como variable dependiente y demás variables como independientes, con 10-fold cross validation. Con 50 valores de lambda tomando valores desde 0.0001 hasta 1. 

![image](https://user-images.githubusercontent.com/88351465/233667703-a817d050-c963-4688-9a3f-1a83e318a937.png)

Plot:

![image](https://user-images.githubusercontent.com/88351465/233667736-9f5f363a-74d3-43e1-97d3-25da4572c8c9.png)

Segunda ejecucion: 

![image](https://user-images.githubusercontent.com/88351465/233860671-fdee5c5b-582a-43d6-bea9-2b728b9f24b3.png)

Tercera ejecucion:

![image](https://user-images.githubusercontent.com/88351465/233861135-a670e90e-0eab-4411-8caf-5b17d004963f.png)


- Lasso Regression utilizando price como variable dependiente y demás variables como independientes, con 10-fold cross validation. Con 50 valores de lambda tomando valores desde 0.0001 hasta 1. 

![image](https://user-images.githubusercontent.com/88351465/233667823-e8cbc3cd-f979-4556-8072-2894a2b78f9b.png)

Plot:

![image](https://user-images.githubusercontent.com/88351465/233667879-5429d85b-5cab-4737-84d6-b6df018145f7.png)

Segunda ejecucion: 

![image](https://user-images.githubusercontent.com/88351465/233860662-504ea1c9-0cbc-4256-8f7b-8b09f99889ee.png)

Tercera ejecucion: 

![image](https://user-images.githubusercontent.com/88351465/233861123-9467d02b-e9e0-48df-a1e9-fdc9bb74c7a1.png)


- Catboost regression utilizando Price como variable dependiente y demas variables como independientes.

![image](https://user-images.githubusercontent.com/88351465/233667974-59e6bfca-feb9-48b9-94b2-7332bb541fa7.png)


Plot:

![image](https://user-images.githubusercontent.com/88351465/233668001-b4a9b330-89bf-411b-ada9-e9635c4efb7e.png)


Segunda ejecucion: 

![image](https://user-images.githubusercontent.com/88351465/233860639-97791f22-a91e-48fd-aaa4-1084b9a50331.png)

Tercera ejecucion:

![image](https://user-images.githubusercontent.com/88351465/233861100-c18dc12a-399e-400b-8a1d-084b01d886af.png)


- Catboost regression utilizando price como variable dependiente y demas variables como independientes. CON CROSS VALIDATION (10-FOLD), utilizando learning_rate=0.01(La tasa de aprendizaje, se utiliza para reducir el paso de gradiente.), iterations=500 (Número máximo de árboles que se pueden construir al resolver problemas de aprendizaje automático), depth=10 (profundidad del árbol), loss_function=”RMSE” (la métrica a utilizar).

![image](https://user-images.githubusercontent.com/88351465/233860335-2db6ee91-0d90-4237-ab8c-e5a79b9b65d0.png)

Segunda ejecucion: 

![image](https://user-images.githubusercontent.com/88351465/233860726-b0643a55-aaa1-4238-adb2-54e3cc6e1d6b.png)

Tercera ejecucion: 

![image](https://user-images.githubusercontent.com/88351465/233861083-affa9240-8609-4877-a8a9-b002fc6170b1.png)

## Análisis y discusión de resultados

### BostonHousing
Recordando del marco teórico, un RMSE bajo presenta mejor performance frente a un RMSE alto. Por otro lado un R2 mayor presenta mejor performance frente a un R2 menor. Teniendo en cuenta lo mencionado, podemos observar lo siguiente: 
El modelo que obtuvo menor performance, comparando las métricas de RMSE y Rsquared es Linear Regression. Aunque podemos ver que al aplicar cross validation obtenemos resultados muy similares a Lasso y Ridge regression (con cv). 
Por otro lado, el vencedor de los modelos es Catboost Regression con una notable mejora con un RMSE menor y un Rsquared mucho mayor (0.8808 aprox) frente al primer Rsquared obtenido por Linear regression (0.5945 aprox). Analizando los plots claramente el vencedor tambien es catboost. La prediccion refleja una curva que representa gran cantidad de los datos. 

Aun podemos mejorar mas la performance de catboost. Aplicando el modelo a medv como variable dependiente y demas variables como independientes (excepto "tax") claramente observamos una mejora muy alta. RMSE menor (2.0271471) y Rsquared de 0.9711059. 

Analizando todos los resultados observamos que el modelo de mejor performance es Catboost. Realizando 3 ejecuciones con cross validation, podemos ver que obtenemos mejores resultados con el modelo de Catboost con cross validation y sin la variable "tax", donde obtenemos valores de Rsquared maximos  y valores de RMSE minimos entre todos los resultados. 

### AmsterdamHousing
El modelo que obtuvo menor performance, comparando las métricas de RMSE y Rsquared es Linear Regression. Vemos una mejora al aplicar ridge y lasso regression. Y observando los resultados de catboost claramente obtenemos mejor performance, RMSE (323909) y Rsquared (0.7841589). Al aplicar cross validation a catboost obtenemos variedad de resultados, en los cuales encontramos los mayores valores de Rsquared y minimos valores de RMSE comparando todos los resultados.      

### KingCountyHousing

El modelo que obtuvo menor performance, comparando las métricas de RMSE y Rsquared es Linear Regression. Vemos una mejora al aplicar ridge y lasso regression. Nuevamente, observando los resultados de catboost obtenemos mejor performance, RMSE (146067.4) y Rsquared (0.8526002). Al aplicar cross validation a catboost observamos que los valores obtenidos por ejemplo de Rsquared varian entre 79% y 87% aproximadamente. Es decir, catboost realiza modelos mas precisos que lasso, ridge y linear regression. 


# Conclusiones finales
