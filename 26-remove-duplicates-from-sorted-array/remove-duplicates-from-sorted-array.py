class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # During iteration, note of the last dup pos
        # Every new element, swap the position
        # Every duplicate, keep the dup pos the same
        pos_to_swap = -1
        unique_number_count = 0
        previous = None
        for i in range(len(nums)):
            if nums[i] != previous:
                pos_to_swap += 1
                unique_number_count += 1
                previous = nums[i]
            if pos_to_swap < i:
                nums[pos_to_swap] = nums[i]
        return unique_number_count


        