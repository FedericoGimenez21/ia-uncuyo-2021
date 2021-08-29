from collections import deque
import random;

import numpy;
import statistics;
class PriorityQueue(object):
    def __init__(self):
        self.queue = deque()
        
  
    
  
   
  
    # insertar elementos
    def insert(self, data):
        self.queue.append(data)
        
  
    # eliminar por prioridad
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i].priority > max:
                    max = self.queue[i].priority
            item = self.queue[max]
            del self.queue[max]
           
            return item
        except IndexError:
            print()
            exit()


class Node:
   
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent
        self.priority=0
 
    
 
 
# movimientos posibles
row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]
 
 
# verifica si es valida una posicion, si esta dentro de los limites y si el valor es cero o cien 
def isValid(matrix,x, y):

  if (0 <= x < len(matrix)) and (0 <= y < len(matrix)):

    if matrix[x][y]==0 or matrix[x][y]==100:
      return True;
  else:
    return False;
 


def findPathBFS(matrix, x, y,zi,zj):
 
    #FIFO
    q = deque()
    src = Node(x, y, None)
    q.append(src)

    visited = set()
 
    key = (src.x, src.y)
    visited.add(key)
    countBFS=0
  
    while q:
        countBFS+=1
      
        curr = q.popleft()
        i = curr.x
        j = curr.y
        #print("i: ",i)
        #print("j: ",j)
      
        if i == zi and j == zj:
            #print("countBFS: ",countBFS)
            return True,countBFS
 
        
        
 
        for k in range(4):
            
            x = i + row[k] 
           
            y = j + col[k] 
   
            if isValid(matrix,x, y):
          
                next = Node(x, y, curr)
                key = (next.x, next.y)
 
                
                if key not in visited:
                    
                    q.append(next)
                    visited.add(key)

 
    #print("countBFS: ",countBFS)
    return False,None



def findPathPriority(matrix, x, y,zi,zj):
 
    
    q = PriorityQueue()
    src = Node(x, y, None)
    q.insert(src)
    

    
    visited = set()
 
    key = (src.x, src.y)
    visited.add(key)
    countPrio=0
    
    while q.queue:
        
        countPrio+=1
        # desencola con prioridad
        curr = q.delete()
        
        i = curr.x
        j = curr.y
  
        # return si se encuentra el destino
        if i == zi and j == zj:
            #print("count priority: ",countPrio)
            return True,countPrio
 
 
 
        # chequea los posibles movimientos
        for k in range(4):
         

            x = i + row[k] 
           
            y = j + col[k] 
           
            # chequea si es posible ir a una siguiente posicion
            if isValid(matrix,x, y):
                # nodo siguiente
                next = Node(x, y, curr)
                key = (next.x, next.y)
 
                # si no ha sido visitado
                if key not in visited:
                    # encola y lo marca como visitado
                    q.insert(next)
                    
                    visited.add(key)
 
    # return None si no existe camino
    #print("count priority: ",countPrio)
    return False,None


def findPathDFS(matrix, x, y,zi,zj):
    #LIFO
    #DFS CON LIMITE DE MOVIMIENTOS
    limite=len(matrix)*(len(matrix)-20)

    q = deque()
    src = Node(x, y, None)
    q.append(src)

    visited = set()
 
    key = (src.x, src.y)
    visited.add(key)

    count=0
    
    while q:
        if count>limite:
            return False,None
        #print(q)
        count+=1
       
        curr = q.pop()
        i = curr.x
        j = curr.y
        #print("i: ",i)
       # print("j: ",j)
     
        
        if i == zi and j == zj:
            #print("count DFS: ",count)
           # printPath(curr)
           #return curr
            return True,count
 
      
       
 
       
        for k in range(4):
          

            x = i + row[k] 
         
            y = j + col[k] 
            
    
            if isValid(matrix,x, y):
               # print("valido: "+str(x)+str(y))
                next = Node(x, y, curr)
                key = (next.x, next.y)

            
                if key not in visited and (key not in q):
                    
                    q.append(next)
                    visited.add(key)
       
                else:
                    for a in range(0,len(q)):
                        if q[a].x==next.x and q[a].y==next.y:
                            
                            q[a].parent=curr
                    
 

    #print("count DFS: ",count)
    return False,None
 


class PriorityQueueA(object):
    def __init__(self):
        self.queue = deque()
        

    def insert(self, data):
        self.queue.append(data)
        
  
    # elimina y retorna elemento  con prioridad mas chica
    def delete(self):
        try:
            max = 99999999
            indice=0
            for i in range(0,len(self.queue)):
                #print(self.queue[i].f)
                if self.queue[i].f < max:
                    max = self.queue[i].f
                    indice=i
            item = self.queue[indice]
            del self.queue[indice]
           
            return item
        except IndexError:
            print()
            exit()
