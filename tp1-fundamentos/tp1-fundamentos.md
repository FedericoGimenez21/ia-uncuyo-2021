Licenciatura en Ciencias de la Computación

Universidad Nacional de Cuyo

Inteligencia Artificial 2021

Trabajo práctico 1 - Fundamentos

Alumno: Gimenez Federico 

**IA débil: ¿pueden las máquinas actuar con inteligencia?**

Algunos filósofos han intentado demostrar que la IA es imposible; que las máquinas no tendrán la posibilidad de actuar inteligentemente.

Obviamente, si la IA es imposible o no lo es, dependerá de cómo se defina. En esencia, la IA consiste en la búsqueda del mejor programa agente en una arquitectura dada. Con esta formulación, la IA es posible por definición: para cualquier arquitectura digital de k bits de almacenamiento existirán exactamente 2^k programas agente y todo lo que habrá que hacer para encontrar el mejor es enumerarlos y probar todos ellos. Esto podría no ser viable para una k grande, pero los filósofos abordan más la teoría que la práctica.

Alan Turing, en su famoso artículo «Computing Machinery and Intelligence» (Turing, 1950), sugirió que en vez de preguntar si las máquinas pueden pensar, deberíamos preguntar si las máquinas pueden aprobar un test de inteligencia conductiva (de comportamiento), conocido como el Test de Turing. La prueba se realiza para que el programa mantenga una conversación durante cinco minutos (mediante mensajes escritos en línea, online) con un interrogador (interlocutor). Éste tiene que averiguar si la conversación se está llevando a cabo con un programa o con una persona; si el programa engaña al interlocutor un 30 por ciento del tiempo, este pasará la prueba. Turing conjeturó que, hacia el año 2000, un computador con un almacenamiento de 10^(9) unidades podría llegar a programarse lo suficientemente bien como para pasar esta prueba, pero no estaba en lo cierto. Algunas personas han sido engañadas durante cinco minutos; por ejemplo, el programa ELIZA y el chatbot en Internet llamado MGONZ han engañado a personas ignorantes que no se daban cuenta de que estaban hablando con un programa; el programa ALICE engañó a un juez en la competición del Loebner Prize en el año 2001. Sin embargo, ningún programa se ha acercado al criterio del 30 por ciento frente a jueces con conocimiento, y el campo en su conjunto de la IA no ha prestado mucha atención a los tests de Turing. Turing también examinó una gran gama de posibles objeciones ante la posibilidad de las máquinas inteligentes, incluyendo virtualmente aquellas que han aparecido medio siglo después de que apareciera este artículo. Examinaremos algunas de ellas. 

*El argumento de incapacidad*

El «argumento de incapacidad» afirma que «una máquina nunca puede hacer X». Como ejemplos de X, Turing enumera las siguientes acciones:

Ser amable, tener recursos, simpático, tener iniciativas, tener sentido del humor, distinguir lo correcto de lo erróneo, cometer errores, enamorarse, hacer que otra persona también se enamore, aprender de la experiencia, utilizar palabras de forma adecuada, ser el tema de su propio pensamiento, tener tanta diversidad de comportamientos como el hombre, hacer algo realmente nuevo. 

Turing tuvo que utilizar su intuición para adivinar aquello que en un futuro sería posible, pero nosotros tenemos el privilegio de poder mirar hacia atrás y ver qué es lo que ya pueden hacer los computadores. Es innegable que los computadores actualmente hacen muchas cosas que anteriormente eran sólo del dominio humano. Los programas juegan al ajedrez, a las damas y a otros juegos, inspeccionan piezas de las líneas de producción, comprueban la ortografía en los documentos de los procesadores de texto, conducen coches y helicópteros, diagnostican enfermedades, y hacen otros cientos de tareas tan bien o mejor que los hombres. Los computadores han hecho pequeños pero significativos descubrimientos, en Astronomía, Matemáticas, Química, Mineralogía, Biología, Informática y otros campos que necesitan rendimiento a nivel de experto.

Es evidente que los computadores pueden hacer muchas cosas tan bien o mejor que el ser humano, incluso cosas que las personas creen que requieren mucha intuición y entendimiento humano. Por supuesto, esto no significa que los computadores utilicen la intuición y el entendimiento para realizar estas tareas, las cuales no forman parte del comportamiento, y afrontamos dichas cuestiones en otro sitio, sino que la cuestión es que la primera conjetura sobre los procesos mentales que se requieren para producir un comportamiento dado suele ser equivocada. También es cierto, desde luego, que existen todavía muchas tareas en donde los computadores no sobresalen (por no decirlo más bruscamente), incluida la tarea de Turing de mantener una conversación abierta.

*La objeción matemática*

Es bien conocido, a través de los trabajos de Turing (1936) y Gödel (1931), que ciertas cuestiones matemáticas, en principio, no pueden ser respondidas por sistemas formales concretos. El teorema de la incompletitud de Gödel es el ejemplo más conocido en este respecto. En resumen, para cualquier sistema axiomático formal F lo suficientemente potente como para hacer aritmética, es posible construir una «sentencia Gödel» G(F) con las propiedades siguientes:

  •G(F) es una sentencia de F, pero no se puede probar dentro de F. 
  
  • Si F es consistente, entonces G(F) es verdadero.
  
