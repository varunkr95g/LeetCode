class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        gain.insert(0,0)

        for i in range(len(gain)-1):
            gain[i+1]+=gain[i]
        
        
        
        return max(gain)
