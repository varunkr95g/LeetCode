class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if(len(arr)<3):
            return False
        else:
            length_arr = []
            max_val = max(arr)

            for i in range(len(arr)):
                if (arr[i] == max_val):
                    length_arr.append(i)

            if (len(length_arr) > 1):
                return False
            elif (max_val == arr[-1] or max_val==arr[0]):
                return False

            elif(arr[:length_arr[0]+1]==sorted(arr[:length_arr[0]+1]) and arr[length_arr[0]+1:]==sorted(arr[length_arr[0]+1:],reverse=True) and len(arr[:length_arr[0]+1])== len(list(set(arr[:length_arr[0]+1]))) and len(arr[length_arr[0]+1:])== len(list(set(arr[length_arr[0]+1:]))) ):
                return True
            else:
                return False
