class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        image_2=[]

        for i in range(len(image)):
            # print (image[i])
            image[i].reverse()
            image[i]=[1 if image[i][j]==0 else 0 for j in range(len(image[i]))]
            image_2.append(image[i])
        
        return image_2
