__author__ = 'gaoboning'
import random

letters = ['A','B','C','D']
#diamondTable = []
diamondTable =  [['C', 'D', 'D', 'B', 'B', 'C', 'A', 'B', 'B', 'A'],
                 ['A', 'C', 'B', 'C', 'D', 'B', 'A', 'B', 'B', 'B'],
                 ['D', 'B', 'C', 'D', 'B', 'A', 'A', 'C', 'B', 'A'],
                 ['D', 'D', 'C', 'D', 'D', 'A', 'A', 'A', 'A', 'A'],
                 ['A', 'D', 'A', 'D', 'C', 'D', 'D', 'B', 'A', 'A'],
                 ['A', 'D', 'B', 'C', 'C', 'D', 'B', 'D', 'C', 'C'],
                 ['C', 'D', 'A', 'A', 'B', 'A', 'A', 'A', 'C', 'C'],
                 ['D', 'B', 'D', 'A', 'C', 'D', 'C', 'A', 'C', 'C'],
                 ['A', 'D', 'C', 'A', 'B', 'B', 'C', 'D', 'D', 'D'],
                 ['D', 'B', 'C', 'A', 'A', 'D', 'B', 'B', 'D', 'A']]
resultTable = [] #result of horizon match

# diamondTable = [
#     [0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0],
# ]


def initTable(n):
    global N
    N = n
    for i in range(0, n):
        tmp = []
        zeros = []
        for j in range(0, n):
            tmp.append(letters[random.randint(0,3)])
            zeros.append(0)
        diamondTable.append(tmp)
        resultTable.append(zeros)


def printTable(table):
    for i in range(0, len(table)):
        for j in range(0, len(table[0])):
            print table[i][j],
        print '\n',



def detectTable(setlist):
    N = 10
    if(len(diamondTable) == 0):
        print "Table not initial successfully!"
    else:
        for i in range(0, N):
            for j in range(0, N):
                #detect the horizon match
                if j < N - 2:
                    (a, b, c) = (diamondTable[i][j], diamondTable[i][j+1], diamondTable[i][j+2])
                    if a == b and b == c:
                        matchset = set([(i,j),(i,j+1),(i,j+2)])
                        for t in range(j+3, N):
                            if diamondTable[i][t] == a:
                                matchset.add((i,t))
                            else:
                                break

                        # repeat = 0
                        # for w in setlist:
                        #     if matchset & w != set([]):
                        #         setlist.remove(w)
                        #         matchset = matchset | w
                        #
                        #         repeat = 1
                        # if repeat == 0:
                        #     setlist.append(matchset)
                        removeRepeat(matchset, setlist)

                #detect the vertical match

                if i < N - 2:
                    (a, b, c) = (diamondTable[i][j], diamondTable[i+1][j], diamondTable[i+2][j])
                    if a == b and b == c:
                        matchset = set([(i,j),(i+1,j),(i+2,j)])
                        for t in range(i+3, N):
                            if diamondTable[t][j] == a:
                                matchset.add((t,j))
                            else:
                                break

                        # repeat = 0
                        # for w in setlist:
                        #     if matchset & w != set([]):
                        #         setlist.append(w | matchset)
                        #         setlist.remove(w)
                        #         repeat = 1
                        # if repeat == 0:
                        #     setlist.append(matchset)
                        removeRepeat(matchset, setlist)

def removeRepeat(set_i, list_i):
    repeat = 0
    for w in list_i:
        if set_i & w != set([]):
            set_i |= w
            list_i.remove(w)
            repeat = 1
        if(removeRepeat(set_i,list_i) == 0):
            list_i.append(set_i)
    return repeat



#initTable(10)
print"\n-----------Diam-----------\n"
printTable( diamondTable)
set_temp = []
detectTable(set_temp)
for w in set_temp:
    print w,
    position = w.pop()
    print diamondTable[position[0]][position[1]]

