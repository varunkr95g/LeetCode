class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        digits=[]
        dictionary={}
        
        for i in range(lowLimit,highLimit+1):
            total = 0
            for j in str(i):
                total+=int(j)
        
            # digits.append(total)
            if(total in dictionary):
                dictionary[total]+=1
            else:
                dictionary[total]=1
        
        
        
        
        # for i in digits:
        #     if( i in dictionary):
        #         dictionary[i]+=1
        #     else:
        #         dictionary[i]=1
        
        return max(dictionary.values())
