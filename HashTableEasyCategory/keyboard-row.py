class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first_row="qwertyuiopQWERTYUIOP"
        second_row="asdfghjklASDFGHJKL"
        third_row="zxcvbnmZXCVBNM"
        
        list_fr=list(first_row)
        list_sr=list(second_row)
        list_tr=list(third_row)
        # print (list_sr)
        
        sub_arr=[]
        
        for element in words:
            list_element=list(element)
            count1=0;count2=0;count3=0
        
            for el in list_element:
                if((el in list_sr) and( (el not in list_fr) or (el not in list_tr))):
                    count1+=1
                elif(el in list_fr and( (el not in list_sr) or (el not in list_tr))):
                    count2 += 1
                elif(el in list_tr and( (el not in list_sr) or (el not in list_fr))):
                    count3+=1
            if((count1==len(list_element)) or (count2==len(list_element)) or (count3==len(list_element)) ):
                sub_arr.append(element)
        
        
        
        return sub_arr
