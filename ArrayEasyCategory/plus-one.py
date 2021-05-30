class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
#         if (digits[-1]!=9):
#             digits[-1]+=1
#         else:

#             digits[-1]=0
#             digits.insert(-2,1)

#         return digits
        digits_str=[]
        list_digits=[]
        list_digits_int=[]
        
        for i in range(len(digits)):
            digits_str.append(str(digits[i]))
        
        # print (digits_str)
        digits_str_num=''.join(digits_str)
        digits_str_num_int=int(digits_str_num)
        
        digits_str_num_int+=1
        list_digits=list(str(digits_str_num_int))
        
        # print (list_digits)
        
        for i in range(len(list_digits)):
            list_digits_int.append(int(list_digits[i]))
        
        return list_digits_int
