"""
Hard!

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.

https://leetcode.com/problems/edit-distance/
"""


"""
https://leetcode.com/problems/edit-distance/solutions/25846/c-o-n-space-dp/

1. Definition of dp[i][j]
To apply DP, we define the state dp[i][j] to be the minimum number of operations 
to convert word1[0..i) to word2[0..j).

2. Base case
For the base case, that is, to convert a string to an empty string, 
the mininum number of operations (deletions) is just the length of the string. 
So we have dp[i][0] = i and dp[0][j] = j.

3. General case
For the general case to convert word1[0..i) to word2[0..j), we break this problem down into sub-problems. Suppose we have already known how to convert word1[0..i - 1) to word2[0..j - 1) (dp[i - 1][j - 1]), if word1[i - 1] == word2[j - 1], then no more operation is needed and dp[i][j] = dp[i - 1][j - 1].

If word1[i - 1] != word2[j - 1], we need to consider three cases.

1) Replace word1[i - 1] by word2[j - 1] (dp[i][j] = dp[i - 1][j - 1] + 1);
2) If word1[0..i - 1) = word2[0..j) then delete word1[i - 1] (dp[i][j] = dp[i - 1][j] + 1);
3) If word1[0..i) + word2[j - 1] = word2[0..j) then insert word2[j - 1] to word1[0..i) (dp[i][j] = dp[i][j - 1] + 1).

So when word1[i - 1] != word2[j - 1], dp[i][j] will just be the minimum of the above three cases.
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # if word2 is empty, edit distance is i
        for i in range(1, m + 1):
            dp[i][0] = i
        # if word1 is empty, edit distance is j
        for j in range(1, n + 1):
            dp[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # if last character is the same
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # if last character is different: 3 cases, replace, delete, insert
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
        return dp[m][n]
