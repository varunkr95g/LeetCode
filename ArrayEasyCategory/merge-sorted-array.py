class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        sub_arr=[]

        for i in range(n):
            sub_arr.append(nums2[i])
        
        for i in range(m):
            sub_arr.append(nums1[i])
        
        sub_arr.sort()
        
        for i in range(len(sub_arr)):
            nums1[i]=sub_arr[i]
        
        
