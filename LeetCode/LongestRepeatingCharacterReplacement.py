## Time Limit Exceeded 
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         hashMap = {} 
#         result = 0 
        
#         l = 0 
#         maxf = 0
#         for r in range(len(s)):
#             hashMap[s[r]] = 1 + hashMap.get(s[r],0)
            
#             while (r-l+1) - max(hashMap.values()) >  k: 
#                 hashMap[s[l]] -= 1
#                 l = + 1 
#             result = max(result,r-l+1)
#         return result 
## Solution from https://www.youtube.com/watch?v=gqXU1UyA8pk
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res