Filósofos como J. R. Lucas (1961) han afirmado que este teorema demuestra que las máquinas son mentalmente inferiores a los hombres, porque las máquinas son sistemas formales limitados por el teorema de la incompletitud, es decir no pueden establecer la verdad de su propia sentencia Gödel, mientras que los hombres no tienen dicha limitación. Esta afirmación ha provocado mucha controversia durante décadas.

En primer lugar, el teorema de la incompletitud de Gödel se aplica sólo a sistemas formales que son lo suficientemente potentes como para realizar aritmética. Aquí se incluyen las máquinas Turing, y la afirmación de Lucas en parte se basa en la afirmación de que los computadores son máquinas de Turing. Esta es una buena aproximación, pero no es del todo verdadera. Aunque los computadores son finitos, las máquinas de Turing son infinitas, y cualquier computador por tanto se puede describir como un sistema (muy grande) en la lógica proposicional, la cual no está sujeta al teorema de incompletitud de Gödel. 

En segundo lugar, un agente no debería avergonzarse de no poder establecer la verdad de una sentencia aunque otros agentes sí puedan. 

En tercer lugar, y de manera mucho más importante, aunque reconozcamos que los computadores tienen limitaciones sobre lo que pueden demostrar, no existen evidencias de que los hombres sean inmunes ante esas limitaciones. Es realmente sencillo demostrar con rigor que un sistema formal no puede hacer X, y afirmar entonces que los hombres pueden hacer X utilizando sus propios métodos informales, sin dar ninguna evidencia de esta afirmación. En efecto, es imposible demostrar que los hombres no están sujetos al teorema de incompletitud de Gödel, porque cualquier prueba rigurosa contendría una formalización del talento humano declarado como no formalizable. De manera que nos quedamos con el llamamiento a la intuición de que los hombres, de alguna forma, pueden realizar hazañas superhumanas de comprensión matemática. Esta atracción se expresa con argumentos como «debemos asumir nuestra propia consistencia, si el pensamiento puede ser posible» (Lucas, 1976). Sin embargo ciertamente se sabe que los hombres son inconsistentes. Esto es absolutamente verdadero para el razonamiento diario, pero también es verdadero para un pensamiento matemático cuidadoso.

*El argumento de la informalidad*

Una de las críticas más persistentes e influyentes de la IA como empresa la realizó Turing mediante su «argumento de la informalidad del comportamiento». En esencia, esta afirmación consiste en que el comportamiento humano es demasiado complejo para poder captarse mediante un simple juego de reglas y que debido a que los computadores no pueden nada más que seguir un conjunto (juego) de reglas, no pueden generar un comportamiento tan inteligente como el de los hombres. En IA la incapacidad de capturarlo todo en un conjunto de reglas lógicas se denomina problema de cualificación

**IA fuerte: ¿pueden las máquinas pensar de verdad?**

Muchos filósofos han afirmado que una máquina que pasa el Test de Turing no quiere decir que esté realmente pensando, sería solamente una simulación de la acción de pensar. De nuevo esta objeción fue prevista por Turing, y cita unas palabras del Profesor Geoffrey Jefferson (1949):

“Hasta que una máquina pueda escribir un soneto o componer un concierto porque sienta los pensamientos y las emociones, y no porque haya una lluvia de símbolos, podría reconocer que la máquina iguala al cerebro, es decir, no sólo escribirlo sino que sepa que lo ha hecho.” 

Esto es lo que Turing llama el argumento de la consciencia, la máquina tiene que ser consciente de sus propias acciones y estados mentales. Aunque la consciencia sea un tema importante, el punto de vista clave de Jefferson se relaciona realmente con la fenomenología, o el estudio de la experiencia directa, es decir, la máquina tiene que sentir emociones realmente. Otros se centran en la intencionalidad, esto es, en la cuestión de si las creencias, deseos y otras representaciones supuestas de la máquina son de verdad algo que pertenece al mundo real.

La respuesta de Turing a esta objeción es interesante. Podría haber presentado razones para demostrar que las máquinas pueden de hecho ser conscientes (o tener fenomenología, o tener intenciones). En cambio, Turing mantiene que la cuestión no está bien definida al decir, «¿Pueden pensar las máquinas?» Además, por qué deberíamos insistir en un estándar más alto para las máquinas que el usado para los humanos. Después de todo, en la vida ordinaria no tenemos nunca una evidencia directa sobre los estados mentales internos de otras personas. No obstante, Turing dice que «En vez de argumentar constantemente sobre este punto de vista, es usual mantener la convención educada de que todos pensamos»

Turing reconoce que la cuestión de la conciencia (consciencia) es difícil, pero niega que sea relevante para la práctica de la IA: «No quiero dar la impresión de que pienso que no hay misterio en torno a la conciencia… Sin embargo no creo que estos misterios tengan necesariamente que resolverse antes de la respuesta a la cuestión que estamos tratando en este trabajo». Coincidimos con Turing en que nos interesa crear programas que se comporten de forma inteligente y no en si alguien los declara reales o simulados. Por otro lado, muchos filósofos están especialmente interesados en esta cuestión. Como ayuda para entenderlo tendremos en cuenta la cuestión de si otros artefactos se consideran reales.


