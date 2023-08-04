class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        s = s.split(" ")
        slen = 0

        for i in s:
            if len(i) != 0:
                slen = len(i)
        
        return slen