class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        total=0
        
        for i in range(1,len(nums),2):
            total+=min(nums[i],nums[i-1])
        
        return total
