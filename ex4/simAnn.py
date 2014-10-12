from random import randrange
from copy import deepcopy

def getStartSolution(n,k):
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

def getDiagDecrease(row, col, matrix, n):
	list = []
	while row < n and col < n:
		list.append(matrix[row][col])
		row+=1
		col+=1
	return list

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
		    
    for scorePartial in scoresPartial:
                if (sum(scorePartial) <= k) and (len(scorePartial) > 0):
                    score += 1
    # Print score in percent of maximum score
    return (score/(4+(n-1)*6)*100)

def getNeighbours(x,y,solution):
	#Create the neighbours
    
    # Define boundries
    nMax = len(solution)-1
    
    #  Create neighbourhood for this solution    
    neighbourhood = []
    
    # Only add existing neighbours to the neigbourhood
    if x is not 0:
        neighbour = deepcopy(solution)
        if neighbour[x-1][y] == 0:
            neighbour[x][y] = 0
            neighbour[x-1][y] = 1
            neighbourhood.append(neighbour)
              
    if x is not nMax:
       neighbour = deepcopy(solution)
       if neighbour[x+1][y] == 0:
            neighbour[x][y] = 0
            neighbour[x+1][y] = 1
            neighbourhood.append(neighbour)
          
    if y is not 0:
        neighbour = deepcopy(solution)
        if neighbour[x][y-1] == 0:
            neighbour[x][y] = 0
            neighbour[x][y-1] = 1
            neighbourhood.append(neighbour)
          
    if y is not nMax:
        neighbour = deepcopy(solution)
        if neighbour[x][y+1] == 0:
            neighbour[x][y] = 0
            neighbour[x][y+1] = 1
            neighbourhood.append(neighbour)
        
	return neighbourhood

def getScores(list):
	scores = []
	for solution in list:
		scores.append(getScore(solution,k))
	return scores

def findBestSolution(solutions):
	maxScore = 0
	bestSolution = solution[0]
	for solution in solutions:
		thisScore = getScore(solution, k)
		if thisScore > maxScore:
			maxScore = thisScore
			bestSolution = solution
	return solution

def getNextSolution(P, PMax, T):
	#8. Let q = (F(Pmax)-F(P))/F(P)
	PMaxScore = getScore(PMax)
	PScore = getScore(P)
	q = (PMaxScore-PScore)/PScore

	#9. Let p = min [1, e^(-q/T) ]
	cooling = exp(-q/T)
	if cooling < 1:
		p = cooling
	else:
		p = 1

	#10. Generate x, a random real number in the closed range [0,1].
	x=rand()

	#11. If x > p then P ? Pmax ;; ( Exploiting )
	if(x > p):
		nextSolution = PMax 

	#12. else P ? a random choice among the n neighbors. ;; (Exploring)
	else:
		nextSolution = n[rand()*len(n)]

	return nextSolution

def printSolution(matrix):
    N = len(matrix)
    for row in range(N):
        line = ""
        for col in range(N):
            line += str(matrix[row][col]) + " "
        print line

T_max = 100
T_step = 1
F_target = 0
n = 3
k = 2
#1. Begin at a start point P (either user-selected or randomly-generated).
this = getStartSolution(n,k)

#2. Set the temperature, T, to it's starting value: Tmax
T = T_max

#4. If F(P) = Ftarget then EXIT and return P as the solution; else continue.
while(getScore(this,k) < F_target):

	#5. Generate n neighbors of P in the search space: (P1, P2, ..., Pn).
	neighbours=getNeighbours(this)

	#6. Evaluate each neighbor, yielding (F(P1), F(P2), ..., F(Pn)).
	#7. Let Pmax be the neighbor with the highest evaluation.
	PMax=findBestSolution(neighbours)

	#8-12
	this = getNextSolution(this, PMax, T)

	#13. T = T - dT
	T=T-T_Step
	# print solution
	printSolution(this)
	
#printStats()

#test1 = [1,0,1]
#test2 = [1,1,0]
#test3 = [0,1,1]
#test=[]
#test.append(test1)
#test.append(test2)
#test.append(test3)
#this = test


printSolution(this)
print getScore(this,k)








