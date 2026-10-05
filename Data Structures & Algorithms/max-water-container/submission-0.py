from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        best = 0

        while l < r:
            width = r - l
            level = min(height[l], height[r])   
            best = max(best, level * width)

            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1                           

        return best