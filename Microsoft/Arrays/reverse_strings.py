"""

Given an input string, reverse the string word by word
"""

class Solution(object):
    def reverseWords(self,s):
        reversedlist = s.split()
        reversedlist = reversedlist[::-1]
        string = ""
        for word in reversedlist:
            string += word
            string += ""
        return string.strip()

