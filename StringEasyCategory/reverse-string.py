class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if(len(s)%2==0):
            s.append(" ")

            start=0
            length=len(s)-1

            while(start!=length):
                s[start],s[length]=s[length],s[start]
                start+=1
                length-=1
            
            s.remove(" ")
            return s

        else:
            start = 0
            length = len(s) - 1

            while (start != length):
                s[start], s[length] = s[length], s[start]
                start += 1
                length -= 1

            return s
        # s.reverse()
