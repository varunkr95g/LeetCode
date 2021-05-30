class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        k=[]

        # ["type","color","name"]
        
        for i in range(len((items))):
            if ((ruleKey=="color") and (items[i][1])==ruleValue):
                k.append(1)
            elif ((ruleKey=="type") and (items[i][0])==ruleValue):
                k.append(1)
            elif ((ruleKey == "name") and (items[i][2]) == ruleValue):
                k.append(1)
        
        return (len(k))
