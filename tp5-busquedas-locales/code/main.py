import numpy
import statistics
from time import time
from collections import deque
import random
import numpy
import math
import copy

cantidadEstadosGenetico=[]
class GeneticChess:

    def __init__(self,n):
        self.board = self.createBoard(n)
        self.solutions = []
        self.size = n
        self.env = []
        self.goal = None
        self.goalIndex = -1
        self.estados=None


    def createBoard(self,n):
        board = [[0 for i in range(n)] for j in range(n)]
        return board

    def setBoard(self,board,gen):
        for i in range(self.size):
            board[gen[i]][i] = 1
    def genereteDNA(self):
        #genereates random list of length n
        from random import shuffle
        DNA = list(range(self.size))
        shuffle(DNA)
        while DNA in self.env:
            shuffle(DNA)
        return DNA

    def initializeFirstGenereation(self):
        if self.size==4:
            for i in range(9):
                self.env.append(self.genereteDNA())
        if self.size==8:
            for i in range(50):
                self.env.append(self.genereteDNA())
        if self.size==10:
            for i in range(200):
                self.env.append(self.genereteDNA())
        if self.size==12:
            for i in range(300):
                self.env.append(self.genereteDNA())    

    def utilityFunction(self,gen):

        hits = 0
        board = self.createBoard(self.size)
        self.setBoard(board,gen)
        col = 0

        for dna in gen:
            try:
                for i in range(col-1,-1,-1):
                    if board[dna][i] == 1:
                        hits+=1
            except IndexError:
                print(gen)
                quit()
            for i,j in zip(range(dna-1,-1,-1),range(col-1,-1,-1)):
                if board[i][j] == 1:
                    hits+=1
            for i,j in zip(range(dna+1,self.size,1),range(col-1,-1,-1)):
                if board[i][j] == 1:
                    hits+=1
            col+=1
        return hits

    def isGoalGen(self,gen):
        if self.utilityFunction(gen) == 0:
            return True
        return False

    def crossOverGens(self,firstGen,secondGen):
        #intercambia los elementos de la primera lista con los de la segunda cuando la diferencia de         
        #de dos elementos en una de las listas es menor a 2
        for i in range(0,len(firstGen)):
            if abs(firstGen[i-1] - firstGen[i])<2:
                firstGen[i],secondGen[i] = secondGen[i],firstGen[i]
            if abs(secondGen[i-1] - secondGen[i])<2:
                firstGen[i],secondGen[i] = secondGen[i],firstGen[i]


    def MutantGen(self,gen):

        bound = self.size//2
        from random import randint as rand
        from random import uniform as uni
        #mutacion con probabilidad
        if uni(0,1)<0.3:
            leftSideIndex = rand(0,bound)
            RightSideIndex = rand(bound+1,self.size-1)
            newGen = []
            for dna in gen:
                if dna not in newGen:
                    newGen.append(dna)
            for i in range(self.size):
                if i not in newGen:
                    # newGen.insert(rand(0,len(gen)),i)
                    newGen.append(i)

            gen = newGen
            gen[leftSideIndex],gen[RightSideIndex] = gen[RightSideIndex],gen[leftSideIndex]
        return gen


    def crossOverAndMutant(self):
        #print("len inicial: ",len(self.env))
        for i in range(1,len(self.env),2):
            firstGen = self.env[i-1][:]
            secondGen = self.env[i][:]
            self.crossOverGens(firstGen,secondGen)
            firstGen = self.MutantGen(firstGen)
            secondGen = self.MutantGen(secondGen)
            self.env.append(firstGen)
            self.env.append(secondGen)
        #print("len final: ",len(self.env))

    def makeSelection(self):
        #index problem
        genUtilities = []
        newEnv = []

        for gen in self.env:
            
            genUtilities.append(self.utilityFunction(gen))
   
        if min(genUtilities) == 0:
            self.goalIndex = genUtilities.index(min(genUtilities))
            self.goal = self.env[self.goalIndex]
            return self.env
        minUtil=None
        while len(newEnv)<self.size:
            
            minUtil = min(genUtilities)
            
            minIndex = genUtilities.index(minUtil)
            newEnv.append(self.env[minIndex])
            genUtilities.remove(minUtil)
            self.env.remove(self.env[minIndex])

        return newEnv

    def solveGA(self):
        startAlgo=time()
        self.initializeFirstGenereation()
        count = 0
      
        
        while True:
            timeIntermedio=time()
            if timeIntermedio-startAlgo>1:
                return False
            #print(count)
            self.crossOverAndMutant()
            #print(len(self.env))
            self.env = self.makeSelection()
            count +=1
            if count==50:
                return False
 
            if self.goalIndex >= 0 and count>1:
                try:
            
         
                    #print("count: ",count)
                    cantidadEstadosGenetico.append(count)
                    return self.goal
                    
                except IndexError:
                    print(self.goalIndex)
            else:
                continue



    def reportGASolverTime(self):
        from time import time
        start = time()
        self.solveGA()
        end = time()
        with open("GA_report.txt","a") as file:
            file.write(str(end-start)+"\n")


