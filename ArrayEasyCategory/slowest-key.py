class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        sub_arr=[]
        str_key=[]
        sub_arr.append(releaseTimes[0])
        
        for i in range(1,len(releaseTimes)):
            sub_arr.append(releaseTimes[i]-releaseTimes[i-1])
        
        # sub_arr_rev=sub_arr[::-1]
        # print sub_arr_rev
        max_sub_arr=max(sub_arr)
        
        for i in range(len(sub_arr)):
            if(sub_arr[i]==max_sub_arr):
                str_key.append(keysPressed[i])
        
        return max(str_key)
