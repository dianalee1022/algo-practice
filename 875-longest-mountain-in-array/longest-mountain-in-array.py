class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        up = down = peak = 0
        mountain_range = 0
        current_mountain_range = 1

        for i in range(1, len(arr)):
            curr = arr[i]
            prev = arr[i - 1]
            if curr == prev:
                # Reset everything
                up = down = peak = 0
                current_mountain_range = 1
            elif curr > prev:
                if up == 0 and i > 1:
                    # mountain_range = max(mountain_range, current_mountain_range)
                    current_mountain_range = 1
                current_mountain_range += 1
                up += 1
                # down = 0
                peak = up
            else: # curr < prev = Down
                up = 0
                # down += 1
                if peak != 0:
                    current_mountain_range += 1
                    if current_mountain_range > mountain_range:
                        mountain_range = current_mountain_range 

            print("Current: " + str(curr) + " And previous: " + str(prev) + " and current_mountain_range: " + str(current_mountain_range))
            

        return mountain_range
        