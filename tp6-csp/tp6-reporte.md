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



![image](https://user-images.githubusercontent.com/88351465/135772291-a8e73bf1-8dc8-4ae3-b93a-b33cdc021bc8.png)


        WA -> SA 	es consistente sii WA=R and SA =(Blue or Green)
        SA->WA	es consistente sii SA=R and WA =?	
	    Por lo tanto borramos R de SA	

						

![image](https://user-images.githubusercontent.com/88351465/135772303-b03510c5-22b2-4c1e-a414-79aae90c248e.png)

	V->SA 	es consistente sii V=B and SA=Green or Red	
	SA-> V 	es consistente sii SA=Blue and V=?	
		por lo tanto borramos B de SA	

![image](https://user-images.githubusercontent.com/88351465/135772318-dfbc8773-8866-49e1-b793-89b497214228.png)

	WA->NT	es consistente sii WA=R and NT = R or G or B	
	NT->WA	es consistente sii NT=R and WA=?	
		por lo tanto borramos R de NT	

![image](https://user-images.githubusercontent.com/88351465/135772327-e71b8c0b-60c5-42f9-9035-08319f988bc9.png)

	SA->NT	es consistente sii SA=G and NT= B or G	
	NT->SA	es consistente sii NT = G and SA=?	
		por lo tanto borramos G de NT	


![image](https://user-images.githubusercontent.com/88351465/135772336-0093eabb-9d50-4b1d-890c-51a0229bce53.png)

	SA->NSW	es consistente sii SA=G and NSW = R or B or G		
	NSW->SA	es consistente sii NSW =G and SA =?		
		por lo tanto borramos G de NSW		


![image](https://user-images.githubusercontent.com/88351465/135772350-f631c5db-72f0-48c6-ab69-ac61f68d03f9.png)


	V->NSW 	es consistente sii V=B and NSW = R or B	
	NSW->V	es consistente sii NSW =B and V=?	
		por lo tanto borramos B de NSW	

![image](https://user-images.githubusercontent.com/88351465/135772357-e82997d7-8b6a-48f0-a432-c587c7cfe383.png)

	NT->Q 	es consistente sii NT=B and Q=R or B or G	
	Q->NT	es consistente sii Q=B and NT=?	
		por lo tanto borramos B de Q	

![image](https://user-images.githubusercontent.com/88351465/135772361-53a87a8e-24f2-46ae-999f-70e5ee70eeee.png)

	SA->Q	es consistente sii SA=G and Q = R or G	
	Q->SA	es consistente sii Q=G and SA=?	
		por lo tanto borramos G de Q	



![image](https://user-images.githubusercontent.com/88351465/135772374-949d4e5c-0a30-4337-a66c-47eb466c383d.png)

	Q->NSW	es consistente sii Q=R and NSW = ?	
		por lo tanto borramos R de Q	

![image](https://user-images.githubusercontent.com/88351465/135772378-f21d43a3-80a2-4fbc-ab98-73a3e43c7def.png)

	inconsistencia encontrada

3. Cuál es la complejidad en el peor caso cuando se ejecuta AC-3 en un árbol estructurado CSP. (i.e. Cuando el grafo de restricciones forma un árbol: cualquiera dos variables están relacionadas por a lo sumo un camino).

		En un arbol estructurado ningún arco será considerado más de una vez, 
		por lo tanto AC-3 es O(ED), donde E es el número de aristas y 
		D es el tamaño del dominio más grande.

4.  AC-3 coloca de nuevo en la cola todo arco ( Xk, Xi) cuando cualquier valor es removido del dominio de Xi incluso si cada valor de Xk es consistente con los valores restantes de Xi. Si por cada arco ( Xk,Xi) se lleva cuenta del número de valores que quedan de Xi que sean consistentes con Xk . Explicar como actualizar ese número de manera eficiente y demostrar que la arco consistencia puede lograrse en un tiempo total O(n2d2 )

		Pre-procesando las restricciones, de esta forma, para cada valor de Xi hacemos seguimiento de las variables Xk 
		para los cuales un arco de Xk a Xi es satisfecho por ese valor de Xi. 
		Este tipo de estructura de datos puede ser computado en tiempo proporcional al tamaño del problema. 
		Por lo tanto cuando un valor Xi es eliminado, reducimos en 1 el contador de valores permitidos para cada arco (Xk,Xi). 
		
5. Demostrar la correctitud del algoritmo CSP para  árboles estructurados (sección 5.4, p. 172 AIMA 2da edición). Para ello, demostrar: 

	a)Que para un CSP cuyo grafo de restricciones es un árbol, 2-consistencia (consistencia de arco) implica n-consistencia (siendo n número total de variables)
	
		Cualquier CSP estructurado por árbol puede resolverse en tiempo lineal en el número de variables. El algoritmo tiene los siguientes pasos:
		
		-Elija cualquier variable como la raíz del árbol, y ordene las variables desde la
		raíz a las hojas de tal modo que el padre de cada nodo en el árbol lo precede
		en el ordenamiento. Etiquetar las variables X1…, Xn
		en orden. Ahora, cada variable excepto la raíz tiene exactamente una variable
		padre.
		
		-Para j desde n hasta 2, aplicar la consistencia de arco al arco (Xi, Xj), donde Xi
		es el padre de Xj, quitando los valores del DOMINIO[Xi] que sea necesario.
		
		-Para j desde 1 a n, asigne cualquier valor para Xj consistente con el valor asignado para Xi, donde Xi es el padre de Xj.
		
		-Como el grafo de restricciones es un árbol, de esta forma solo quedará resolver 2-consistencia consistencias de arco. 
		
	b) Argumentar por qué lo demostrado en a es suficiente.
	
		-Aplicando la comprobación de consistencia de arco en orden inverso en el paso 2, 
		el algoritmo asegura que cualquier valor suprimido no puede poner en peligro 		
		la consistencia de arcos que ya han sido tratados.

6.c En cada variante, calcular los tiempos de ejecución para los casos de 4, 8, 10, 12 y 15 reinas.

	Encadenamiento hacia adelante tiempos: [0.0010006427764892578, 0.08001708984375, 0.14403200149536133, 0.5123147964477539, 4.280789136886597]
	Backtracking tiempos:  [0.001001119613647461, 0.004999876022338867, 0.008001089096069336, 0.02800583839416504, 0.18172335624694824]
	
6.d En cada variante, calcular la cantidad de estados recorridos antes de llegar a la solución para los casos de 4, 8, 10, 12 y 15 reinas.

	Encadenamiento hacia adelante estados recorridos:  [19, 577, 779, 2291, 14217]
	Backtracking estados recorridos: [8, 113, 102, 261, 1359]

6.e Realizar un gráfico de cajas para los puntos c y d.

![image](https://user-images.githubusercontent.com/88351465/135772873-a2c63870-6bb4-4f51-aa3c-508922a7eae9.png)

![image](https://user-images.githubusercontent.com/88351465/135772859-1f198481-00d5-4a74-bfad-dc4e61e8145b.png)
