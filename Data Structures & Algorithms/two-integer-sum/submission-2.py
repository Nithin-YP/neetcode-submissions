class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map ={}
        for i in range(len(nums)):
            want = target - nums[i]
            if want in map :
                return [map[want] , i]
            else:
                map[nums[i]] = i
            