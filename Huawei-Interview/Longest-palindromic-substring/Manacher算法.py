# https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/

import time

class Solution:
	def longestPalindrome(self, s) -> str:
		size = len(s)
		if size < 2:
			return s

		# center为取的最右边回文串的中心得max_right更新时
		center = 0
		max_right = 0

		max_length = 1
		start = 1

		t = '#'
		# 遍历s 构造t
		for i in range(size):
			t += s[i]
			t += '#'

		t_len = 2 * size + 1

		p = [0] * t_len

		for i in range(t_len):
			if i < max_right:
				mirror = 2 * center - i
				p[i] = min(max_right - i, p[mirror])

			left = i - (1 + p[i])
			right = i + (1 + p[i])

			# 扩展
			while left >= 0 and right < t_len and t[left] == t[right]:
				p[i] += 1
				left -= 1
				right += 1

			if i + p[i] > max_right:
				# center为取的最右边回文串的中心得max_right更新时
				max_right = i + p[i]
				center = i

			if p[i] > max_length:
				max_length = p[i]
				start = (i - max_length) // 2

		return s[start: start + max_length]

if __name__ == '__main__':
	solution = Solution()
	t1 = time.process_time()
	# print(solution.longestPalindrome('aaaaaaaaa'))
	for i in range(10000):
		palidrome = solution.longestPalindrome('badbadababaddba')
		# print(palidrome)
	t2 = time.process_time()
	print('time costs:%.10f s' % (t2 - t1))

