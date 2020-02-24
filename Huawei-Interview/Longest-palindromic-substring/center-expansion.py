"""
事实上，只需使用恒定的空间，我们就可以在 O(n^2)O的时间内解决这个问题。

我们观察到回文中心的两侧互为镜像。因此，回文可以从它的中心展开，并且只有 2n - 1 个这样的中心。

你可能会问，为什么会是 2n - 12n−1 个，而不是 nn 个中心？
原因在于所含字母数为偶数的回文的中心可以处于两字母之间
（例如 \textrm{“abba”}“abba” 的中心在两个 \textrm{‘b’}‘b’ 之间）。

作者：LeetCode
链接：https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

class Solution:
	def longestPalindrome(self, s: str):
		if s is None or len(s) < 1:
			return ""
		start = end = 0
		for i in range(len(s)):
			len1 = self.expandAroundCenter(s, i, i)
			len2 = self.expandAroundCenter(s, i, i+1)
			length = max(len1, len2)
			if length > end - start:
				start = i - (length -1) // 2
				end = i + length // 2
				# print(start, end)
		return s[start: end+1]

	def expandAroundCenter(self, s, left, right):
		while left >= 0 and right < len(s) and s[left] == s[right]:
			left -= 1
			right += 1

		return right - left - 1

if __name__ == '__main__':
	solution = Solution()
	print(solution.longestPalindrome("babad"))
