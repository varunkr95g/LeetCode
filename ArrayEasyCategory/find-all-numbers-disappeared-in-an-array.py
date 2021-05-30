class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_2=list(set(nums))

        sub_arr=[]
            
        for i in range(1,len(nums)+1):
            if i not in nums_2:
                sub_arr.append(i)
            
        return sub_arr
