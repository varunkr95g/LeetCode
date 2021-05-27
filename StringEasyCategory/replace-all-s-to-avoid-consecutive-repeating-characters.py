class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        lists=list(s)

        for i in range(len(lists)):
            if(lists[i]=="?"):
                lists[i]="a"
                if(lists[i-1]==lists[i]):
                    lists[i]="b"
        
        for i in range(len(lists)-1):
            if(lists[i]==lists[i+1] and (lists[i-1]!="z")):
                lists[i]="z"
            elif(lists[i]==lists[i+1] and (lists[i-1]=="z")):
                lists[i] = "c"
        
        return ''.join(lists)
