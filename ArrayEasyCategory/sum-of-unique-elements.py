class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictionary={}
        sum=0
        
        for i in nums:
            if(i in dictionary):
                dictionary[i]+=1
            else:
                dictionary[i]=1
        
        for key,value in dictionary.items():
            if(value==1):
                sum+=key
        
        return sum
