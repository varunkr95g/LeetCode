class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sum=0;

        for i in range(1,len(points)):
        
            if(points[i][0]!=points[i-1][0] and points[i][1]==points[i-1][1]):
                sum+=abs(points[i][0]-points[i-1][0])
            elif (points[i][0]==points[i-1][0] and points[i][1]!=points[i-1][1]):
                sum+= abs(points[i][1] - points[i - 1][1])
            else:
                ax=abs(points[i][0]-points[i-1][0])
                ay=abs(points[i][1]-points[i-1][1])
                sum+=max(ax,ay)
        
        return sum
        
