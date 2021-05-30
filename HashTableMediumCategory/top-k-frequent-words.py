class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dictionary={}
        sub_arr=[]
        
        
        for i in words:
            if(i in dictionary):
                dictionary[i]+=1
            else:
                dictionary[i]=1
        
        # print dictionary
        values_dict=dictionary.values()
        
        values_dict.sort(reverse=True)
        
        for i in values_dict:
            for j in sorted(dictionary.keys()):
                if(dictionary[j]==i):
                    sub_arr.append(j)
                    dictionary.pop(j)
                    break
        
        return sub_arr[:k]
