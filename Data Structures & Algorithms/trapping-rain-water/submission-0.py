class Solution:
    def trap(self, height: List[int]) -> int:
            ml =[]
            v=0
            for x in height:
                v = max(v,x)
                ml.append(v)
            
            mr =[0]*len(height)
            v=0
            for i in range(len(height)-1,-1,-1):
                v = max(v,height[i])
                mr[i] = v
            
            sum = 0
            for i in range(len(height)):
                sum+= (min(ml[i],mr[i]) - height[i])
            
            return sum

