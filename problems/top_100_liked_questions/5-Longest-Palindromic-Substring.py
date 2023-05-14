"""
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""



# straight forward approach 1: from two sides
# time complexity is O(n^3)

def isPalindrome(s, l, r):
	while l < r:
		if s[l] != s[r]:
			return False
		l += 1
		r -= 1
	return True

def longestPalindrome(self, s: str) -> str:
	for i in xrange(len(s)):
		for j in xrange(i, len(s)):
			if (j - i + 1 > len(best)) and isPalindrome(s, i, j):
				best = s[i:j+1]
	return best


# optimized: check from center
# https://leetcode.com/problems/longest-palindromic-substring/solutions/2954/python-easy-to-understand-solution-with-comments-from-middle-to-two-ends/
# time complexity is O(n^2)

# expand from center
def longestPalindrome(self, s: str) -> str:
	res = ""
	for i in xrange(len(s)):
		# odd case, like "aba"
		tmp = self.helper(s, i, i)
		if len(tmp) > len(res):
			res = tmp
		# even case, like "abba"
		tmp = self.helper(s, i, i+1)
		if len(tmp) > len(res):
			res = tmp
	return res
 
# get the longest palindrome, l, r are the middle indexes   
# from inner to outer
def helper(self, s, l, r):
	while l >= 0 and r < len(s) and s[l] == s[r]:
		l -= 1; r += 1
	return s[l+1:r]


# dp approach
class Solution:
	def longestPalindrome(self, s: str) -> str:
		n = len(s)
		# initialize a 2D array to store the results of subproblems
		dp = [[False] * n for _ in range(n)]
		res = ""

		# iterate over the 2D array diagonally, starting from top right corner
		for k in range(n):
			i = 0
			j = k
			while j < n:
				# if the substring is a palindrome
				if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
					dp[i][j] = True
					# update the result if the current substring is longer than the previous result
					if j - i + 1 > len(res):
						res = s[i:j+1]
				i += 1
				j += 1
		return res




"""
Manacher's algorithm

In this implementation, we first modify the input string s by inserting # characters between each character. 
This allows us to handle both even-length and odd-length palindromes more easily.

We then iterate over the indices of the modified string t, and for each index i, 
we first check if i is within the right boundary of the current palindrome. 
If it is, we use the symmetry of palindromes to update the length of the palindrome at index i. 

We then try to expand the palindrome centered at index i by checking if the characters to the left and right of i match. 
If they do, we increment the length of the palindrome at index i. 

We then update the center and right boundary of the current palindrome if necessary, 
and update the center and length of the longest palindrome found so far,
if the palindrome at index i is longer than the previous longest palindrome.

Finally, we extract the longest palindrome substring from the modified input string t 
by finding the center and length of the longest palindrome, and then mapping those indices back to the original input string s. 
This algorithm has a time complexity of O(n), where n is the length of the input string s.
"""

#  Manacher's algorithm, time complexity O(n)
class Solution:
	def longestPalindrome(self, s: str) -> str:
		# modify the input string to insert '#' characters between each character
		t = '#' + '#'.join(s) + '#'
		n = len(t)
		# initialize an array to store the lengths of palindromes
		p = [0] * n
		# initialize variables to track the center and right boundary of the current palindrome
		center = right = 0
		# initialize variables to track the center and length of the longest palindrome found so far
		max_center, max_len = 0, 0

		for i in range(n):
			# check if the current index is within the right boundary of the current palindrome
			if i < right:
				# use the symmetry of palindromes to update the length of the palindrome at index i
				p[i] = min(right - i, p[2*center - i])

			# try to expand the palindrome centered at index i
			while i - p[i] - 1 >= 0 and i + p[i] + 1 < n and t[i - p[i] - 1] == t[i + p[i] + 1]:
				p[i] += 1

			# update the center and right boundary of the current palindrome if necessary
			if i + p[i] > right:
				center, right = i, i + p[i]

			# update the center and length of the longest palindrome found so far
			if p[i] > max_len:
				max_center, max_len = i, p[i]

		# extract the longest palindrome substring from the modified input string
		start = (max_center - max_len) // 2
		end = start + max_len
		return s[start:end]
	

"""
similar problem: LeetCode 516. Longest Palindromic Subsequence
"""