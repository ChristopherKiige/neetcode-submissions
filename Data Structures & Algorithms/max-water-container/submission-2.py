class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,max_area,r = 0,0 ,len(heights) - 1
        
        while r > l:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height

            if area > max_area:
                max_area = area

            if(heights[l] > heights[r]):
                r -= 1
            else:
                l += 1
        return max_area
        