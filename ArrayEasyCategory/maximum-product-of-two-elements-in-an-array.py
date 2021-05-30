class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr=[]
        prod=0
        
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i!=j):
                    arr.append((nums[i]-1)*(nums[j]-1))
        
        # print (arr)
        
        prod=max(arr)
        return prod
