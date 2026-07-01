class Solution:
    def trap(self, height: List[int]) -> int:
        l , r = 0 , len(height)-1
        ml =height[0]
        mr = height[len(height)-1]
        sum = 0
        while(l<r):
            if ml < mr:
                l+=1
                water = ml - height[l]
                if(water > 0):
                    sum += water
                ml = max(ml,height[l])
            else:
                r-=1
                water = mr - height[r]
                if(water > 0):
                    sum += water
                mr = max(mr,height[r])

        return sum