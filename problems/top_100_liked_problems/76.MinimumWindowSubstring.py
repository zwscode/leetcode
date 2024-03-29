# https://leetcode.com/problems/minimum-window-substring/description/
# hard

"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
"""

class Solution(object):
	def minWindow(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: str
		"""
		from collections import Counter
		need = Counter(t)
		window = Counter()
		left = right = 0
		valid_len = 0
		start = 0
		res_len = len(s) + 1
		while right < len(s):
			# step1: expand the window to get a valid window
			c = s[right]
			right += 1
			if c in need:
				window[c] += 1
				if window[c] == need[c]:
					valid_len += 1
			# step2: shrink the valid window to get the minimum valid window
			while valid_len == len(need):
				if right - left < res_len:
					start = left
					res_len = right - left
				c = s[left]
				left += 1
				if c in need:
					if window[c] == need[c]:
						valid_len -= 1
					window[c] -= 1
		# res_len < initial value means we have found a valid window
		if res_len <= len(s):
			return s[start:start+res_len]
		else:
			return ""
