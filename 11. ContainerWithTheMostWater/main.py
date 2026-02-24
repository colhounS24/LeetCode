"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 
Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

My thinking:

sort the array.

1. brute force attempt. 2 pointers O(N^2)... very slow
2. good == biggest numbers && largest gap....

-- Note

2 pointers, left and right. Then be greedy and move them closer together

It is worth noting that I calcualte the first diff, then greedy algo the rest of the way


"""
class Solution:
    def maxArea(height: list[int]) -> int:
        # Set the max to the initial container.
        largest_area = min(height[0], height[len(height)-1]) * (len(height)-1)
        

        lh_pointer = 0
        rh_pointer = len(height) -1

        while rh_pointer > lh_pointer:
            # So the area is already reducing, all that I care about is if it improves the min

            if height[lh_pointer+1] > height[rh_pointer-1]:
                rh_pointer -= 1
            else:
                lh_pointer += 1
            new_container = min(height[lh_pointer],height[rh_pointer]) * (rh_pointer - lh_pointer)

            if new_container > largest_area:
                largest_area = new_container

        return largest_area


                    
print(Solution.maxArea([1,8,6,2,5,4,8,3,7]))        


        
        