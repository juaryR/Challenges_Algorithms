class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for num in nums:
            count[num] = 1 + count.get(num,0)
        for num,c in count.items():
            freq[c].append(num)
        
        result = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                result.append(num)
                if len(result) ==k:
                    return result 