def configurar(tablero,estados):

    for i in range(0,len(estados)):
        tablero[estados[i]][i]=1



def heuristica(tablero,pos):
    #pos contiene fila en [0] y columna en [1]
    directions=[0,1,2,3,4,5] 
    visited = []
    h=0

    for i in directions:
        #IZQUIERDA HORIZONTAL
        if(i == 0):
            if(pos[1] != 0):
                fila = pos[0]
                columna = pos[1]
                while(columna > 0):
                    columna -= 1
                    if(tablero[columna] == fila):
                    #SI NO HA SIDO VISITADA
                        if(not([fila,columna] in visited)):
                            visited.append([fila,columna])
                            h+=1
        #DERECHA HORIZONTAL
        elif(i == 1):
            if(pos[1] != len(tablero)-1):
                fila = pos[0]
                columna = pos[1]
                while(columna < len(tablero)-1):
                    columna += 1
                    if(tablero[columna] == fila):#SI SE ENCUENTRA REINA SE DEBE VERIFICAR SI YA FUE VISITADA 
                        if(not([fila,columna] in visited)):
                            visited.append([fila,columna])
                            h+=1
        #ARRIBA DERECHA
        elif(i == 2):
            if(pos[0] != 0 and pos[1] != len(tablero)-1): 
                fila = pos[0]
                columna = pos[1]
                while(fila > 0 and columna < len(tablero)-1): #MIENTRAS PUEDA SUBIR POR DIAGONAL HACIA ARRIBA DERECHA
                    columna += 1
                    fila -= 1
                    if(tablero[columna] == fila): 
                        if(not([fila,columna] in visited)):
                            visited.append([fila,columna])
                            h+=1
        #ARRIBA IZQUIERDA
        elif(i == 3):
            if(pos[0] != 0 and pos[1] != 0): 
                fila = pos[0]
                columna = pos[1]
                while(fila > 0 and columna > 0): #MIENTRAS PUEDA SUBIR POR DIAGONAL HACIA ARRIBA IZQUIERDA
                    columna -= 1
                    fila -= 1
                    if(tablero[columna] == fila):
                        if(not([fila,columna] in visited)):
                            visited.append([fila,columna])
                            h+=1
        #ABAJO DERECHA
        elif(i==4):
            if(pos[0] != len(tablero)-1 and pos[1] != len(tablero)-1): 
                fila = pos[0]
                columna = pos[1]
                while(fila < len(tablero)-1 and columna < len(tablero)-1): #MIENTRAS PUEDA BAJAR POR DIAGONAL HACIA ABAJO DERECHA
                    columna += 1
                    fila += 1
                   
                    if(tablero[columna] == fila): 
                        if(not([fila,columna] in visited)):
                            visited.append([fila,columna])
                            h+=1
        #ABAJO IZQUIERDA
        elif(i==5):
            if(pos[0] != len(tablero)-1 and pos[1] != 0): 
                fila = pos[0]
                columna = pos[1]
                while(fila < len(tablero)-1 and columna > 0):  #MIENTRAS PUEDA BAJAR POR DIAGONAL HACIA ABAJO IZQUIERDA
                    columna -= 1
                    fila += 1
                    if(tablero[columna] == fila): 
                        if(not([fila,columna] in visited)):
                            visited.append([fila,columna])
                            h+=1

    return h
    
