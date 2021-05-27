class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        string1=''.join(word1)
        string2=''.join(word2)
        
        # print (string1)
        # print (string2)
        
        if(string1==string2):
            return True
        else:
            return False
