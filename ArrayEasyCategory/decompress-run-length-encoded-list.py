class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k=[]

        for i in range(0,len(nums),2):
            for j in range(0,nums[i]):
                k.append(nums[i+1])
        
        return (k)
        
