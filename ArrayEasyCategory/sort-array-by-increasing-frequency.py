class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dictionary={}
        dictionary_2={}
        sub_arr=[]
        
        for i in nums:
            if(i in dictionary):
                dictionary[i]+=1
            else:
                dictionary[i]=1
        
        # dictionary_2=sorted(dictionary, key=dictionary.get)
        #
        # print dictionary
        
        for j in sorted(dictionary.values()):
            for k in sorted(dictionary.keys(),reverse=True):
                if(dictionary[k]==j):
                    for i in range(j):
                        sub_arr.append(k)
                    dictionary.pop(k)

        return sub_arr
