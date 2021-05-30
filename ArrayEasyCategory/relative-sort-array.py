class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        sub_arr=[]

        dictionary={}
        
        for i in arr1:
            if(i in dictionary):
                dictionary[i]+=1
            else:
                dictionary[i]=1
        
        # print dictionary
        
        for i in arr2:
            for key,value in dictionary.items():
                if(i==key):
                    for j in range(value):
                        sub_arr.append(i)
        
        key=dictionary.keys()
        
        x=[x for x in key if x not in arr2]
        
        for i in sorted(x):
            j=dictionary[i]
            for k in range(j):
                sub_arr.append(i)
        
        
        return sub_arr
