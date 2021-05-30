class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        sub_arr=[]

        dictionary={}
        
        for i in nums:
            if(i in dictionary):
                dictionary[i]+=1
            else:
                dictionary[i]=1
        
        # print dictionary
        
        values_dict=dictionary.values()
        
        values_dict.sort(reverse=True)
        
        for i in values_dict:
            for j in dictionary.keys():
                if(dictionary[j]==i):
                    sub_arr.append(j)
                    dictionary.pop(j)
                    break
        
        return sub_arr[:k]
