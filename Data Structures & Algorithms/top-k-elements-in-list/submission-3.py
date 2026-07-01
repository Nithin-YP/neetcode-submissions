class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] +=1
        
        buckets= [[] for i in range(len(nums)+1)]
        for k1,v in d.items():
            buckets[v].append(k1)
        res=[]
        for i in range(len(buckets)-1,0,-1):
            for x in buckets[i]:
                res.append(x)
                if(len(res)==k):
                    return res
        return res