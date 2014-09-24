from sys import stdin
import collections

# Estimates the Manhatten distance between pos and goalPos
def getManhattenDistance(pos,goalPos):
    estimatedCost=abs(pos[0]-goalPos[0])+abs(pos[1]-goalPos[1])
    return estimatedCost

# Checks if current position is the goal node
def goalTest(pos, map):
    x=pos[0]
    y=pos[1]
    return map[x][y]=='B'

# Converts the map from text to a matrix where # gets the value -1
def makeMap():
    # Symbols used in the map and their corresponding values.
    available = 1
    unavailable = -1
    start = 'A'
    goal = 'B'
    
    # Create first dimention of a two dimentional 
    # array for internal representation of the map.
    map=[]

    # Read from file and fill the internal map with desired values.
    for textLine in stdin:
        temp=[]
        for symbol in textLine:
            if symbol == '.':
                temp.append(available)
            elif symbol == start:
                temp.append(start)
            elif symbol == goal:
                temp.append(goal)
            else:
                temp.append(unavailable)
        map.append(temp)
        
    #return the two dimentional array whth mapped values
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
