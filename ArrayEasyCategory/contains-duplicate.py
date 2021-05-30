class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dictionary={}
        count=0
        
        for i in nums:
            if(i in dictionary):
                dictionary[i]+=1
            else:
                dictionary[i]=1
        
        for i in dictionary.values():
            if(i!=1):
                count=1
                break
        
        if(count):
            return True
        else:
            return False
