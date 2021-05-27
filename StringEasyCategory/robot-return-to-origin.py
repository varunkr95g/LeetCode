class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        xaxis=0
        yaxis=0
        
        for i in moves:
            if i=='U':
                xaxis+=1
            elif i=='D':
                xaxis-=1
            elif i=='L':
                yaxis-=1
            elif i=='R':
                yaxis+=1
        
        if(xaxis==0 and yaxis==0):
            return True
        else:
            return False
