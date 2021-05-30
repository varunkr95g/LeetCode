class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        count=0
        arr=[]
        
        for i,j in zip(range(len(startTime)),range(len(endTime))):
            arr.append((startTime[i],endTime[j]))
        
        for i in range(len(arr)):
            if(arr[i][0]<=queryTime<=arr[i][1]):
                count+=1
        
        return count
