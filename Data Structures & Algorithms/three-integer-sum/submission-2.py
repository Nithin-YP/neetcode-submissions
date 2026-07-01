class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for a in range(len(nums)):
            if a>0 and nums[a-1]==nums[a]:
                continue
            l , r = a+1 , len(nums)-1
            while(l<r):
                sum = nums[a] + nums[l] + nums[r]
                if sum > 0:
                    r -=1
                elif sum < 0:
                    l +=1
                else:
                    res.append([nums[a],nums[l],nums[r]])
                    l +=1
                    r -=1
                    while(l<r and nums[l] == nums[l-1]):
                        l+=1
                    while(l<r and nums[r] == nums[r+1]):
                        r-=1
        return res