import sys
import copy
import time
class HW2:
    n=0
    matrix = []
    matrixCopy = []
    sumRows = []
    sumColumns = []
    sumDiagonals = []
    freeSpaces = []
    visited = []
    answer = []
    foundGoal = False
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
                    self.matrix[x][y] = -1

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
        file.close()
    def generateNodes(self, node):
        nodes = []
        
        for x in self.freeSpaces:
            newNode = copy.deepcopy(node)
            num = newNode[x[0]][x[1]] + 1
            if(num <= 9):
                newNode[x[0]][x[1]] = num
                if(not newNode in self.visited):
                    nodes.append(newNode)
                    self.visited.append(newNode)
        return nodes




    def bestOrder(self,list):
        n = self.n
        values = []
        # check row sum
        pos =0
        for matrix in list:
            count = 0
            rowSum = 0
            i = 0
            remove = False

            # check if row sums equal right number
            for row in matrix:
                for x in row:
                    rowSum += x
                if(rowSum>self.sumRows[i]):
                    remove = True
                    break
                if(rowSum==self.sumRows[i]):
                    count +=1
                i += 1
                rowSum = 0

            if(remove):
                list.remove(matrix)
                continue

            colSum = 0
            #check if col sums equal right number
            for i in range(n):
                for j in range(n):
                   colSum += matrix[j][i]
                if(colSum>self.sumColumns[i]):
                    remove = True
                    break
                if(colSum==self.sumColumns[i]):
                    count+=1
                colSum = 0

            if(remove):
                list.remove(matrix)
                continue

            diagSum = 0
            #check major diagonal
            for i in range(n):
                diagSum += matrix[i][i]
            if(diagSum > self.sumDiagonals[0]):
                list.remove(matrix)
                continue
            if(diagSum== self.sumDiagonals[0]):
                count+=1
            diagSum=0
        
            y = n-1
            for x in range(n):
                diagSum+= matrix[x][y]
                y-=1
            if(diagSum> self.sumDiagonals[1]):
                list.remove(matrix)
                continue
            if(diagSum== self.sumDiagonals[1]):
                count+=1
            if(count == self.n*2 + 2):
                self.answer = copy.deepcopy(matrix)
                self.foundGoal = True
                return []
            values.append([count,pos])
            pos +=1
        values.sort(reverse=True)
        newList = []
        for x in values:
            newList.append(list[x[1]])
        return newList

    #def pruneList(self,list):
    #    n = self.n
    #    # check row sum
        
    #    # check if row sums equal right number
    #    for matrix in list:
    #        remove = False
    #        rowSum = 0
    #        i = 0
    #        for row in matrix:
    #            for x in row:
    #                rowSum += x
    #            if(rowSum>self.sumRows[i]):
    #                remove = True
    #                break
    #            i += 1
    #            rowSum = 0
    #        if(remove):
    #            list.remove(matrix)
    #            continue
    #        colSum = 0
    #        #check if col sums equal right number
    #        for i in range(n):
    #            for j in range(n):
    #               colSum += matrix[j][i]

    #            if(colSum>self.sumColumns[i]):
    #                remove = True
    #                break
    #            colSum = 0
    #        if(remove):
    #            list.remove(matrix)
    #            continue

    #        diagSum =0
    #        #check major diagonal
    #        for i in range(n):
    #            diagSum += matrix[i][i]
    #        if(diagSum > self.sumDiagonals[0]):
    #            list.remove(matrix)
    #            continue
    #        diagSum=0
        
    #        y = n-1
    #        for x in range(n):
    #            diagSum+= matrix[x][y]
    #            y-=1
    #        if(diagSum> self.sumDiagonals[1]):
    #            list.remove(matrix)
    #            continue
    #    return list

    def getSolution(self,currentNode):
        queue = []
        queue.append(currentNode)
        self.visited.append(currentNode)
        while(len(queue)>0):
            node = queue.pop()
            
            list = self.generateNodes(node)
            #list = self.pruneList(list)
            list = self.bestOrder(list)
            self.answer
            if(self.foundGoal):
                return True
            for x in list:
                queue.append(x)
                

            
        return False

    def getMatrix(self):
        return self.matrixCopy
    def getAnswer(self):
        return self.answer

def main():
    start = time.time()
    obj = HW2(fileName = 'sample1.txt')
   # matrix = [[[1,7],[9,8]]]
    #matrix = obj.bestOrder(matrix)
    #print(matrix)
    print(obj.getSolution(obj.getMatrix()))
    end = time.time()
    print(obj.getAnswer())
    print(end-start)
main()