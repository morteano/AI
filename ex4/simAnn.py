



#1. Begin at a start point P (either user-selected or randomly-generated).
this = getStartSolution()

#2. Set the temperature, T, to it’s starting value: Tmax
Temp = T_max

#4. If F(P) ≥ Ftarget then EXIT and return P as the solution; else continue.
while(getScore(this) < F_target):

	#5. Generate n neighbors of P in the search space: (P1, P2, ..., Pn).
	n=getNeighbours(this)

	#6. Evaluate each neighbor, yielding (F(P1), F(P2), ..., F(Pn)).
	ns=getScores(n)

	#7. Let Pmax be the neighbor with the highest evaluation.
	pMax=getMaxScore(ns)

	#8. Let q = F (Pmax)−F (P )F (P )
	q=getQ(pMax,this)

	#9. Let p = min [1, e−qT ]
	candidateScore=getp(q, Temp)

	#10. Generate x, a random real number in the closed range [0,1].
	x=rand()

	#11. If x > p then P ← Pmax ;; ( Exploiting )
	if(x > candidateScore):
		this = pMax 

	#12. else P ← a random choice among the n neighbors. ;; (Exploring)
	else:
		this = n[rand()*len(n)]
	#13. T ← T − dT
	Temp=Temp-TempStep
# print solution
printSolution()
printStats()

def getNeighbours(this):
	#Find the part with the most issues

	#Create the neighbours
	return createNeighbours(This, troubledStep)

def printSolution(matrix):
	line = ""
	for row in range(1:M):
		for col in range(1:N):
			line += str(matrix[row][col])
		print line







