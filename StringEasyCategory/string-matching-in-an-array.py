class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        sub_arr=[]

        for i in words:
        
            for j in words:
                
                if( j in i and j!=i):
                    
                    sub_arr.append(j)
        
        return list(set(sub_arr))
