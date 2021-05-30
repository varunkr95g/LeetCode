class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        sub_arr=[]
        odd=0
        
        
        for i in range(len(arr)):
            for j in range(i+2,len(arr)+1):
                if(j-i==3):
                    sub_arr.append(arr[i:j])
        
        print (sub_arr)
        
        for i in range(len(sub_arr)):
            total = 0;
            for j in sub_arr[i]:
                if (j%2!=0):
                    total+=1;
                    if(total==3):
                        odd=1
                        break
        
        
        if(odd):
            return True
        else:
            return False
