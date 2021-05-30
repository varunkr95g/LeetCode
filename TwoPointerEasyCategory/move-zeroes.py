class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(0,len(nums)-1):
                if(nums[j]==0):
                    nums[j+1],nums[j]=nums[j],nums[j+1]
                    
#         sub_arr=[]

#         for i in nums:
#             if(i!=0):
#                 sub_arr.append(i)
#         for i in nums:
#             if(i==0):
#                 sub_arr.append(i)
        
#         for i in range(len(sub_arr)):
#             nums[i]=sub_arr[i]

#         # return nums
