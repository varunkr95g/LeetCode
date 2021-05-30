class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=[]
        count=0
        
        for i in range(len(nums)):
            k.append(len(str(nums[i])))
        
        # print (k)
        
        for i in range(len(k)):
            if(k[i]%2==0):
                count+=1
        
        return count
