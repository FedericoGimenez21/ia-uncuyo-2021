from time import time

import numpy as np
class Unassigned:

    def __init__(self, row, column):
        self.row = row
        self.column = column

def solveNQueensForwardChecking(grid, queen):
    if len(grid) == queen:
        #print (grid)
        return True
    rowsProposition = getRowsProposition(grid, queen)
    for row in rowsProposition:
        
        grid[row][queen] = 1
        domainWipeOut = False
        
        for variable in getUnassignedFromConstraint(grid, queen):
            iteracionArray[0]+=1
            if fc(grid, variable.row, variable.column):
                domainWipeOut = True
                break
        if not domainWipeOut:
            if solveNQueensForwardChecking(grid, queen + 1):
                return True
        grid[row][queen] = 0


def getUnassignedFromConstraint(grid, queen):
    result = []
    for row in range(len(grid)):
        for col in range(queen+1, len(grid)):
            if grid[row][queen] == 0 and isCorrect(grid, row, col):
                result.append(Unassigned(row, col))
    return result


def fc(grid, row, queen):
    actualDomain = getRowsProposition(grid, queen)
    tempDomain = list(actualDomain)
    for propositionRow in actualDomain:
        if not isCorrect(grid, propositionRow, queen):
            tempDomain.remove(propositionRow)
    return len(tempDomain) == 0



def isCorrect(grid, row, column):
    return isRowCorrect(grid,row) and  isColumnCorrect(grid, column) and isDiagonalCorrect(grid, row, column)

def isRowCorrect(grid, row):
    
    for col in range(len(grid)):
        if grid[row][col] == 1:
            return False
    return True

def isColumnCorrect(grid, column):
    for row in range(len(grid)):
        if grid[row][column] == 1:
            return False
    return True


def checkUpperDiagonal(grid, row, column):
    iterRow = row
    iterCol = column
    while iterCol >= 0 and iterRow >= 0:
        if grid[iterRow][iterCol] == 1:
            return False
        iterCol -= 1
        iterRow -= 1
    return True


def checkLowerDiagonal(grid, row, column):
    iterRow = row
    iterCol = column
    while iterCol >= 0 and iterRow < len(grid):
        if grid[iterRow][iterCol] == 1:
            return False
        iterRow += 1
        iterCol -= 1
    return True


def isDiagonalCorrect(grid, row, column):
    return checkUpperDiagonal(grid, row ,column) and checkLowerDiagonal(grid, row, column)


def getRowsProposition(grid, queen):
    rows = []
    for row in range(len(grid)):
        if isCorrect(grid, row, queen):
            rows.append(row)
    return rows


queens=[4,8,10,12,15]
times=[0]*5
iteracionestotales=[0]*5
print(len(times))
if __name__ == "__main__":
    for k in range(0,len(queens)):

        iteracionArray=[0]*1
        
        N=queens[k]
        board=np.array(np.zeros(shape = (N,N), dtype=int))

        start=time()
        solved = solveNQueensForwardChecking(board,0)
        end=time()

        if solved:
            #print("Tiempo ejecucion: ",end-start)
            times[k]=end-start
            #print("iteracion: ",iteracionArray[0])
            iteracionestotales[k]=iteracionArray[0]
            #for i in range(len(board)):
                #print(board[i])

print("Tiempos: ",times)
print("Iteraciones: ",iteracionestotales)
