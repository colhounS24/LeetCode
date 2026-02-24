"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.


Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.

"""

class Solution:
    def merge(self,intervals: list[list[int]]) -> list[list[int]]:
        final = []
        i = 0
        Solution.sort_arr(intervals)

        if len(intervals) == 1:
            return intervals
        
        elif len(intervals) ==2:
            if intervals[0][1] >= intervals[1][1]:
                return [intervals[0]]
            elif intervals[0][1] >= intervals[1][0]:
                
                temp =[intervals[0][0],intervals[1][1]]
                return [temp]
            
            else:
                return intervals
        else:
            current = intervals[0]
            for next_interval in intervals[1:]:
                if current[1] >= next_interval[0]:
                    current = [current[0], max(current[1], next_interval[1])]
                else:
                    final.append(current)
                    current = next_interval
            # append the last interval
            final.append(current)    
        return final

    @staticmethod
    def sort_arr(arr: list[list[int]]):
        
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(n-i-1):
                if arr[j][0] > arr[j+1][0]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                    swapped = True
            if not swapped:
                break


