import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i,0)+1
        
        heap = [(freq,val) for val,freq in count.items()]
        heapq.heapify_max(heap)

        res = []

        while len(res) < k:
            freq, val = heapq.heappop_max(heap)
            res.append(val)
        
        return res

