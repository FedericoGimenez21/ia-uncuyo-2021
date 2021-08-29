B) 
  1)Algoritmo de búsqueda a lo ancho 
  
    Resultados de los 30 entornos generados aleatoriamente
    
    ([4487, 4735, 2930, 5864, 3582, 2867, 2400, 1041, 447, 7073, 3728, 4423, 858, 3278, 318, 1588, 4657, 4851, 8572, 132, 1504, 392, 518, 910, 7479, 5198, 3837, 1302, 8083, 4773])
   
    Media= 3394.2
    
    Desviación =2458.6
    
  2)Algoritmo de búsqueda uniforme
         
    
    Resultados de los 30 entornos generados aleatoriamente
    
    ([4487, 4735, 2930, 5864, 3582, 2867, 2400, 1041, 447, 7073, 3728, 4423, 858, 3278, 318, 1588, 4657, 4851, 8572,  132, 1504, 392, 518, 910, 7479, 5198, 3837, 1302, 8083, 4773])
   
    Media= 3394.2
    
    Desviación =2458.6  
  3) Algoritmo de búsqueda en profundidad limitada
  
    Resultados de los 30 entornos generados aleatoriamente
    
    ([3283, 2030, 2852, 2775, 479, 6246, 5621, 4157, 3425, 1325, 7711, 3164, 29, 3302, 1302, 6052, 201, 3966, 594, 64, 7440, 1212, 1983, 1582, 3853, 3244, 2253, 1152, 1316, 6403] )
    
    Media= 2967.2
    
    Desviación =2203.3   
    
 
    
C) Cuál de los 3 algoritmos considera más adecuado para resolver el problema planteado en A)?. Justificar la respuesta.
  
    Por un lado, teniendo en cuenta la cantidad de estados (casillas en este caso), el algoritmo de búsqueda en profundidad limitada presenta el mejor rendimiento frente a búsqueda a lo ancho y búsqueda de costo uniforme. Esto se debe a como está planteado el algoritmo, es decir, expande en profundidad cada camino hasta llegar a un objetivo sin necesidad de explorar o analizar cada estado o casilla. Podemos observar estos resultados en los ejemplos de ejecución, la media y la desviación (teniendo en cuenta cantidad de estados en cada ejecución de los entornos) más bajas se presentan en general en búsqueda en profundidad limitada. 
    
    Por otro lado, dado que en el problema no se plantea costos por movimiento, es decir no existe ninguna prioridad a la hora de elegir el siguiente estado, el algoritmo de búsqueda a lo ancho y búsqueda de costo uniforme presentan los mismos rendimientos. 
    
    Teniendo en cuenta ahora la longitud de los caminos que presentan los diferentes algoritmos, es lógico que el algoritmo de búsqueda a lo ancho presente una ventaja en este apartado, ya que examina todos los posibles casos para cada casilla, de esta forma siempre asegura el camino más corto.
    
    Finalizando, en resumen, si necesitamos encontrar simplemente un camino desde un punto inicio hasta un punto objetivo en una grilla, entonces la mejor opción será implementar el algoritmo de búsqueda en profundidad. En cambio si necesitamos encontrar el camino más corto desde un punto inicio hasta un punto objetivo entonces deberíamos usar el algoritmo de búsqueda a lo ancho. Y si el problema presentará costos por movimiento la mejor opción sería utilizar el algoritmo de costo uniforme.

  
