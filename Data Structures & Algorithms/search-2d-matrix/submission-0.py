class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in range(len(matrix)):
            lo, hi = 0, len(matrix[arr]) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if matrix[arr][mid] == target: return True

                elif matrix[arr][mid] < target: lo = mid + 1

                else: hi = mid - 1
            
        return False