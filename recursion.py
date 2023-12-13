class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        num_list = []
        for m in matrix:
            for j in m:
                num_list.append(j)
        l,r = 0, len(num_list)-1
        while l <= r:
            m = (l+r)//2
            if num_list[m] > target:
                r = m - 1
            if num_list[m] < target:
                l = m + 1
            if num_list[m] == target:
                return True
        return False

             
    
a = Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3)
print(a)