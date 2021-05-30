class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        listnum=list(str(num))

        # print listnum
        
        for i in range(len(listnum)):
            if(int(listnum[i])==6):
                listnum[i]='9'
                break
        
        return ''.join(listnum)
