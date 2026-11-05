class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area_holder = 0
        L,R = 0, len(heights) - 1
        while L < R:
            area = (R - L) * min(heights[R], heights[L])
            if area > area_holder:
                area_holder = area
            if heights[R] < heights[L]:
                R -= 1
                continue
            elif heights[L] < heights[R]:
                L += 1
                continue
            else:
                L += 1
                continue
        return max(area, area_holder)
