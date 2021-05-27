class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        sub_arr=[]
        listsen=sentence.split(" ")
        
        for i in range(len(listsen)):
            if (searchWord in listsen[i] and searchWord[0]==listsen[i][0]):
                sub_arr.append(i+1)
                break
        
        if(sub_arr):
            return sub_arr[0]
        else:
            return -1
