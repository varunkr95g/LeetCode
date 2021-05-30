class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub_arr=[]
        max_arr=[]
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                sub_arr.append(nums[i:j])
        
        
        for i in sub_arr:
            if(i==list(OrderedDict.fromkeys(i)) and i==sorted(i)):
                max_arr.append(sum(i))
        
        return max(max_arr)
