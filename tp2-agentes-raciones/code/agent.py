from entorno import*
import random;

class AgentRandom:
  def __init__(self,Enviroment):
    self.e=Enviroment
    

  def up(self):
    flag=self.e.accept_action("arriba",self.e.x,self.e.y)

    return flag;

  def down(self):
    flag=self.e.accept_action("abajo",self.e.x,self.e.y)
    return flag;
  def right(self):
    flag=self.e.accept_action("derecha",self.e.x,self.e.y)
    return flag;

  def left(self):
    flag=self.e.accept_action("izquierda",self.e.x,self.e.y)
    return flag;

  def suck(self):
    if self.e.is_dirty(self.e.x,self.e.y):
      
      flag=self.e.accept_action("limpiar",self.e.x,self.e.y)
      return flag;
    else:
      return False

  def idle(self):
    flag=self.e.accept_action("nada",self.e.x,self.e.y)
    return flag;
  
  def perspective(self):
    flag=self.e.is_dirty(self.e.x,self.e.y)
    return flag;


  def think(self):
    acciones=0
    cantidad=0
    bandera=True
    while bandera:
      if acciones==1000:
        bandera=False
        break

      flag=True
      while flag:
        n=(random.randint(0,5))
        if n==0:
          #nada
          cantidad+=1
          if self.idle():
            acciones+=1
            if(acciones==1000):
              bandera=False
            flag=False
          continue          
        if n==1:
          cantidad+=1
          #arriba
          if self.up():
            acciones+=1
            if(acciones==1000):
              bandera=False
            flag=False
          continue
          
          
          
            
        if n==2:
          cantidad+=1
          #abajo
          if self.down():
            acciones+=1
            if(acciones==1000):
              #paramos el primer bucle
              bandera=False
            flag=False
          continue

        if n==3:
          cantidad+=1
          #derecha
          if self.right():
            acciones+=1
            if(acciones==1000):
              bandera=False
            flag=False
          continue
        if n==4:
          cantidad+=1
          #izquierda
          if self.left():
            acciones+=1
            if(acciones==1000):
              bandera=False
            flag=False
          continue

        if n==5:
          cantidad+=1
          #limpiar
          if self.suck():
            acciones+=1
            if(acciones==1000):
              bandera=False
            flag=False
          continue         
    #print(cantidad)



class AgentReflexSimple:
  def __init__(self,Enviroment):
    self.e=Enviroment
    

  def up(self):
    flag=self.e.accept_action("arriba",self.e.x,self.e.y)

    return flag;

  def down(self):
    flag=self.e.accept_action("abajo",self.e.x,self.e.y)
    return flag;
  def right(self):
    flag=self.e.accept_action("derecha",self.e.x,self.e.y)
    return flag;

  def left(self):
    flag=self.e.accept_action("izquierda",self.e.x,self.e.y)
    return flag;

  def suck(self):
    if self.e.is_dirty(self.e.x,self.e.y):
      
      flag=self.e.accept_action("limpiar",self.e.x,self.e.y)
      return flag;
    else:
      return False

  def idle(self):
    flag=self.e.accept_action("nada",self.e.x,self.e.y)
    return flag;
  
  def perspective(self):
    flag=self.e.is_dirty(self.e.x,self.e.y)
    return flag;


  def think(self):

    acciones=0
    #xinicial yinicial

    while acciones<1000:
      #xi e yi se iran actualizando a traves de accept_action, es decir en un principio son el punto de partida y luego seran los indices de movimiento 
      xi=self.e.x
      yi=self.e.y
      #print("x: ",xi)
      #print("y: ",yi)
      #verifo si esta sucia la casilla
      if self.e.is_dirty(xi,yi)==True:
        #limpiamos
        if self.e.accept_action("limpiar",xi,yi):

          #incrementamos performance y el contador de acciones
          
          acciones+=1
          if(acciones==1000):
            break
          continue
      
      if self.e.is_dirty(xi,yi)==False:
        #cada vez que una casilla este limpia, no hace nada, luego se mueve a otra casilla
        self.e.accept_action("nada",xi,yi)
        acciones+=1
        if(acciones==1000):
          break
        #flag de stop
        flag=True
        while flag==True:
          #n random para ir tomando movimientos random (Arriba, abajo, izquierda, derecha)
          n=(random.randint(0,3))
          #si es 0 derecha
          if n==0:
            if self.e.accept_action("derecha",xi,yi):
              acciones+=1
              if(acciones==1000):
                break
              flag=False
          #si es 1 izquierda    
          if n==1:
            if self.e.accept_action("izquierda",xi,yi):
              acciones+=1
              if(acciones==1000):
                break
              flag=False;
          #si es 2 arriba    
          if n==2:

            if self.e.accept_action("arriba",xi,yi):
              acciones+=1
              if(acciones==1000):
                break
              flag=False;
          #si es 3 abajo    
          if n==3:  
            if self.e.accept_action("abajo",xi,yi):
              acciones+=1
              if(acciones==1000):
                break
              flag=False;
          else:
            continue
        continue
