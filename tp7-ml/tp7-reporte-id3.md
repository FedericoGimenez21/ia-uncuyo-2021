### Resultados sobre la evaluación sobre tennis.csv

![image](https://user-images.githubusercontent.com/88351465/140232008-4e1d02ea-726d-42dc-b82b-6163982d21c7.png)


### Información sobre las estrategias para datos de tipo real

Para aplicar arboles de decision utilizando datos de tipo real hay unos problemas que deben considerarse. Algunos de ellos son:

**Datos faltantes**: En varios dominios, no todos los valores de atributos seran conocidos para todo ejemplo. Es posible que los valores no hayan sido registrados o que haya sido muy costosos de obtener. Esto da lugar a dos problemas: primero, dado un árbol de decisión completo, ¿cómo se debe clasificar un objeto para el que no se conoce uno de sus atributos de test? Segundo, ¿cómo se debe modificar la fórmula de la ganancia de información cuando algunos ejemplos tienen valores desconocidos para cierto atributo?

**Atributos multivaluados**: cuando un atributo tiene muchos valores posibles, la ganancia de información proporciona una indicación inapropiada de su utilidad. En el caso extremo, se podría utilizar un atributo, como NombreRestaurante, que tenga un valor diferente para cada ejemplo. En este caso, cada subconjunto de ejemplos tendrá un único elemento con una única clasificación, por lo tanto la medida de ganancia de información tendrá su máximo valor para este atributo. Sin embargo, el atributo puede ser irrelevante o inútil. Una solución es utilizar el ratio de ganancia


**Atributos de entrada continuos de valor entero**: los atributos continuos de valor entero, como Altura o Peso, tienen un número infinito de valores posibles. Más que generar infinitas ramas, los algoritmos de aprendizaje del árbol de decisión típicamente encuentran el punto de ruptura (split point) que proporciona la máxima ganancia de información. Por ejemplo, en un nodo del árbol se puede dar el caso de que el test sobre Altura>160 proporcione la mayor información. Existen métodos de programación dinámica eficiente para encontrar puntos de ruptura, pero esta parte es, con diferencia, la más ineficiente de las aplicaciones reales de aprendizaje de árboles de decisión.


**Atributos de salida de valor continuo**: si intentamos predecir un valor numérico, como el precio de una obra de arte, más que una clasificación discreta necesitamos un árbol de regresión. Este tipo de árbol tiene en cada hoja una función lineal de algún subconjunto de atributos numéricos, en vez de un valor simple. Por ejemplo, la rama para grabados pintados a mano puede terminar con una función lineal del área, edad y número de colores. El algoritmo de aprendizaje debe decidir cuándo dejar de dividir para comenzar a aplicar regresión lineal utilizando los atributos restantes (o algún subconjunto).


**Un sistema de aprendizaje de árboles de decisión para aplicaciones reales debe ser capaz de manejar todos estos problemas. El manejo de variables de valor continuo es especialmente importante, porque tanto los procesos físicos como los financieros proporcionan datos numéricos.**
