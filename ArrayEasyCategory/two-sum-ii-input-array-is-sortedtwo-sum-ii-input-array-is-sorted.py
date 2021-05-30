class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        sub_arr=[]

        low=0
        high=len(numbers)-1
        
        while(low!=high):
            if((numbers[low]+numbers[high])==target):
                sub_arr.append(low+1)
                sub_arr.append(high+1)
                break
            elif((numbers[low]+numbers[high])>target):
                high-=1
            elif ((numbers[low] + numbers[high]) < target):
                low+=1
        
        
        
        return sub_arr
