class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        
        """
        sub_arr=[0]*len(nums)

        sub_arr[::2]=[x for x in nums if x%2==0]
        sub_arr[1::2]=[x for x in nums if x%2!=0]

        return sub_arr
