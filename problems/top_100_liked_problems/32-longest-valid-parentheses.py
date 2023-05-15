# https://leetcode.com/problems/longest-valid-parentheses/
#Given a string containing just the characters '(' and ')', 
# return the length of the longest valid (well-formed) parentheses 

# Example 1:

# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:

# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:

# Input: s = ""
# Output: 0
 

# Constraints:

# 0 <= s.length <= 3 * 104
# s[i] is '(', or ')'.


class Solution:
	def longestValidParentheses(self, s: str) -> int:
		stack = [-1]
		ans = 0
		for i in range(len(s)):
			if s[i] == '(':
				stack.append(i)
			else:
				stack.pop()
				if (not stack):
					stack.append(i)
				else:
					ans = max(ans, i - stack[-1])

		return ans

	def longestValidParentheses2(self, s):
		stack, res, s = [0], 0, ')'+s
		for i in range(1, len(s)):
			if s[i] == ')' and s[stack[-1]] == '(':
				stack.pop()
				res = max(res, i - stack[-1])
			else:
				stack.append(i)
		return res
	
