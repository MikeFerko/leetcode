#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
'''
time complexity: T = T(n) = O(n*m) 
space complexity: S = S(n,m) = O(n*m)

DP Solution using a table.

n = len(X), m = len(Y)
if the last character matches i.e. X[n-1] == Y[m-1]:
L(X[0…n-1],Y[0…m-1]) = 1+L(X[0…n-2],Y[0…m-2])
elif X[n-1] != Y[m-1]:
	L(X[0…n-1],Y[0…m-1]) = max(L(X[0…n-2],Y[0…m-1]), L(X[0…n-1],Y[0…m-2])) 

X = "abcde"
Y = "ace"

'''

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # find the length of each string
        n = len(text1)
        m = len(text2)

        L = [[None]*(m+1) for _ in range(0, n+1)]
        for i in range(0, n+1):
            for j in range(0, m+1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    L[i][j] = 1 + L[i-1][j-1]
                else:
                    L[i][j] = max(L[i-1][j], L[i][j-1])
        return L[n][m]

# @lc code=end

