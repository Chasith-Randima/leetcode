class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        newString = ""
        newDict = {}

        for num in range(len(indices)):
            newDict[indices[num]] = s[num]

        for index in range(len(indices)):
            newString += newDict[index]

        return newString