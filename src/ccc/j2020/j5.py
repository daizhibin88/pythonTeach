import sys
#sys.setrecursionlimit(8192*64)
class j5:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.matrix = list()
    # def showMatrix(self):
    #     print(self.matrix)
    def setData(self, m, n, matrix):
        self.m = m
        self.n = n
        self.matrix = matrix

    def getData(self):
        return (self.m , self.n, self.matrix)

    def setDataByInput(self):
        m = int(input())
        n = int(input())
        matrix = list()
        for i in range(m):
            inputStr = input()
            datastr:list = inputStr.split(' ')
            #matrix.append([int(data) for data in datastr])
            listinMatrix = list()
            for j in range(len(datastr)):
                listinMatrix.append( int(datastr[j]))
            matrix.append(listinMatrix)
        self.setData(m ,n , matrix)

    def generateMap(self):
        mapDataLocation = dict()
        for r in range(self.m):
            for c in range(self.n):
                data = self.matrix[r][c]
                setfordata = mapDataLocation.get(data)
                if setfordata is None:
                    setfordata = set()
                    mapDataLocation[data] = setfordata
                setfordata.add((r + 1) * (c + 1))
        return mapDataLocation

    def checkpathByRecusive(self):
        mapDataLocation = self.generateMap()
        def findout(startdata: int, passeddata: set) -> bool:
            end = 1
            passeddata.add(startdata)
            listdata = mapDataLocation.get(startdata)
            if listdata == None:
                return False
            else:
                for element in listdata:
                    if element == end:
                        return True
                    else:
                        if element not in passeddata:
                            if findout(element, passeddata):
                                return True
                return False
        start = self.m * self.n
        passed = set()
        return findout(start, passed)

    def checkpathByStack(self):
        mapDataLocation = self.generateMap()
        passed = set()
        stack = []
        stack.append(self.m * self.n)
        while len(stack) > 0 :
            start = stack.pop()
            passed.add(start)
            if start == 1:
                return  True
            else:
                listdata = mapDataLocation.get(start)
                if listdata is not None:
                    for ele in listdata:
                        if ele not in passed:
                            stack.append(ele)
                    #[stack.append(ele) for ele in listdata]
                    #[stack.append(element) for element in listdata if element not in passed]
        return False

if __name__ == '__main__':
    question = j5()
    question.setDataByInput()
    result =question.checkpathByStack()
    print("yes") if result else print('no')