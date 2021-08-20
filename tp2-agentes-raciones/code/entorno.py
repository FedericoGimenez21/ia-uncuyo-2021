import numpy;
import random;
class Enviroment:

  def __init__(self,fila,columna,dirty):


    
    self.m=numpy.random.choice([0, 1], size=(fila,columna), p=[1-dirty,dirty])
    self.x=random.randint(0,len(self.m)-1)
    self.y=random.randint(0,len(self.m)-1)
    self.performance=0



  def prin(self):
    
    print(self.m)


  def accept_action(self,action,i,j):
    if 0<=i<=(len(self.m)-1) and 0<=j<=(len(self.m)-1):
      if action=="arriba":
        if 0<=i-1<=len(self.m)-1:
          self.x=self.x-1
          return True;

        else:
          return False;

      if action=="abajo":
        if 0<=i+1<=len(self.m)-1:
          self.x=self.x+1
          return True;

        else:
          return False;
      if action=="derecha":
        if 0<=j+1<=len(self.m)-1:
          self.y=self.y+1
          return True;

        else:
          return False;
      if action=="izquierda":
        if 0<=j-1<=len(self.m)-1:
          self.y=self.y-1
          return True;

        else:
          return False;
      if (action=="limpiar"):
        self.m[i][j]=0
        self.performance+=1
        return True;
      if (action=="nada"):
        return True;
    else:
      return False;

  def is_dirty(self,i,j):
    if (self.m)[i][j]==1:
      return True;
    else:
      return False;


  def get_performance(self):
    return self.performance;



