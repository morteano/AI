from sys import stdin
import collections
import heapq

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
    
    # Create first dimention of a two dimentional 
    # array for internal representation of the map.
    map=[]
    
    # Create dictionary to hold the cost of different terrains
    terrainCost = {'A':0, 'B':0, 'w':100, 'm':50, 'f':10, 'g':5, 'p':1, '.':1, '#':1000}

    # Init helper variables
    startPos = None
    endPos = None
    row = 0
    col = 0
    
    # Read from file and fill the internal map with desired values.
    for textLine in stdin:
        mapVertical = []
        for symbol in textLine:          
            if symbol != '\n':
                node=Node()
                node.pos = (row,col)
                node.singleNodeCost = terrainCost[symbol]
                node.pastTravelCost = 0
                node.parent = None
                mapVertical.append(node)
                if symbol == 'A':
                    startPos = node.pos
                elif symbol == 'B':
                    endPos = node.pos
                col += 1
            else:
                col = 0
        row += 1
        map.append(mapVertical)
    #return the two dimentional array whth mapped values
    print "inside makeMap, startpos and endpos:"
    print (startPos,endPos)
    return [map,startPos,endPos]

def getShortestPath(map, startPos, endPos):
    
    sortedEstimateCosts = []
    visited =[]
    
    # Start at the beginning
    this = map[startPos[0]][startPos[1]]
#    this.totalEstimateCost = getManhattenDistance(this.pos, end.pos)
    visited.append(this)

    # Untill target is reached
    while this.pos != endPos:

        # Update values on all sides
        print "firing updateNeighbours with this.pos: "
        print this.pos
        updateNeighbours(this, map, sortedEstimateCosts, visited, endPos)

        # Pick the cheapest seen but unvisited node
        (estimatedCost, this) = heapq.heappop(sortedEstimateCosts)
        visited.append(this)

    # Reached the target node
    totalCost = this.pastTravelCost

    # Backtrace to get path
    path = []
    print "starting backtracing from __ to __:"
    print (this.pos, startPos)
    
    while this.pos != startPos:
        path.append(this)
        print "adding pos to path: "
        print this.pos
        this = this.parent

    # Reverse path
        
    return (path, totalCost)

def updateNeighbours(node, map, sortedEstimateCosts, visited,endPos):
    print "updateNeighbours fired with node.pos:"
    print node.pos
    
    # Get current map position
    x = node.pos[0]
    y = node.pos[1]
    
    # Define boundries
    xMax = len(map)-1
    yMax = len(map[0])-1
    print "max values for X and Y is:" 
    print (xMax,yMax)
    
    #  Create neighbourhoodfor this node    
    neighbourhood = []
    
    # Only add existing neighboursto the neigbourhood
    if x is not 0:
        neighbourhood.append(map[x-1][y])
        print "n added, not x0"
              
    if x is not xMax:
       neighbourhood.append(map[x+1][y])
       print "n added, not xMax"
          
    if y is not 0:
        neighbourhood.append(map[x][y-1])
        print "n added, not y0"
          
    if y is not yMax:
        neighbourhood.append(map[x][y+1])
        print "n added, not yMax"
    
    # Update all neighbours in neighbourhood and sort them by totalEstimateCost in a heap      
    
    for neighbour in neighbourhood:
        print "looking at n with pos:"  
        print neighbour.pos
        if neighbour not in visited:
            # Who's your daddy?
            if neighbour.parent == None:
                neighbour.parent = node
            # Update estimated path cost, and add to heap
            neighbour.pastTravelCost= node.pastTravelCost+neighbour.singleNodeCost
            totalEstimateCost = neighbour.pastTravelCost+getManhattenDistance(neighbour.pos,endPos)
            heapq.heappush(sortedEstimateCosts,(totalEstimateCost,neighbour))
    
class Node(object):
    def __init__(self):
        pos = None
        singleNodeCost = None
        pastTravelCost = None
        parent = None


node = Node()
node.pos = (3,0)

[map,startPos,endPos]=makeMap()

(path, cost) = getShortestPath(map, startPos, endPos)
print "path was: "
for node in path:
  print node.pos