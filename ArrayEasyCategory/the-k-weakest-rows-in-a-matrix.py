class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        dictionary={}
        arr1=[]
        arr2=[]
        
        for i in range(len(mat)):
            count1=0
            # print mat[i]
            for j in mat[i]:
                if(j ==1):
                    count1+=1
            # print count1
        
            dictionary[i]=count1
        
        # print dictionary
        # print sorted(dictionary.values())
        arr1=sorted(dictionary.values())
        
        for i in arr1:
            for l in dictionary.keys():
                if(dictionary[l]==i):
                    arr2.append(l)
                    dictionary.pop(l)
                    break
        
        return arr2[0:k]
