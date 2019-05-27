N = 10
cnt = 0

def isSafe(board, row, col): 
	for i in range(col): 
		if board[row][i] == 1: 
			return False

	for i,j in zip(range(row,-1,-1), range(col,-1,-1)): 
		if board[i][j] == 1: 
			return False

	for i,j in zip(range(row,N,1), range(col,-1,-1)): 
		if board[i][j] == 1: 
			return False
	return True

def solveNQUtil(board, col): 
	global cnt
	if col >= N: 
		cnt += 1
		return True

	for i in range(N): 
		if isSafe(board, i, col): 
			board[i][col] = 1
			solveNQUtil(board, col+1)
			board[i][col] = 0

def solveNQ(): 
	board = [[0]*N for i in range(N)]
	solveNQUtil(board, 0)
	if not cnt: 
		print("Solution does not exist")
		return
	print(cnt)

# driver program to test above function 
solveNQ()
