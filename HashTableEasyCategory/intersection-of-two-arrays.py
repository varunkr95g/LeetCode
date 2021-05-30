class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        length1=len(nums1)
        length2=len(nums2)
        sub_arr=[]
        sub_arr_2=[]
        
        if length1 > length2:
            for i in range(len(nums2)):
                if( nums2[i] in nums1):
                    sub_arr.append(nums2[i])
        else:
            for i in range(len(nums1)):
                if (nums1[i] in nums2):
                    sub_arr.append(nums1[i])
        
        
        sub_arr_2=list(set(sub_arr))
        
        return sub_arr_2
