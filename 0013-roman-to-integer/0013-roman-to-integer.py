class Solution:
    def romanToInt(self, s: str) -> int:
        keys = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        ans = 0
        

        for i in range(len(s)):
            if i < len(s)-1 and keys[s[i]] < keys[s[i+1]]:
                ans -= keys[s[i]]
            else:
                ans += keys[s[i]]
        return ans