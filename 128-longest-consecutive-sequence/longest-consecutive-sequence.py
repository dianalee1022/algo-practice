class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCount = 0
        numbers = set(nums)
        
        for num in numbers:
            if num - 1 not in numbers:
                counter = 1
                while num + counter in numbers:
                    counter += 1
                maxCount = max(maxCount, counter)

        return maxCount

        