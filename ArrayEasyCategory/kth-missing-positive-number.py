class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        const_arr=[]


        for i in range(1,2002):
            const_arr.append(i)
        
        for i in arr:
            if( i in const_arr):
                const_arr.remove(i)
        
        if (k<len(const_arr)):
            return const_arr.pop(k-1)
        else:
            return 0
