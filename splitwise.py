#Set the number of people involved
N = 4


def minCalculate(net_spend):

#Calculating the max credit and max debit index.
	maxC = net_spend.index(max(net_spend))
	maxD = net_spend.index(min(net_spend))
    
#If both, max credit and max debit, amount to zero, this implies that all debts have been settled.
	if (net_spend[maxC] == 0 and net_spend[maxD] == 0):
		return 0

#Calculating the minimum of max credit and max debit
	min1 = -net_spend[maxD] if -net_spend[maxD] < net_spend[maxC] else net_spend[maxC]
#Settling the debt between Max creditor and max debitor (min of either is transferred to the other person)
	net_spend[maxC] -=min1
	net_spend[maxD] += min1
#Printing the above transaction.
	print("Person " , maxD , " will pay $" , min1
		, " to " , "Person " , maxC)
#Recursively call after removing the person whose debt has been settled
	minCalculate(net_spend)

def amountCalculate(graph):

	net_spend = [0 for i in range(N)]
#Traversing through the graph and calculating the net amount for each person and storing it in an array.
	for i in range(N):
		for j in range(N):
			net_spend[i] += (graph[j][i] - graph[i][j])

	minCalculate(net_spend)
	
#Input is taken in the form of a 2-D array. The amount owed by the ith person is written on the corresponding column.
graph = [ [0, 1000, 500,0],
		[0, 0, 1500, 500],
		[0, 0, 0, 500],
        [2000, 0, 0, 0]]

amountCalculate(graph)

