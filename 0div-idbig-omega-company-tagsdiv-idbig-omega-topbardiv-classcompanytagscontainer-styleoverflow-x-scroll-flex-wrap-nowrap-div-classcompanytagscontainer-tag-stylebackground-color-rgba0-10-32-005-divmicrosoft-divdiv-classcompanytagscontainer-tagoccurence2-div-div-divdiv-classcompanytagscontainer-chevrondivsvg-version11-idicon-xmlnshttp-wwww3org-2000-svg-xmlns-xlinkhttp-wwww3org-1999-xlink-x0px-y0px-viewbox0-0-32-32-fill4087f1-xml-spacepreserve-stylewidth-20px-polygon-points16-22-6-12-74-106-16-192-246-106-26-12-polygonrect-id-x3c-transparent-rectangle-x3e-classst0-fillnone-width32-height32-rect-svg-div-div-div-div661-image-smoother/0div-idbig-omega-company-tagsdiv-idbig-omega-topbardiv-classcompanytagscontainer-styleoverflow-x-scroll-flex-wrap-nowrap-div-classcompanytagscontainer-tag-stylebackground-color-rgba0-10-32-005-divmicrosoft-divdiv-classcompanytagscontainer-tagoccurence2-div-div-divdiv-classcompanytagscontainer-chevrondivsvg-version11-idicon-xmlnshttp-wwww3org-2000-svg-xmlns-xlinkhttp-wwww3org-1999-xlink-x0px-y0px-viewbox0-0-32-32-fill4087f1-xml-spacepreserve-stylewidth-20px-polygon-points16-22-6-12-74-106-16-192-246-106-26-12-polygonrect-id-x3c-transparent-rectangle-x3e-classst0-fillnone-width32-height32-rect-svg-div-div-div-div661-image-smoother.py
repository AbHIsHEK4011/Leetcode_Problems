class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        ROWS,COLS= len(img), len(img[0])
        res= [[0] * COLS for _ in range(ROWS)]
        
        for i in range(ROWS):
            for j in range(COLS):
                t,c=0,0
                for q in range(i-1,i+2):
                    for p in range(j-1,j+2):
                        if q<0 or q==ROWS or p<0 or p==COLS:
                            continue
                        
                        t += img[q][p]
                        c += 1
                res[i][j]= t//c
        return res
        