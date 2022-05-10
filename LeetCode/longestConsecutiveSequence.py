## Solution from https://www.youtube.com/watch?v=P6RZZMu_maU
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        arrSet = set(nums)
        long = 0
        
        for num in nums:
            if (num - 1) not in arrSet:
                length = 1
                while (num + length) in arrSet:
                    length += 1
                long = max(length, long)
        return long