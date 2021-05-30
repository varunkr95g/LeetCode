class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq={}
        length=float(len(arr))
        
        for i in arr:
            freq[i]=arr.count(i)
        
        # print (freq)
        
        for i in freq:
            if(freq[i]>0.25*length):
                return i
