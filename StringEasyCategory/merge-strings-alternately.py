class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        sub_arr=[]

        if(len(word1)==len(word2)):
            for i in range((len(word1)+len(word2))/2):
                sub_arr.append(word1[i])
                sub_arr.append(word2[i])
        
        elif(len(word2)>len(word1)):
            for i in range(len(word1)):
                sub_arr.append(word1[i])
                sub_arr.append(word2[i])
        
            sub_arr.append(word2[i + 1:len(word2)])
        
        else:
            for i in range(len(word2)):
                sub_arr.append(word1[i])
                sub_arr.append(word2[i])
        
            sub_arr.append(word1[i + 1:len(word1)])
        
        
        
        
        
        
        
        return ''.join(sub_arr)
