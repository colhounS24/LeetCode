class Solution:
    @staticmethod
    def _binarySearch(arr, target):
        a = 0
        b = (len(arr)*len(arr[0])) - 1

        while a <= b:
            mid = (a + b) // 2

            if arr[mid // len(arr[0])][mid % len(arr[0])] > target:
                b = mid - 1
            
            elif arr[mid // len(arr[0])][mid % len(arr[0])] < target:
                a = mid + 1

            else:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self._binarySearch(matrix, target)
        