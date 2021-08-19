10.a) No, un agente reflexivo simple no puede ser racional. Asumamos que la unica percepcion que recibe el agente es acerca de la posicion en la que se encuentra, si esta limpia o sucia. En este caso el agente solo puede decidir si limpiar o no, y decidir a que posicion adjunta moverse. Sin conocimiento del entorno el agente es posible que se mueva en circulos, siendo penalizado por cada movimiento y teniendo una performance final mala, o decidir no hacer nada evadiendo las penalizaciones de movimiento pero dejando las casillas o posiciones sucias. 

10.b) Un agente reflexivo con estados tampoco será racional.
  Diseño: 
  Agregaria una funcion que verifique si la posicion actual ya fue verificada(una casilla se marcará como verificada cuando se haya limpiado o no en caso necesario, en caso de verdadero que no realice nada. Luego se moverá a la siguiente posicion dependiendo de donde se encuentre. 
  Es decir: 
    if (sucia):
      limpiar();
    elif (vericada==True):
      nada();
    elif (posicion==Izquierda) and (verificada==True):
      ir derecha;;
    if (posicion==Derecha) and (verificada==True):
      ir izquierda;
    
10.c) En este caso teniendo conocimiento de todo el entorno, un agente reflexivo simple puede ser racional, en mi opinion los estados no presentan una mejora. Seria posible que el agente tenga conocimiento acerca de que acciones realizar frente a cada posicion/casilla. Luego de que el agente realice acciones, su conocimiento se actualiza y su funcion de percepcion decide que accion realizar.  

11.a) Un agente reflexivo simple no puede ser perfectamente racional para el entorno mencionado, dado que el agente no conoce acerca de la geogafia del entorno y percibe a partir de la ubicacion actual unicamente y no recuerda que acciones realizó, es posible que se encuentre atascado (por los obstaculos) o "dando vueltas en circulos". 

11.b) Agente realizado en agent.py

11.c) Adjunto imagen con el entorno 

11.d) Un agente reflexivo con estados puede superar a un agente reflexivo simple ya que explorará el entorno e irá almacenando un conocimiento acerca del mismo. Es decir, cada accion lo llevara a una nueva percepcion del entorno. 
