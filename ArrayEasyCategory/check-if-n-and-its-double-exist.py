class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        
        
        
        
        count_arr=0
        x=[x*2 for x in arr]
        
        for i in arr:
            if(i%2==0):
                x.append(i//2)
        
        arr.sort()
        x.sort()
        
        for i in arr:
            if(i in x):
                count_arr+=1
        
        if(count_arr>=2):
            return True
        else:
            return False
