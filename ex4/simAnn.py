from random import random
from random import randrange
from copy import deepcopy
from math import exp
from math import floor
from time import sleep

# Add k eggs in each row
def getStartSolutionByRows(n,k):
    solution = []
    for i in range(n):
        solution.append([0]*n)
    for row in solution:
        eggsPlaced = 0
        while eggsPlaced < k:
            candidate = randrange(n)
            if row[candidate] == 0:
                row[candidate]=1
                eggsPlaced += 1
    return solution

# Add n*k eggs randomly in the carton
def getStartSolution(n,k):
    solution = []
    for i in range(n):
        solution.append([0]*n)
    eggsPlaced = 0
    while eggsPlaced < k*n:
        x = int(random()*n)
        y = int(random()*n)
        if solution[x][y] == 0:
            solution[x][y] = 1
            eggsPlaced += 1
    return solution

# Return the diagonal going south east, and consisting of the element with coordinates row, col
def getDiagDecrease(row, col, matrix, n):
    list = []
    while row < n and col < n:
        list.append(matrix[row][col])
        row+=1
        col+=1
    return list

# Return the diagonal going south west, and consisting of the element with coordinates row, col
def getDiagIncrease(row, col, matrix, n):
    list = []
    while (row < n) and (col >= 0):
    #    print j
        list.append(matrix[row][col])
        row+=1
        col-=1
    return list

def getScore(solution, k):
    scoresPartial = []
    score = 0.0
    n = len(solution)

    # for each element in a row or col
    for i in range(n):
        #add row
        scoresPartial.append(solution[i])

        #add col
        col = []
        for j in range(n):
            col.append(solution[j][i])
        
        scoresPartial.append(col)

        #add diagonals
        scoresPartial.append(getDiagDecrease(0,i,solution,n))
        scoresPartial.append(getDiagDecrease(i+1,0,solution,n))

        scoresPartial.append(getDiagIncrease(i,n-1,solution,n))
        scoresPartial.append(getDiagIncrease(0,i-1,solution,n))

    # Give credit when credit is due
    for scorePartial in scoresPartial:
        # Award for each partial without too many eggs
        if (sum(scorePartial) <= k) and (len(scorePartial) > 0):
            score += 1
        # Punish for each extra egg in a partial
        elif (sum(scorePartial) > k):
            extraEggs = sum(scorePartial)-k
            score -= extraEggs
    
    # Perfect score
    perfectScore = (4+(n-1)*6)
    
    # Return score in percent of maximum score
    return (score/perfectScore*100)
    
def getNeighbours(x,y,solution):
    #Create the neighbours

    # Define boundries
    nMax = len(solution)-1

    #  Create neighbourhood for this solution    
    neighbourhood = []
    #print "inside getNeighbours"

    # Only add existing neighbours to the neigbourhood
    if x is not 0:
        #print "inside x not 0"
        neighbour = deepcopy(solution)
        if neighbour[x-1][y] == 0:
            #print "appending"
            neighbour[x][y] = 0
            neighbour[x-1][y] = 1
            neighbourhood.append(neighbour)
      
    if x is not nMax:
        #print "inside x not max"
        neighbour = deepcopy(solution)
        if neighbour[x+1][y] == 0:
           #print "appending"
            neighbour[x][y] = 0
            neighbour[x+1][y] = 1
            neighbourhood.append(neighbour)

    if y is not 0:
        #print "inside y not 0"
        neighbour = deepcopy(solution)
        if neighbour[x][y-1] == 0:
            #print "appending"
            neighbour[x][y] = 0
            neighbour[x][y-1] = 1
            neighbourhood.append(neighbour)

    if y is not nMax:
        #print "inside y not max"
        neighbour = deepcopy(solution)
        if neighbour[x][y+1] == 0:
            #print "appending"
            neighbour[x][y] = 0
            neighbour[x][y+1] = 1
            neighbourhood.append(neighbour)

    #print "Neighbourhood"
    #print neighbourhood
    return neighbourhood

