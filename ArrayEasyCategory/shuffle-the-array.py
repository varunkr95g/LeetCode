class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        x=[]
        y=[]
        z=[]
        
        
        for i in range(len(nums)/2):
            x.append(nums[i])
        
        # print (x)
        
        
        for i in range(len(nums)/2,len(nums)):
            y.append(nums[i])
        
        # print (y)
        
        for i in range(len(x)):
            z.append(x[i])
            z.append(y[i])
        
        return z
        
