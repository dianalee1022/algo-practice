class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force - O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # Optimized solution - O(n) but with space complexity O(n) in worst case
        hashMap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashMap:
                return [hashMap.get(target - nums[i]), i]
            else:
                hashMap[nums[i]] = i



                
                
        