def isValidSodoku(board):
	for i in range(9):
		rows = set()
		colomns = set()
		cube = set()		
		for j in range(9):
			if board[i][j]!='.' and board[i][j] in rows:
				return False
			if board[j][i]!='.' and board[j][i] in colomns:
				return False
			rows.add(board[i][j])
			colomns.add(board[j][i])
			rowIndex = 3*(i//3)
			colomnIndex = 3*(i%3)
			if (board[rowIndex+j//3][colomnIndex+j//3]!='.') and board[rowIndex+j//3][colomnIndex+j//3] in cube:
				return False

	return True
