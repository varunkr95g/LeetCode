class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length=len(A)

        dictionary={}
        
        for i in A:
            if (i in dictionary):
                dictionary[i]+=1
            else:
                dictionary[i]=1
        
        # print (dictionary)
        
        for i,j in dictionary.items():
            if(j==length/2):
                return i
                break
