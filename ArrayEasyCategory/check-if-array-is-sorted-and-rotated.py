class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_sort=sorted(nums)
        # x=0
        count=0
        
        
        for i in range(len(nums)):
            sub_arr = []
            for x in range(len(nums)):
        
        
        
                sub_arr.append(nums[(i+x)%len(nums)])
        
            if(sub_arr==nums_sort):
                count+=1
                break
        
            else:
                count=0
        
        if(count):
            return True
        else:
            return False
