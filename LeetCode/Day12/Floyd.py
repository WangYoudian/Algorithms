V = 4
INF = 99999

def floydWarshall(graph): 
	dist = [[j for j in i] for i in graph] 
	for k in range(V): 
		# pick all vertices as source one by one 
		for i in range(V): 
			# Pick all vertices as destination for the 
			# above picked source 
			for j in range(V): 
				# If vertex k is on the shortest path from 
				# i to j, then update the value of dist[i][j] 
				dist[i][j] = min(dist[i][j] , 
								dist[i][k]+ dist[k][j]) 
	printSolution(dist) 

# A utility function to print the solution 
def printSolution(dist): 
	print("Following matrix shows the shortest distances between every pair of vertices") 
	for i in range(V): 
		for j in range(V): 
			if(dist[i][j] == INF): 
				# align right for string
				print("{:>7}\t".format("INF"), end='') 
			else: 
				# align right for number
				print("{:7d}\t".format(dist[i][j]), end='') 
			if j == V-1: 
				print("") 

# Driver program to test the above program 
graph = [[0,5,INF,10], 
			[INF,0,3,INF], 
			[INF, INF, 0, 1], 
			[INF, INF, INF, 0] 
		] 
floydWarshall(graph); 
