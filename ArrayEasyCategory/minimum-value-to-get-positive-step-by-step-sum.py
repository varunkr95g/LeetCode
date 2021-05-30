class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val_arr=range(1,2500)

        # print val_arr
        
        
        nummin=min(nums)
        
        if(nummin)>0:
            return 1
        else:
            for val in val_arr:
                sub_arr = []
                count=0
                t = val
                for i in nums:
        
        
                        t+=i
                        sub_arr.append(t)
        
                for j in sub_arr:
                        if(j>0):
                            count+=1
        
                if(count==len(sub_arr)):
                    return val
                    break
