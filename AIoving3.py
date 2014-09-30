from sys import stdin
import collections
import heapq
import time

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
    terrainCost = {'A':0, 'B':0, 'w':100, 'm':50, 'f':10, 'g':5, '.':1, 'r':2, '#':10000}

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
    return [map,startPos,endPos]

def getShortestPath(map, startPos, endPos, algorithm):
    
    openNodes = []
    closedNodes =[]
    seen = []
    
    # Start at the beginning
    this = map[startPos[0]][startPos[1]]
    closedNodes.append(this)
    seen.append(this)

    # Untill target is reached
    while this.pos != endPos:

        # Update values on all sides
        updateNeighbours(this, map, endPos, algorithm, openNodes, seen)

        # Pick the cheapest seen but unvisited node
        if algorithm == "A_star" or algorithm == "Dijkstra":
            (estimatedCost, this) = openNodes.pop(0)
        elif algorithm == "BFS":
            this = openNodes.pop()
        closedNodes.append(this)
        
        #printPath(map, seen, closedNodes, [])
        #time.sleep(2) 

    # Reached the target node
    totalCost = this.pastTravelCost

    # Backtrace to get path
    path = []
    
    while this.pos != startPos:
        path.append(this)
        this = this.parent
    
    # Reverse path
    return (seen, closedNodes, path, totalCost)

def updateNeighbours(node, map, endPos, algorithm, openNodes, seen):
    
    # Get current map position
    x = node.pos[0]
    y = node.pos[1]
    
    # Define boundries
    xMax = len(map)-1
    yMax = len(map[0])-1
    
    #  Create neighbourhoodfor this node    
    neighbourhood = []
    
    # Only add existing neighboursto the neigbourhood
    if x is not 0:
        neighbourhood.append(map[x-1][y])
              
    if x is not xMax:
       neighbourhood.append(map[x+1][y])
          
    if y is not 0:
        neighbourhood.append(map[x][y-1])
          
    if y is not yMax:
        neighbourhood.append(map[x][y+1])
    
    # Update all neighbours in neighbourhood and sort them by totalEstimateCost in a heap      
    
    for neighbour in neighbourhood:
        if neighbour not in seen:
            # Who's your daddy?
            if neighbour.parent == None:
                neighbour.parent = node
            # Update estimated path cost, and add to heap
            neighbour.pastTravelCost= node.pastTravelCost+neighbour.singleNodeCost
            if algorithm == "A_star":
                totalEstimateCost = neighbour.pastTravelCost+getManhattenDistance(neighbour.pos,endPos)
                if neighbour.singleNodeCost < 10000:
                    insertInList(openNodes, (totalEstimateCost, neighbour))
            elif algorithm == "Dijkstra":
                if neighbour.singleNodeCost < 10000:
                    totalEstimateCost = neighbour.pastTravelCost
                    heapq.heappush(openNodes,(totalEstimateCost,neighbour))
            elif algorithm == "BFS":
                if neighbour.singleNodeCost != 10000:
                    openNodes.insert(0,neighbour)
            seen.append(neighbour)

#prints the map with path marked as 'O'
def printPath(map, seen, closedNodes, path):
    terrainCost = {10000:'#', 100:'w', 50:'m', 10:'f', 5:'g', 1:'.', 2:'r', 0:'O'}
    for nodeGroup in map:
        line = ""
        for node in nodeGroup:
            if node in path:
                line+='O'
            elif node in closedNodes:
                line+='x'
            elif node in seen and node.singleNodeCost != 10000:
                line+='-'
            else:
                line += terrainCost[node.singleNodeCost]
        print line

def insertInList(openNodes, (cost, element)):
    if len(openNodes) > 0:
        i = 0
        while cost > openNodes[i][0] and i<len(openNodes)-1:
            i += 1
        if i==len(openNodes)-1:
            i += 1
        openNodes.insert(i, (cost, element))
    else:
        openNodes.insert(0, (cost, element))
    
class Node(object):
    def __init__(self):
        pos = None
        singleNodeCost = None
        pastTravelCost = None
        parent = None

[map,startPos,endPos]=makeMap()

(seen, closedNodes, path, cost) = getShortestPath(map, startPos, endPos, "A_star")

print "path was: "
printPath(map, seen, closedNodes, path)