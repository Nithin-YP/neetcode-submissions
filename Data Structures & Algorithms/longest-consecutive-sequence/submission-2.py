class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        st = set(nums)
        for n in nums:
            if n-1 not in st:
                length = 0
                while(n+length) in st:
                    length += 1
                longest = max(longest,length)
        return longest
                