class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] +=1
        
        res = [key for key,item in heapq.nlargest(k,d.items(),key = lambda x : x[1])]
        return res