def HillClimb(array):
    tablero=copy.deepcopy(array)
    count=0

    while count<1000:
     # print(count)
        reinas=0
        for i in range(0,len(tablero)):
            h=heuristica(tablero,[tablero[i],i])
            if h==0:
                reinas+=1
        if reinas==len(tablero):
            iteracionesHill.append(count)
            return tablero
        for i in range(0,len(tablero)):
        #print(i)
        
            incremento = 0
            while(tablero[i]-incremento >= 0):
            
                h1=heuristica(tablero,[tablero[i],i])
            

                h2=heuristica(tablero,[tablero[i]-incremento,i])
                
                
                if(h1 > h2):

                    tablero[i] = tablero[i]-incremento
                    incremento = 0
                incremento+=1
            incremento=0
            while(tablero[i]+incremento < len(tablero)):
                h1=heuristica(tablero,[tablero[i],i])
                h3=heuristica(tablero,[tablero[i]+incremento,i])
                if h1>h3:

                        tablero[i] = tablero[i]+incremento
                        incremento = 0

                incremento += 1

            count+=1
    return tablero


def Simulated(array):
    tablero=copy.deepcopy(array)
    count=0
    temperatura=100
    while count<1000:
     # print(count)
        reinas=0
        for i in range(0,len(tablero)):
            h=heuristica(tablero,[tablero[i],i])
            if h==0:
                reinas+=1
        if reinas==len(tablero):
            iteracionesSimulated.append(count)
            return tablero
        for i in range(0,len(tablero)):
        #print(i)
        
            incremento = 0
            while(tablero[i]-incremento >= 0):
                temperatura*=0.99
                h1=heuristica(tablero,[tablero[i],i])
                if h1!=0:

                    h2=heuristica(tablero,[tablero[i]-incremento,i])
                    
                    
                    if(h1 > h2):

                        tablero[i] = tablero[i]-incremento
                        incremento = 0
                    else:
                        delta=h2-h1
                        #if delta>=0: #si fuese menor solo continua, si es mayor a 0 tomamos con probabilidad
                        if (random.uniform(0,1)< (math.exp(-delta*temperatura))):
                            tablero[i] = tablero[i]-incremento
                            

                incremento+=1
            incremento=0
            while(tablero[i]+incremento < len(tablero)):
                temperatura*=0.99
                h1=heuristica(tablero,[tablero[i],i])
                if h1!=0:
                    h3=heuristica(tablero,[tablero[i]+incremento,i])
                    if h1>h3:

                            tablero[i] = tablero[i]+incremento
                            incremento = 0
                    else:
                        delta=h3-h1
                        #if delta>=0: #si fuese menor solo continua, si es mayor a 0 tomamos con probabilidad
                        if (random.uniform(0,1)< (math.exp(-delta*temperatura))):
                            tablero[i] = tablero[i]+incremento
                            
                        
                incremento += 1
            
        
            count+=1

    return tablero





size=8

estados=list(range(size))

solucionesH=0
solucionesSimulated=0
timeHill=[]
timeS=[]
iteracionesSimulated=[]
iteracionesHill=[]
for j in range(0,30):
    random.shuffle(estados)
    startH = time()
    ArrayHill= HillClimb(estados)
    reinashill=0
    for i in range(0,len(ArrayHill)):
        h=heuristica(ArrayHill,[ArrayHill[i],i])
        if h==0:
            reinashill+=1

    if reinashill==size:
        #print("Array Hill: ",ArrayHill)
        solucionesH+=1
        endH=time()
        timeHill.append(endH-startH)
    startS = time()
    ArraySimulated= Simulated(estados)
    reinasSimulated=0
    
    for i in range(0,len(ArraySimulated)):
        h2=heuristica(ArraySimulated,[ArraySimulated[i],i])
        if h2==0:
            reinasSimulated+=1

    if reinasSimulated==size:
        
        solucionesSimulated+=1
        endS=time()
        timeS.append(endS-startS)

