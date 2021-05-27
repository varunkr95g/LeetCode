class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        p2=paragraph.replace("!","")
        p2=p2.replace("?","")
        p2=p2.replace("'","")
        p2=p2.replace(","," ")
        p2=p2.replace(";","")
        p2=p2.replace(".","")
        
        p2=p2.lower()
        listpara=p2.split(" ")
        # print (listpara)
        
        # print (paragraph)
        # paragraph.split(" ")
        
        
        
        dictionary={}
        
        for i in listpara:
            if (i in dictionary):
                dictionary[i]+=1
            else:
                dictionary[i]=1
        
        if("" in dictionary):
            dictionary.pop("")
        
        if(banned):
            for i in banned:
                if ( i in dictionary):
                    dictionary.pop(i)
        
        # print dictionary
        
        max_val=max(dictionary.values())
        
        # print (max_val)
        
        for key,value in dictionary.items():
            if value==max_val:
                return key
