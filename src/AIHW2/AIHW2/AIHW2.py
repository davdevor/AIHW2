import sys
import copy
import timeit
class HW2:
    n=0
    matrix = []
    matrixCopy = []
    sumRows = []
    sumColumns = []
    sumDiagonals = []
    freeSpaces = []
    nodesVisited = []
    def __init__(self, **kwargs):
        self.readData(kwargs['fileName'])
        return super().__init__()

    def readData(self,fileName):
        file = open(str(fileName),'r')
        n = self.n = int(file.readline())
        self.matrix = [[0 for x in range(self.n)] for y in range(self.n)]
       
        for x in range(n):
            line = file.readline()
            line = line.split(' ')
            for y in range(n):
                num = int(line[y])
                if(num != -1):
                    self.matrix[x][y] = int(line[y])
                else:
                    self.freeSpaces.append([x,y])
                    self.matrix[x][y] = 0

        self.matrixCopy = copy.deepcopy(self.matrix)
        line = file.readline()
        line = line.split(' ')
        for x in line:
            self.sumRows.append(int(x))

        line = file.readline()
        line = line.split(' ')
        for x in line:
            self.sumColumns.append(int(x))

        line = file.readline()
        line = line.split(' ')
        for x in line:
            self.sumDiagonals.append(int(x))

    def generateNodes(self, node):
        nodes = []
        
        for x in self.freeSpaces:
            newNode = copy.deepcopy(node)
            num = newNode[x[0]][x[1]] + 1
            if(num <= 9):
                newNode[x[0]][x[1]] = num
                if(newNode not in self.nodesVisited):
                    nodes.append(newNode)
                    self.nodesVisited.append(newNode)
        return nodes

    def isGoal(self,matrix):
        n = self.n
        # check row sum
        rowSum = 0
        i = 0
        # check if row sums equal right number
        for row in matrix:
            for x in row:
                rowSum += x
            if(rowSum!=self.sumRows[i]):
                return False
            i += 1
            rowSum = 0

        colSum = 0
        #check if col sums equal right number
        for i in range(n):
            for j in range(n):
               colSum += matrix[j][i]

            if(colSum!=self.sumColumns[i]):
                return False
            colSum = 0

        diagSum =0
        #check major diagonal
        for i in range(n):
            diagSum += matrix[i][i]
        if(diagSum!= self.sumDiagonals[0]):
            return False
        diagSum=0
        
        y = n-1
        for x in range(n):
            diagSum+= matrix[x][y]
            y-=1
        if(diagSum!= self.sumDiagonals[1]):
            return False
        return True
        

    def getSolution(self,currentNode):
        if(self.isGoal(currentNode)):
            print(currentNode)
            return True
        else:
            possibleNodes = self.generateNodes(currentNode)
            if (len(possibleNodes)==0):
                return False
            for x in possibleNodes:
                if (self.getSolution(x)):
                    return True

    def getMatrix(self):
        return self.matrixCopy


def main():
    start = timeit.timeit()
    obj = HW2(fileName = 'test.txt')
    print(obj.getSolution(obj.getMatrix()))
    end = timeit.timeit()
    print(end-start)
main()