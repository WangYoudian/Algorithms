# 拼写检查
# 语音识别
# DNA分析
# 剽窃检测

def levenshtein(str1, str2):
	m, n = len(str1), len(str2)
	dp = [[0]*(n+1) for i in range(m+1)]
	for i in range(1, m+1):
		dp[i][0] = dp[i-1][0] + 1
	for j in range(1, n+1):
		dp[0][j] = dp[0][j-1] + 1

	for i in range(1, m+1):
		for j in range(1, n+1):
			if str1[i-1] == str2[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
	# for d in dp:
	# 	print(d)
	return dp[-1][-1]

if __name__ == '__main__':
	str1 = 'ATCG'
	str2 = 'TCA'
	dist = levenshtein(str1, str2)
	print(dist)