"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

https://leetcode.com/problems/longest-common-prefix/
"""

def longestCommonPrefix(self, strs):
	"""
	:type strs: List[str]
	:rtype: str
	"""
	if not strs:
		return ""
	shortest = min(strs,key=len)
	for i, ch in enumerate(shortest):
		for other in strs:
			if other[i] != ch:
				return shortest[:i]
	return shortest 