class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        sub_arr=[]
        
        for i in range(1,len(arr)):
            sub_arr.append(arr[i]-arr[i-1])
        
        return max(sub_arr)==min(sub_arr)
