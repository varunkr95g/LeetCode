class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count=0
        check=high-low+1

        if(check%2==0):
            count+=check//2
        else:
            if(low%2!=0 and high%2!=0):
                count=check//2 + 1
            elif(low%2==0 and high%2==0):
                count = check // 2
        
        
        return count
