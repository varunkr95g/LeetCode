class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length=0

        for i in range(len(nums)):
            if(nums[i]==val):
                nums[i]=-1
        
        nums.sort(reverse=True)
        
        for i in nums:
            if(i!=-1):
                length+=1
        
        return length
