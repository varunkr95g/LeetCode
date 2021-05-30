class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        listjewels=list(jewels)
        liststones=list(stones)
        
        # print (listjewels)
        # print (liststones)
        
        c=[x for x in liststones if x in listjewels]
        
        return  len(c)
