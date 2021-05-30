class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        sortheight=sorted(heights)
        total=0
        # print sortheight
        
        for i in range(len(heights)):
            if(heights[i]!=sortheight[i]):
                total+=1
        
        return total
