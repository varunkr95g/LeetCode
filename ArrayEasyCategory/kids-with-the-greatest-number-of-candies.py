class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_val=max(candies)
        ae=[None]*len(candies)
        bool_list=[]
        
        
        for i in range(len(candies)):
            ae[i]=candies[i]+extraCandies
        
        
        for i in range(len(candies)):
            if(ae[i]>=max_val):
                bool_list.append(True)
            else :
                bool_list.append(False)
        
        return bool_list
        
