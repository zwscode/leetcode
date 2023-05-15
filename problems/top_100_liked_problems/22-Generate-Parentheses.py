"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

https://leetcode.com/problems/generate-parentheses/
"""

# backtrack
class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		res = []
		str = ""
		l, r = 0, 0
		self.backtrack(res, str, l, r, n)
		return res

	def backtrack(self, res, str, l, r, max):
		if (len(str) == max * 2):
			res.append(str)

		if l < max:
			self.backtrack(res, str+"(", l+1, r, max)
		if l > r:
			self.backtrack(res, str+")", l, r+1, max)

# dp
"""
Generate one pair: ()

Generate 0 pair inside, n - 1 afterward: () (...)...

Generate 1 pair inside, n - 2 afterward: (()) (...)...

...

Generate n - 1 pair inside, 0 afterward: ((...))

I bet you see the overlapping subproblems here. Here is the code:
(you could see in the code that x represents one j-pair solution 
and y represents one (i - j - 1) pair solution,
and we are taking into account all possible of combinations of them)
"""
class Solution2:
	def generateParenthesis(self, n: int) -> List[str]:
		dp = [[] for i in range(n + 1)]
		dp[0].append('')
		for i in range(n + 1):
			for j in range(i):
				dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
		return dp[n]