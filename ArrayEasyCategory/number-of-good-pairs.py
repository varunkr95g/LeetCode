class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        k=[];

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if((nums[i]==nums[j])):
                    k.append(1)
        
        return(len(k))
