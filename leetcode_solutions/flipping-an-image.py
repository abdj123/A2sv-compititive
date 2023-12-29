class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res=[]
        
        for i in range(len(image)):
            temp=image[i][::-1]
            for j in range(len(temp)):
                if(temp[j]==0):
                    temp[j]=1
                else:
                    temp[j]=0
            res.append(temp)
        
        return res
                    