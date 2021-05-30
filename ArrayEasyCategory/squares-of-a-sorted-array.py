class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sub_arr=[]

        for i in nums:
            sub_arr.append(i*i)
        
        return sorted(sub_arr)
