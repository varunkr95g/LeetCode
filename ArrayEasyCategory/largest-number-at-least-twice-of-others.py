class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num=max(nums)
        max_index=nums.index(max_num)
        sub_arr=[]
        # print (max_num)
        # print (max_index)
        
        for i in range(len(nums)):
            if((max_num!=nums[i]) and (max_num>=2*nums[i])):
                sub_arr.append(nums[i])
        
        print (sub_arr)
        
        if ((len(nums)-len(sub_arr))==1):
            return max_index
        else:
            return -1
        