print(".................")
print("              HILL CLIMB ")
print("Cantidad de soluciones Hill Climbing: ",solucionesH)
promedio=(solucionesH*100)/30
print("Promedio Hill Climbing: ", promedio)
print("Tiempos de hill climbing: ",timeHill)
print("Tiempo promedio Hill climb: ",statistics.mean(timeHill))
print("Tiempo maximo: ",max(timeHill))
print("Tiempo minimo: ",min(timeHill))
print("Cuartiles 1: ",numpy.percentile(timeHill,25))
print("Cuartiles 3: ",numpy.percentile(timeHill,75))
if len(timeHill)>1:
    print("Desviacion estandar de tiempo Hill climb: ",statistics.stdev(timeHill))
print("Array de estados para encontrar las soluciones Hill Climb: ",iteracionesHill)
print("La cantidad de estados previos promedio Hill Climb: ",statistics.mean(iteracionesHill))
if len(iteracionesHill)>1:
    print("La desviacion estandar de estados previos Hill Climb: ",statistics.stdev(iteracionesHill))
print("")
print(".................")
print("              Simulated ")
print("Cantidad de soluciones Simulated: ",solucionesSimulated)
promedioSimultaed=(solucionesSimulated*100)/30
print("Promedio Simulated: ", promedioSimultaed)
print("Tiempos de Simulated: ",timeS)
print("Tiempo promedio Simulated: ",statistics.mean(timeS))
print("Tiempo maximo: ",max(timeS))
print("Tiempo minimo: ",min(timeS))
print("Cuartiles 1: ",numpy.percentile(timeS,25))
print("Cuartiles 3: ",numpy.percentile(timeS,75))
if len(timeS)>1:
    print("Desviacion estandar de tiempo Simulated: ",statistics.stdev(timeS))
print("Array de estados para encontrar las soluciones Simulated: ",iteracionesSimulated)
print("La cantidad de estados previos promedio Simulated: ",statistics.mean(iteracionesSimulated))
if len(iteracionesSimulated)>1:
    print("La desviacion estandar de estados previos Simulated: ",statistics.stdev(iteracionesSimulated))


print(".................")
print("              GENETICO ")
#dimension = int(input("Enter board dimension: "))


solucionesTOTALES =0
tiemposGenetico=[]
iter=30
for j in range(0,iter):
    chess = GeneticChess(size)
    #print(j)
    start = time()
    solution=chess.solveGA()
    if solution==False:
        continue
    else:
        solucionesTOTALES+=1
        end =time()
        tiemposGenetico.append(end-start)


print("Cantidad de soluciones Genetico:  ",solucionesTOTALES)
promedioGenetico=(solucionesTOTALES*100)/iter
print("Promedio Genetico: ", promedioGenetico)
print("Tiempos de Genetico: ",tiemposGenetico)
print("Tiempo promedio Genetico: ",statistics.mean(tiemposGenetico))
print("Tiempo maximo: ",max(tiemposGenetico))
print("Tiempo minimo Genetico: ",min(tiemposGenetico))
print("Cuartiles 1: ",numpy.percentile(tiemposGenetico,25))
print("Cuartiles 3: ",numpy.percentile(tiemposGenetico,75))
if len(tiemposGenetico)>1:
    print("Desviacion estandar de tiempo Genetico: ",statistics.stdev(tiemposGenetico))
print("La cantidad de estados previos promedio: ",statistics.mean(cantidadEstadosGenetico))
if len(cantidadEstadosGenetico)>1:
    print("La desviacion estandar de estados previos: ",statistics.stdev(cantidadEstadosGenetico))
