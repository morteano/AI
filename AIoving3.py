from sys import stdin
import collections

#estimates the Manhatten distance between pos and goalPos
def estimatedPath(pos,goalPos):
    estimatedCost=abs(pos[0]-goalPos[0])+abs(pos[1]-goalPos[1])
    return estimatedCost

#checks if current position is the goal node
def goalTest(pos, map):
    x=pos[0]
    y=pos[1]
    return map[x][y]=='B'

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
    def __init__(self):
        pos = None
        weight = None
        parent = None
        kids = []


node = Node()
node.pos = (2,3)

map=makeMap()

print goalTest(node.pos,map)
node.pos = (3,17)
print goalTest(node.pos,map)