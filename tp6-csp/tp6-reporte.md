1. Describir en detalle una formulación CSP para el Sudoku
    -Variables: 
    
        81 variables cada una representando el valor de una celda
    
    -Dominio: 
 
        valores fijos para celdas que ya están rellenadas, y un conjunto {1,2,…,9} para las celdas vacías
    
    -Restricciones: 

        Toda lista de columnas debe ser un conjunto.
      
        Toda lista de filas debe ser un conjunto.
      
        Cada sub-cuadrado debe ser único. 
2. Utilizar el algoritmo AC-3 para demostrar que la arco consistencia puede detectar la inconsistencia de la asignación parcial {WA=red, V=blue} para el problema del colorar el mapa de Australia (Figura 5.1 AIMA 2da edición ).

        ![image](https://user-images.githubusercontent.com/88351465/135772225-a4987514-bca1-4b2b-a434-1a832f42d970.png)
        WA -> SA 	es consistente sii WA=R and SA =(Blue or Green)
        SA->WA	es consistente sii SA=R and WA =?	
	    Por lo tanto borramos R de SA	



    
