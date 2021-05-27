class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        sub_arr_right=[]
        sub_arr_left=[]
        
        for i in range(len(paths)):
            sub_arr_right.append(paths[i][1])
            sub_arr_left.append(paths[i][0])
        
        # print (sub_arr_right)
        # print (sub_arr_left)
        
        
        for i in sub_arr_right:
            if( i not in sub_arr_left):
                return i
                break
