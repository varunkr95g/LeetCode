class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictionary={}

        for i in nums:
            if(i in dictionary):
                dictionary[i]+=1
            else:
                dictionary[i]=1
        
        for i in dictionary.keys():
            if(dictionary[i]==1):
                return i
                break
