class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.split(" ")
        newS = []

        for word in reversed(s):
            if len(word) > 0:
                newS.append(word)

        return " ".join(newS)
