# Given a string, what is the minimum number of adjacent swaps required to convert a string into a palindrome. If not possible, return -1.

# Example 1:

# Input: "mamad"
# Output: 3
# Example 2:

# Input: "asflkj"
# Output: -1
# Example 3:

# Input: "aabb"
# Output: 2
# Example 4:

# Input: "ntiin"
# Output: 1
# Explanation: swap 't' with 'i' => "nitin"

class Solution:
    def minSwap(self, S: str) -> int:
        s = list(S)
        # check if s can be panlindrom
        letter, odd = [0] * 26, 0
        for i in s: letter[ord(i) - ord('a')] += 1
        for l in letter:
            if l & 1 == 1: odd += 1
        if odd > 1: return -1
        i, j, res = 0, len(s) - 1, 0
        while i < j:
            if s[i] == s[j]:
                i, j = i + 1, j - 1
                continue
            t = j - 1
            # find same letter with s[i] from right to left
            while t > i and s[t] != s[i]: t -= 1
            # if t==i, means this is the only letter in the s, should be swap to the middle
            # otherwise should be swap to the position of j
            target = len(s) // 2 if t == i else j
            while t < target:
                # swap
                tmp = s[t]
                s[t] = s[t+1]
                s[t+1] = tmp
                res, t = res + 1, t + 1
        return res
