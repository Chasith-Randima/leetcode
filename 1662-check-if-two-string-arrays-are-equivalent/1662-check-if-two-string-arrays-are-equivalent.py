class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        tempWord1 = ""
        tempWord2 = ""

        for word in word1:
            tempWord1 += word
        
        for word in word2:
            tempWord2 += word

        if tempWord1 == tempWord2:
            return True
        else:
            return False

