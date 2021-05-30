class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        sub_arr=[]

        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if(abs(arr1[i]-arr2[j])<=d):
        
                    sub_arr.append(arr1[i])
        
        # print sub_arr
        
        x=[x for x in arr1 if x not in sub_arr]
        
        return len(x)
