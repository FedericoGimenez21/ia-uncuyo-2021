A)1) Se elimino las variables/columnas "ultima_modificacion" "lat" "long" "area_seccion" "nombre_seccion"  para el data_train y para el test

A)2) No se crearon nuevas variables

A)3) No se normalizaron los valores

B) Resultados obtenidos de validacion

C) Resultados obtenidos de Kaggle: 0.71524

D) Descripción detallada del algoritmo propuesto: 

  Guardar los id del dataset test
  
  Eliminar las variables mencionadas
  
  Analizar cuantos arboles con inclinacion peligrosa hay en el data_train para poder balancear la cantidad de arboles con inclinacion peligrosa y sin inclinacion peligrosa
  
  A partir del analisis, seleccionar de manera random 3000 de los que no tienen inclinacion peligrosa
  
  Aplicar randomForest a data_train 
  
  Predecir los valores de inclinacion peligrosa del dataset test
  
  Crear el dataset de envio con los id guardados y la inclinacion peligrosa calculada para el test 
  
