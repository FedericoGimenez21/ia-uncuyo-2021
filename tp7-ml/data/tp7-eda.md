PARTE A

1)a)


data <- read_csv("data/arbolado-mza-dataset.csv") 

trainIndex <- createDataPartition(as.factor(data$inclinacion_peligrosa), p=0.80, list=FALSE)
data_train <- data[ trainIndex,]
data_test <-  data[-trainIndex,]



2)a) 

data_train %>% group_by(inclinacion_peligrosa) %>% summarise(total=n())

![image](https://user-images.githubusercontent.com/88351465/138969810-5cecfa8d-ece6-4268-bb49-355817b0cd76.png)


2)b) 

#juntamos dos peticiones, una que cuenta el total por seccion y otra que que cuenta el total por seccion agrupada por inclinacion peligrosa
sub1 <- merge(data %>% group_by(seccion) %>% summarise(total=n()),data %>% group_by(inclinacion_peligrosa,seccion) %>% summarise(total_inclinacion=n()),by="seccion")

#con los datos anteriores podemos calcular los porcentajes y analizarlos
sub1%>% mutate(prob=total_inclinacion/total)


![image](https://user-images.githubusercontent.com/88351465/138969863-270c4ba4-2c9b-4184-a3f2-50b2a2d5fdc3.png)

![image](https://user-images.githubusercontent.com/88351465/138969875-ea7662ff-fba5-466f-929f-0ab5f3835391.png)


**De esta forma podemos observar que la seccion que presenta mayor porcentaje de arboles con inclinacion_peligrosa es la 2**

**En cambio si necesitamos observar cual es la seccion con mayor cantidad de arboles con inclinacion peligrosa podemos visualizar el siguiente grafico**

ggplot(data)+
  geom_bar(aes(x=as.factor(inclinacion_peligrosa),fill=as.factor(inclinacion_peligrosa)   ))+
  theme_bw()+
  facet_wrap(~seccion)
  
  
![image](https://user-images.githubusercontent.com/88351465/138970365-49d27262-5d4f-49d9-9159-91209cfb6786.png)


Asi podemos visualizar que la seccion con mayor cantidad de arboles con inclinacion peligrosa es la 4 

2)c)

#juntamos dos peticiones, una que cuenta el total por especie y otra que que cuenta el total por especie agrupada por inclinacion peligrosa
sub2 <- merge(data %>% group_by(especie) %>% summarise(total=n()),data %>% group_by(inclinacion_peligrosa,especie) %>% summarise(total_inclinacion=n()),by="especie")

#con los datos anteriores podemos calcular los porcentajes y analizarlos

sub3<- sub2%>%mutate(prob=total_inclinacion/total) 
ordenado<- sub3[order(sub3$prob),]

![image](https://user-images.githubusercontent.com/88351465/138971372-593ca325-08ad-48eb-a928-37b94b147cf3.png)

**De esta forma podemos observar que la especie que presenta mayor porcentaje de arboles con inclinacion peligrosa es Algarrobo**

En cambio, si lo visualizamos con el grafico: 
ggplot(data_train)+
  geom_bar(aes(x=as.factor(inclinacion_peligrosa),fill=as.factor(inclinacion_peligrosa)   ))+
  theme_bw()+
  facet_wrap(~especie)# Aca estamos indicando que queremos que diferencie por especie
  
  ![image](https://user-images.githubusercontent.com/88351465/138971552-fbc64853-a708-452c-af07-59ae4ba1b318.png)

Podemos ver que la especie morera presenta mayor cantidad de arboles con inclinacion peligrosa frente a los demas


3)b)

hist(data$circ_tronco_cm, xlab = "diametro", main="Histograma de circ_tronco_cm")

![image](https://user-images.githubusercontent.com/88351465/138973255-2720de7b-867a-4ca4-887a-41aad649a76a.png)

3)c)

hist(data$inclinacion_peligrosa, xlab = "inclinacion peligrosa", breaks = 2, labels = c("0","1"), main = "Histograma de inclinacion peligrosa")

![image](https://user-images.githubusercontent.com/88351465/138973292-8e99a3ba-db96-48f6-baee-db55f9e545ac.png)


3)d)

data_circ_categorical <- data %>% mutate(circ_tronco_cm_cat= ifelse(`circ_tronco_cm`<=100,'bajo',
                                                               ifelse(`circ_tronco_cm`>100 & `circ_tronco_cm` <= 200, 'medio',
                                                                      ifelse(`circ_tronco_cm` > 200 & `circ_tronco_cm` <= 300, 'alto','muy alto'))))

write.csv(data_circ_categorical,"C:\\Users\\Fede\\Desktop\\arbolado-publico-mendoza-2021-circ_tronco_cm-train.csv")




4)a) 

predictFunc<- function(recibida){
  
  final <- recibida %>% mutate(prediction_prob=runif(nrow(data_train),min=0,max(1)))
  return(final)
}

data_train<- predictFunc(data_train)

4)b)

random_classifier<-function(recibida){
  final <-recibida %>% mutate(prediction_class = ifelse(`prediction_prob` >= 0.5, 1 ,0))
  return(final)
}


data_train <- random_classifier(data_train)

4)d)

TruePositive<- nrow(data_train %>% filter(inclinacion_peligrosa==1 & prediction_class==1))

TrueNegative<- nrow(data_train %>% filter(inclinacion_peligrosa==0 & prediction_class==0))

FalsePositive <- nrow(data_train %>% filter(inclinacion_peligrosa==0 & prediction_class==1))

FalseNegativo <-nrow(data_train %>% filter(inclinacion_peligrosa==1 & prediction_class==0))


5)a) 

mayority<-  data_train %>% group_by(inclinacion_peligrosa) %>% summarise(total=n())

m<- max(mayority)

#se debe establecer el prediction_class  de forma manual analizando **m **
biggerclass_classifier<- function(recibido){
  
  final <-recibido %>% mutate(prediction_class = 0)
  return(final)
}
data2 <- biggerclass_classifier(data_train)


TruePositive2<- nrow(data2 %>% filter(inclinacion_peligrosa==1 & prediction_class==1))

TrueNegative2<- nrow(data2 %>% filter(inclinacion_peligrosa==0 & prediction_class==0))

FalsePositive2 <- nrow(data2 %>% filter(inclinacion_peligrosa==0 & prediction_class==1))

FalseNegativo2 <-nrow(data2 %>% filter(inclinacion_peligrosa==1 & prediction_class==0))


6)a)

acur<- (TrueNegative2 +TrueNegative2)/(TrueNegative2+TrueNegative2+FalsePositive2+FalseNegativo2)
Pres<- TruePositive2/(TruePositive2+FalsePositive2)
Sens<-TruePositive2/(TruePositive2+FalseNegativo2)
speci<- TrueNegative2/(TrueNegative2+FalsePositive2)
