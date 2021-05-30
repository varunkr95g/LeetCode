class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)<3):
            return max(nums)

        else:
            nums_2=list(set(nums))
            nums_2.sort(reverse=True)
            if(len(nums_2)>=3):
                return nums_2[2]
            else:
                return max(nums_2)