class NodeAestrella:
   
    def __init__(self, x, y, parent,g,h,f):
        self.x = x
        self.y = y
        self.parent = parent
        self.f=f
        self.g=g
        self.h=h
 


def CalculateH(x,y,zi,zj):
    return (abs(x-zi)+abs(y-zj))
def findPathA(matrix, x, y,zi,zj):
 
    
    q = PriorityQueueA()
    src = NodeAestrella(x, y, None,0,0,0)
    q.insert(src)
    

    
    visited = set()
 
    key = (src.x, src.y)
    visited.add(key)
    countPrioA=0
    
    while len(q.queue)!=0:
        #print(q.queue)
     
        countPrioA+=1
        # desencola con prioridad
        curr = q.delete()
        
        i = curr.x
        j = curr.y
        #print("x: ",i)
        #print("j: ",j)
        # return si se encuentra el destino
        if i == zi and j == zj:
 
            #print("count priority: ",countPrio)
            #printPath(curr)
            return True,countPrioA
 
 
 
        # chequea los posibles movimientos
        for k in range(4):
         

            x = i + row[k] 
           
            y = j + col[k] 
           
            # chequea si es posible ir a una siguiente posicion
            if isValid(matrix,x, y):
                # nodo siguiente
                gnuevo=curr.g+1
                hnuevo=CalculateH(x,y,zi,zj)
                fnuevo=gnuevo+hnuevo
                next = NodeAestrella(x, y, curr,gnuevo,hnuevo,fnuevo)
                key = (next.x, next.y)
 
                # si no ha sido visitado
                if key not in visited :
                    # encola y lo marca como visitado
                    q.insert(next)
                    
                    visited.add(key)
 
    # return None si no existe camino
    #print("count priority: ",countPrio)
    return False,None


# Imprimir el camino
def printPath(node):
    if node is None:
        return 0
 
    length = printPath(node.parent)
    print(node, end=' ')
    return length + 1
 
 
if __name__ == '__main__':    
    arrayBFS=deque()
    arrayPrio=deque()
    arrayDFS=deque()
    arrayA=deque()
    soluciones=0
    #itera hasta que se encuentren 30 soluciones para los 4 algoritmos
    while soluciones<30:
            
        obstaculos=random.randint(0,10)
        prob0=((10-obstaculos)/10)
        prob1=obstaculos/10
        matrix=numpy.random.choice([0, 1], size=(100,100), p=[prob0,prob1])
        xi=random.randint(0,len(matrix)-1)
        xj=random.randint(0,len(matrix)-1)
        matrix[xi][xj]=50
        while True:
            zi=random.randint(0,len(matrix)-1)
            zj=random.randint(0,len(matrix)-1)
            if zi!=xi and zj!=xj:
                matrix[zi][zj]=100
                break
        booleanoBFS,estadosBFS=findPathBFS(matrix, xi, xj,zi,zj)
        booleanoPriority,estadosPriority=findPathPriority(matrix, xi, xj,zi,zj)
        booleanoDFS,estadosDFS=findPathDFS(matrix, xi, xj,zi,zj)
        booleanoA,estadosA=findPathA(matrix, xi, xj,zi,zj)
        if booleanoDFS==True and booleanoPriority==True and booleanoBFS==True and booleanoA==True:
            arrayBFS.append(estadosBFS)
            arrayPrio.append(estadosPriority)
            arrayDFS.append(estadosDFS)
            arrayA.append(estadosA)
            soluciones+=1
    print("ARRAY BFS: ")
    print(arrayBFS)
    print("")
    print("ARRAY PRIORIDAD: ")
    print(arrayPrio)
    print("")
    print("ARRAY DFS: ")
    print(arrayDFS)
    print("")
    print("ARRAY A*: ")
    print(arrayA)
    print("")    
    mediaBFS=statistics.mean(arrayBFS)
    mediaPrio=statistics.mean(arrayPrio)
    mediaDFS=statistics.mean(arrayDFS)
    mediaA=statistics.mean(arrayA)
    
    print("MEDIA USANDO BFS: ", mediaBFS)
    print("MEDIA USANDO BUSQUEDA UNIFORME(COLA PRIORIDAD): ", mediaPrio)
    print("MEDIA USANDO DFS LIMITADO: ", mediaDFS)
    print("MEDIA USANDO A*: ", mediaA)
    
    print("")
    print("calculo de desviacion estandar")
    desviacionBFS=statistics.stdev(arrayBFS)
    desviacionPrio=statistics.stdev(arrayPrio)
    desviacionDFS=statistics.stdev(arrayDFS)
    desviacionA=statistics.stdev(arrayA)
    print("DESVIACION USANDO BFS: ",desviacionBFS)
    print("DESVIACION USANDO BUSQUEDA UNIFORME(COLA PRIORIDAD): ",desviacionPrio)
    print("DESVIACION USANDO DFS LIMITADO: ",desviacionDFS)
    print("DESVIACION USANDO A*: ",desviacionA)
