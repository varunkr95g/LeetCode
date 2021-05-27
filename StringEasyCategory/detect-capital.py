class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        wordupper=word.upper()
        wordlower=word.lower()
        charupper=word[0].upper()
        strlower=word[1:].lower()
        
        
        
        if(word==wordupper or word==wordlower):
            return True
        elif(word[0]==charupper and word[1:]==strlower):
            return True
        else:
            return False
