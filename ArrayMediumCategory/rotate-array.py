class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums_rotate=[]

        for i in range(len(nums)):
            nums_rotate.append(nums[(i+len(nums)-k)%len(nums)])
        
        for i in range(len(nums)):
            nums[i]=nums_rotate[i]

        return nums
