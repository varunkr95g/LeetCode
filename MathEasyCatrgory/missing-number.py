class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        arr_2=[]
        length=len(nums)
        # print (length)
        sub_arr=[]
        
        nums.append(0)
        for i in range(length+1):
            arr_2.append(i)
        
        # print (arr_2)
        
        for i  in range(len(nums)):
            if(nums[i]!=arr_2[i]):
                sub_arr.append(arr_2[i])
        
        return min(sub_arr)