**La ética y los riesgos de desarrollar la Inteligencia Artificial**

Hasta ahora nos hemos concentrado en si podemos desarrollar la IA, pero debemos también tener en cuenta si deberíamos hacerlo. Si es más probable que los efectos de la tecnología de la IA sean más negativos que positivos, sería responsabilidad moral de los trabajadores en su campo redirigir su investigación.

Sin embargo, la IA parece que expone problemas nuevos yendo más allá de, por ejemplo, construir puentes que no se desmoronen:

• Las personas podrían perder sus trabajos por la automatización. 
  - Opinión personal: desde mi punto de vista la automatización ha generado desempleo pero también ha generado nuevos trabajos. Por ejemplo: el desarrollo de maquinaria referida a la agricultura produce muchas mejoras a las fabricas ya que las tareas pueden ser realizadas de forma más rápida y eficiente, 1 maquina podría realizar el trabajo de 50 trabajadores en menos tiempo y con menor costo asociado. Es decir, en este caso, si todos los trabajadores de agricultura del mundo fueran reemplazados por maquinas, ¿Cómo podrían reintegrarse estos trabajadores al nuevo mercado? 
    - ¿Deberían de capacitarse en nuevas tecnologías? Si consideramos esta solución, supondría un gran gasto económico (tanto para las empresas como para los trabajadores) y mental (ya que es posible que no todos estén dispuestos a adquirir estos conocimientos).
    - Pienso que al desarrollarse nuevas tecnologías se debe de analizar cómo afectará a todo el mundo. Si estas tienen más impactos negativos que positivos considero que debe de replantearse la idea para buscar mejores soluciones o incluso descartarse. 
    El ejemplo lo aplique en agricultura pero considero que es posible aplicarlo en todos los entornos de trabajo.
    
    Por otro lado, pienso que hay trabajos que el ser humano  puede realizar de mejor forma frente las maquinas o sistemas ya que el factor humano es muy determinante, dentro de los cuales destaco Psicología pero el abanico de trabajos es inmenso hasta trabajos referidos al arte. Es decir trabajos en los cuales se requieran habilidades humanísticas por el momento suponen un cierto tipo de ventaja frente al avance tecnológico. 

• Las personas podrían tener demasiado (o muy poco) tiempo de ocio. 

  - Opinion personal: considero que la IA podría permitir que las personas tengan más tiempo de ocio, esto por ejemplo, debido a que la IA podría realizar tareas diarias. Es decir, la IA puede facilitar nuestra vida, desde preparar un café en la mañana con solo presionar un botón o incluso programarlo, hasta trasladarnos en auto de forma automatizada (autos Tesla, por mencionar una marca
 
• Las personas podrían perder el sentido de ser únicos. 

  - Opinión personal: considero que el sentimiento de ser único no se perderá nunca, desde el punto de vista de que las personas tenemos habilidades que la IA es muy poco probable que adquiera, el simple hecho de ser personas nos hace únicos. 
  
• Las personas podrían perder algunos de sus derechos privados. 

  - Opinión personal: considero que las personas si podrían perder algunos derechos privados, pero por este motivo es que debemos de tomar consciencia y responsabilidad de los usos tecnológicos. Existen sistemas de vigilancia que tienen un fin justificado hacia la humanidad (entre ellos analizar posibles amenazas), pero también existen otros que crean amenazas y ponen en riesgo nuestros datos privados. En este punto sostengo la misma opinión que Scott McNealy quien ha dicho que «De cualquier forma tenemos privacidad cero. Hay que superarlo».
 
• La utilización de los sistemas de IA podría llevar a la pérdida de responsabilidad. 

  - Opinión personal: considero dos puntos de vista en esta afirmación. Por un lado la pérdida de responsabilidad puede ser una mejora, por ejemplo al manejar vehículos cada piloto tiene responsabilidad con sí mismo y con los demás vehículos pero si dependemos de un vehiculo automatizado entonces perdemos toda responsabilidad, es decir recae en los fabricantes del vehiculo. Por otro lado en el campo de la medicina por ejemplo cuando un médico depende del juicio de un sistema médico experto para hacer diagnóstico, ¿quién es el culpable si el diagnóstico es erróneo?. Si los sistemas expertos se hacen más fiables y precisos que los hombres que hacen los diagnósticos, los médicos podrían tener obligaciones legales si no utilizan las recomendaciones de un sistema experto.
  
• El éxito de la IA podría significar el fin de la raza humana.

  - Opinión personal: considero que el éxito de la IA significaría mejoras en la vida diaria de las personas, cada año surgen nuevas tecnologías que nos permiten delegar tareas y de esta forma contar con más tiempo de ocio o simplemente para realizar esas tareas de una forma más eficiente. La IA tiene un largo camino de investigación y desarrollo para adaptarlos cuidadosamente a las metas deseadas, de esta forma generaran mayores avances tecnológicos y no supondrán una amenaza a la raza humana.  
  
