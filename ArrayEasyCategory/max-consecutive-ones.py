class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count1_arr=[]
        count1=0
        
        for i in nums:
            if(i==1):
                count1+=1
            if(i==0):
                count1_arr.append(count1)
                count1=0

        count1_arr.append(count1)
        
        return max(count1_arr)