def findBestSolution(solutions, k):
    maxScore = 0
    bestSolution = solutions[0]
    for solution in solutions:
        thisScore = getScore(solution, k)
        if thisScore > maxScore:
            maxScore = thisScore
            bestSolution = solution
    return bestSolution

def getNextSolution(P, PMax, T, k, n):
    #8. Let q = (F(Pmax)-F(P))/F(P)
    PMaxScore = getScore(PMax, k)
    PScore = getScore(P, k)
    q = (PMaxScore-PScore)/PScore

    #9. Let p = min [1, e^(-q/T) ]
    cooling = exp(-q/T)
    if cooling < 1:
        p = cooling
    else:
        p = 1

    #10. Generate x, a random real number in the closed range [0,1].
    x=random()

    #11. If x > p then P ? Pmax ;; ( Exploiting )
    if(x > p):
        nextSolution = PMax 

    #12. else P ? a random choice among the n neighbors. ;; (Exploring)
    else:
        nextSolution = n[int(random()*len(n))]

    return nextSolution

def printSolution(matrix):
    N = len(matrix)
    for row in range(N):
        line = ""
        for col in range(N):
            line += str(matrix[row][col]) + " "
        print line
    print " "

def printStats():
    print "stepCounter:"
    print stepCounter
    
def mostTroublingNode(matrix, n, k):
    mostTroubles = 0
    for rad in range(n):
        for col in range(n):
            if matrix[rad][col] == 1:
                troubles = 0
                eggs = 0
                for line in matrix:
                    eggs += line[col]
                if eggs > k:
                    troubles += 1
                if sum(matrix[rad]) > k:
                    troubles += 1
                if sum(getDiagIncrease(rad, col, matrix, n)) > k:
                    troubles += 1
                if sum(getDiagDecrease(rad, col, matrix, n)) > k:
                    troubles += 1
                
                if troubles > mostTroubles:
                    mostTroubles = troubles
                    troubledX = rad
                    troubledY = col
    return (troubledX,troubledY)

def randomXY(this, n):
    x=int(n*random())
    y=int(n*random())
    while(this[x][y] == 0):
        x = int(n*random())
        y = int(n*random())
    return (x,y)
    
########################### For testing #######################
def test():
    test1 = [1,0,1]
    test2 = [1,1,0]
    test3 = [0,1,1]
    test=[]
    test.append(test1)
    test.append(test2)
    test.append(test3)
    return test
################################################################


T_max = 100
T_step = 0.01
F_target = 100
stepCounter = 0
n = 5
k = 2

#1. Begin at a start point P (either user-selected or randomly-generated).
this = getStartSolution(n,k)
#this = test()                                                                     #####################Testing##############
#2. Set the temperature, T, to it's starting value: Tmax
T = T_max

#4. If F(P) = Ftarget then EXIT and return P as the solution; else continue.
while(getScore(this,k) < F_target) and (T > 0):

    (x,y) = randomXY(this, n)
    #(x,y) = mostTroublingNode(this, n, k)
    
    #print (x,y)
    #printSolution(this)
    #sleep(3)

    #5. Generate n neighbors of P in the search space: (P1, P2, ..., Pn).
    neighbours=getNeighbours(x,y,this)

    if(len(neighbours) != 0):
        #6. Evaluate each neighbor, yielding (F(P1), F(P2), ..., F(Pn)).
        #7. Let Pmax be the neighbor with the highest evaluation.
        PMax=findBestSolution(neighbours, k)

        #8-12
        this = getNextSolution(this, PMax, T, k, neighbours)

        #13. T = T - dT
        T=T-T_step

        # print solution
        #print "Candidate"
        #printSolution(this)
        #print getScore(this,k)
        stepCounter += 1


printStats()
printSolution(this)
print getScore(this,k)








