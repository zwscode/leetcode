
"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""


"""
summary:
dfs
backtracking
permutations
"""

class Solution:
    def letterCombinations_dfs(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        res=[]
        if len(digits) ==0:
            return res
            
        self.dfs(digits, 0, dic, '', res)
        return res
    
    def dfs(self, nums, index, dic, path, res):
        if index >=len(nums):
            res.append(path)
            return
        string1 =dic[nums[index]]
        for i in string1:
            self.dfs(nums, index+1, dic, path + i, res)


    

from collections import deque
from typing import List

def letterCombinations_Queue(digits: str) -> List[str]:
    ans = deque()
    if not digits:
        return list(ans)
    mapping = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    ans.append("")
    while len(ans[0]) != len(digits):
        remove = ans.popleft()
        phone_keys = mapping[int(digits[len(remove)])]
        for c in phone_keys:
            ans.append(remove + c)
    return list(ans)
