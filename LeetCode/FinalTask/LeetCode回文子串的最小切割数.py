import sys
class Solution:
	def minCut(self, s):
		if len(s) == 0:
			return 0
		chars = list(s)
		length = len(chars)
		dp = [0]*(length+1)
		dp[length] = -1
		p = [[0]*length for i in range(length)]

		for i in range(length-1, -1, -1):
			dp[i] = sys.maxsize
			for j in range(i, length):
				if chars[i] == chars[j] and (j-i<2 or p[i+1][j-1]):
					p[i][j] = True
					dp[i] = min(dp[i], dp[j+1]+1)

		return dp[0]

if __name__ == '__main__':
	solution = Solution()
	# data
	s = "abcbaac"
	cut = solution.minCut(s)
	print(cut)
