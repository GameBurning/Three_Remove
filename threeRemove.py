__author__ = 'gaoboning'
import random

#Store the same letters
class group():
    def __init__(self):
        self.letter = ['0']
        self.number = 0
        self.list = [(0,0)]
    def appendLetter(self, l_in):
        self.letter = l_in
    def appendList(self, l_in):
        self.list.append(l_in)
    def printOut(self):
        print "\n------------------\nLetter:"+self.letter+"\nList:"+self.list+"\n"

letters = ['A','B','C','D']
diamondTable = []

resultTable_Hori = [] #result of horizon match
resultTable_Vert = [] #result of vertical match
#global N #rows and lines


def initTable(n):
    global N
    N = n
    for i in range(0, n):
        tmp = []
        zerosHori = []
        zerosVert = []
        for j in range(0, n):
            tmp.append(letters[random.randint(0,3)])
            zerosHori.append(0)
            zerosVert.append(0)
        diamondTable.append(tmp)
        resultTable_Hori.append(zerosHori)
        resultTable_Vert.append(zerosVert)
    #for i in range(0, n):
    #    print Diamond_table[i][:]

def printTable(table):
    for i in range(0, len(table)):
        for j in range(0, len(table)):
            print table[i][j],
        print '\n',



def detectTable():
    number = 1
    if(len(diamondTable) == 0):
        print "Table not initial successfully!"
    else:
        for i in range(0, N-2):
            for j in range(0, N-2):
                #detect the horizon match
                if(resultTable_Hori[i][j] == 0):
                    (a, b, c) = (diamondTable[i][j], diamondTable[i][j+1], diamondTable[i][j+2])
                    if a == b and b == c:
                        resultTable_Hori[i][j] = (number, a)
                        resultTable_Hori[i][j+1] = (number, a)
                        resultTable_Hori[i][j+2] = (number, a)
                        for t in range(j+3, N-2):
                            if diamondTable[i][t] == a:
                                resultTable_Hori[i][t] = (number, a)
                            else:
                                break
                        number += 1


                #detect the vertical match
                '''use even number to store horizon match and odd number to store vertical match'''
                if(resultTable_Vert[i][j] == 0):
                    (a, b, c) = (diamondTable[i][j], diamondTable[i+1][j], diamondTable[i+2][j])
                    if a == b and b == c:
                        resultTable_Vert[i][j] = (number, a)
                        resultTable_Vert[i+1][j] = (number, b)
                        resultTable_Vert[i+2][j] = (number, c)
                        for t in range(i+3, N-2):
                            if diamondTable[t][j] == a:
                                resultTable_Vert[t][j] = (number, a)
                            else:
                                break
                        number += 1



initTable(10)
print"\n-----------Diam-----------\n"
printTable(diamondTable)
detectTable()
print"\n-----------Hori-----------\n"
printTable(resultTable_Hori)
print"\n-----------Vert-----------\n"
printTable(resultTable_Vert)
