class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        product=1
        if(0 in nums):
            product=0
            return 0
        else:
            for i in nums:
                product*=i
            if(product>0):
                return 1
            else:
                return -1
