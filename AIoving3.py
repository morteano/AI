from sys import stdin
import collections

#estimates the Manhatten distance between pos and goalPos
def estimatedPath(pos,goalPos):
    estimatedCost=abs(pos[0]-goalPos[0])+abs(pos[1]-goalPos[1])
    return estimatedCost

#Converts the map from text to a matrix where # gets the value -1
def makeMap():
    available = 1
    unavailable = -1
    start = 'A'
    goal = 'B'
    
    map=[]
    rowCounter=0
    for linje in stdin:
        temp=[]
        for j in linje:
            if j == '.':
                temp.append(available)
            elif j == start:
                temp.append(start)
            elif j == goal:
                temp.append(goal)
            else:
                temp.append(unavailable)
        rowCounter+=1
        map.append(temp)
    return map


class Node(object):
    def __init__(self, position):
        pos = position
        print pos
        weight = None
        parent = None
        kids = []

node2 = Node((2,1))
node = Node((2,3))
nodeFar = Node((2,2))
node.pos = (2,3)
nodeFar.pos = (2,2)
node.parent = nodeFar
nodeFar.kids = node
print makeMap()
print node.parent.pos
print nodeFar.kids.pos