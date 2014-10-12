



#1. Begin at a start point P (either user-selected or randomly-generated).
#this = getStartSolution()

#2. Set the temperature, T, to it's starting value: Tmax
#Temp = T_max

#4. If F(P) = Ftarget then EXIT and return P as the solution; else continue.
#while(getScore(this) < F_target):

	#5. Generate n neighbors of P in the search space: (P1, P2, ..., Pn).
#	n=getNeighbours(this)

	#6. Evaluate each neighbor, yielding (F(P1), F(P2), ..., F(Pn)).
#	ns=getScores(n)

	#7. Let Pmax be the neighbor with the highest evaluation.
#	pMax=getMaxScore(ns)

	#8. Let q = F (Pmax)-F (P )F (P )
#	q=getQ(pMax,this)

	#9. Let p = min [1, e-qT ]
#	candidateScore=getp(q, Temp)

	#10. Generate x, a random real number in the closed range [0,1].
#	x=rand()

	#11. If x > p then P ? Pmax ;; ( Exploiting )
#	if(x > candidateScore):
#		this = pMax 

	#12. else P ? a random choice among the n neighbors. ;; (Exploring)
#	else:
#		this = n[rand()*len(n)]
	#13. T ? T - dT
#	Temp=Temp-TempStep
# print solution
#printSolution()
#printStats()

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
    score = 0
    for col in range(n):
        eggs = 0
        for row in range(n):
            eggs += solution[row][col]
        if eggs <= k:
            score += 1
    print "Score after row:"
    print score
    
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
    print "Score after diag1:"
    print score
            
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
    print "Score after diag2:"
    print score
    return score  

def getNeighbours(this):
	#Find the part with the most issues

	#Create the neighbours
	return createNeighbours(This, troubledStep)

def printSolution(matrix):
    N = len(matrix)
    for row in range(N):
        line = ""
        for col in range(N):
            line += str(matrix[row][col]) + " "
        print line

n = 4
k = 2
solution = getStartSolution(n,k)
printSolution(solution)
print getScore(solution,k)









