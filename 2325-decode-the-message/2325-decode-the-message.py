class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        # mapping = {' ': ' '}
        # i = 0
        # res = ''
        # letters = 'abcdefghijklmnopqrstuvwxyz'
        
        # for char in key:
        #     if char not in mapping:
        #         print(len(letters),i)
        #         mapping[char] = letters[i]
        #         i += 1
        
        # for char in message:
        #     res += mapping[char]
                
        # return res
        keyTable = {" ":" "}
        index = 0
        letters = "abcdefghijklmnopqrstuvwxyz"
        outString = ""

        for letter in key:
            if letter not in keyTable:
                keyTable[letter] = letters[index]
                index += 1

        for letter in message:
            if letter == " ":
                outString += " "
            else:
                outString += keyTable[letter]
        return outString
