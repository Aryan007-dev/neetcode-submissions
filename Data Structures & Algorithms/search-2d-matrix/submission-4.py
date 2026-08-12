class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        rows = len(matrix)
        cols= len(matrix[0])
        r = rows*cols-1
        while l<=r:
            mid = (l+r)//2
            row = mid//cols
            col = mid%cols
            if matrix[row][col]>target:
                    r=mid-1
            elif matrix[row][col]<target: 
                    l = mid+1
            else:
                return True
        return False    
        
                       


