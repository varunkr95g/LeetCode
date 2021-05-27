class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        listC=list(coordinates)

        # print listC
        
        # print (int(coordinates[1])%2)
        if((listC[0] in ['a','c','e','g']) and (int(listC[1])%2!=0)):
            return False
        elif((listC[0] in ['a','c','e','g']) and (int(listC[1])%2==0)):
            return True
        elif((listC[0] in ['b','d','f','h']) and (int(listC[1])%2!=0)):
            return True
        elif((listC[0] in ['b','d','f','h']) and (int(listC[1])%2==0)):
            return False
