class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq = {}
        num_arr=[]
        
        for i in arr:
            freq[i]=arr.count(i)
        
        
        # print (freq)
        
        for i in freq:
            if(i==freq[i]):
                num_arr.append(i)
        
        if (num_arr):
            return max(num_arr)
        else:
            return -1
