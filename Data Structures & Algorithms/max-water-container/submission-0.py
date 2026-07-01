class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxa = 0
        l , r = 0 , len(heights)-1
        while(l<r):
            area = min(heights[r],heights[l]) * (r-l)
            maxa = max(maxa,area)
            if(heights[r] <= heights[l]):
                r -= 1
            elif(heights[l]<heights[r]):
                l+=1
        return maxa