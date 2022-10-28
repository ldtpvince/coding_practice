# Question: https://leetcode.com/problems/longest-common-subsequence/
# Solution:

#     a | b | c | e
# a   1   1   1   1
# c   1   1   2   2
# e   1   1   2   3

# Let's think this problem with a simple case:
#     - In order to do this we have to traverse both string each character a time
#     - Say we are consider the sequence ("abce", "ace")
#     - If we are consider two substring at their ends lcs("abc", "ac"), they have the same characters so 
#     our suspicion is that the longest common substring is lcs("ab", "a") + 1
#     - To check that there aren't any previous c in two substring that may also correspond to the current c
#     we check max(lcs("ab", "ac"), lcs("abc", "a"))
#     => lcs("abc", "ac") = max(lcs("ab", "a") + 1, lcs("ab", "ac"), lcs("abc", "a"))

def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    l1 = len(text1)
    l2 = len(text2)
    temp = [[0] * l1 for _ in range(l2)]
    
    for i in range(l1):
        if text2[0] == text1[i]:
            temp[0][i] = 1
        else:
            if i != 0:
                temp[0][i] = temp[0][i-1]
            
    for i in range(l2):
        if text1[0] == text2[i]:
            if i != 0:
                temp[i][0] = 1
        else:
            if i != 0:
                temp[i][0] = temp[i-1][0]
            
    for i in range(1, l2):
        for j in range(1, l1):
            if text2[i] == text1[j]:
                temp[i][j] += max([temp[i-1][j-1] + 1, temp[i-1][j], temp[i][j-1]])
            else:
                temp[i][j] = max(temp[i-1][j], temp[i][j-1])

    return temp[l2-1][l1-1]