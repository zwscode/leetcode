"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

"""
idea:
use dict to record every character's index,
use a variable `start` to mark the start of the substring's start
update `max_len` if the substring's length is greater than `max_len`
"""

class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		n = len(s)
		str2idx = {}
		start = 0
		max_len = 0
		i = 0
		while i < len(s):
			char = s[i]
			if char in str2idx and str2idx[char] >= start:
				start = str2idx[char] + 1
			else:
				max_len = max(max_len, i - start + 1)
			str2idx[char] = i
			i += 1
		return max_len