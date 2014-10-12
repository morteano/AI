from random import randrange

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
    
def getScore(solution,k):
    n = len(solution)
    score = 0.0
    for col in range(n):
        eggs = 0
        for row in range(n):
            eggs += solution[row][col]
        if eggs <= k:
            score += 1
    
    # Check diagonal for lower triangular matrix    
    for row in range(n):
        eggs = 0
        rowTemp = row
        colTemp = 0
        while rowTemp < n and colTemp < n:
            eggs += solution[rowTemp][colTemp]
            rowTemp += 1
            colTemp += 1
        if eggs <= k:
            score += 1
            
    # Check diagonal for upper triangular matrix            
    for col in range(1,n):
        eggs = 0
        rowTemp = 0
        colTemp = col
        while rowTemp < n and colTemp < n:
            eggs += solution[rowTemp][colTemp]
            rowTemp += 1
            colTemp += 1
        if eggs <= k:
            score += 1

    # Check diagonal for lower triangular matrix    
    for row in range(n):
        eggs = 0
        rowTemp = row
        colTemp = n-1
        while rowTemp >= 0 and colTemp >= 0:
            eggs += solution[rowTemp][colTemp]
            rowTemp -= 1
            colTemp -= 1
        if eggs <= k:
            score += 1
            
    # Check diagonal for upper triangular matrix            
    for col in range(1,n):
        eggs = 0
        rowTemp = n-1
        colTemp = col
        while rowTemp >= 0 and colTemp >= 0:
            eggs += solution[rowTemp][colTemp]
            rowTemp -= 1
            colTemp -= 1
        if eggs <= k:
            score += 1
    return score*100/(3+(n-1)*5) 

def getNeighbours(this):
	#Find the part with the most issues

	#Create the neighbours
	return []

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
	#8. Let q = F (Pmax)-F (P )F (P )
	PMaxScore = getScore(PMax)
	PScore = getScore(P)
	q = (PMaxScore-PScore)/PScore

	#9. Let p = min [1, e-qT ]
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
n = 4
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

printSolution(this)
print getScore(this,k)









