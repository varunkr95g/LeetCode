class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        sub_arr=[]
        for element in range(left,right+1):
            count = 0
            for i in str(element):
                if(i!='0'):
                    if(element%int(i)==0):
                        count+=1
        
            if(count==len(str(element))):
                sub_arr.append(element)
        
        return sub_arr
