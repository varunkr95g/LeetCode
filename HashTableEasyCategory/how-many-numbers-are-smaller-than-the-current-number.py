class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr=[]


        for i in range(len(nums)):
            k = 0;
            for j in range(len(nums)):
        
                if((nums[i]>nums[j]) and i!=j):
                    k=k+1
            arr.append(k)
        
        
        return arr
