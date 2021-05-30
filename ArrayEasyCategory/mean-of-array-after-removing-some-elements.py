class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        arr.sort()

        initelement=int(len(arr)*0.05)
        finalelement=int(len(arr)*0.95)
        
        
        # print initelement
        # print finalelement
        
        return (sum(arr[initelement:finalelement]))/(len(arr)*0.9)
