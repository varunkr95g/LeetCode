class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x==1):
            return 1
        else:
            sub_arr=[]

            for i in range(0,x):
                if(i*i<=x):
                    sub_arr.append(i)

            if(sub_arr):
                return max(sub_arr)
            else:
                return 0
