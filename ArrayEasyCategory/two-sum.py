class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sub_arr=[]

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if ((nums[i]+nums[j])==target):
                    sub_arr.append(i)
                    sub_arr.append(j)
                    break
        
        return sub_arr
