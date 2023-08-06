class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows < 2:
            return s

        i = 0

        res = [""]*numRows

        for ch in s:
            if i == numRows-1:
                grow = False
            elif i == 0:
                grow = True
            res[i] += ch
            i = (i+1) if grow else i-1
        
        return "".join(res)