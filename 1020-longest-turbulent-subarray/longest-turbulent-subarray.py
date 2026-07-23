class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        switch = 0 # +1 for incremental -1 for decremental
        current_range = 1
        result = 0

        if len(arr) < 2:
            return current_range

        for i in range(1, len(arr)):
            curr = arr[i]
            prev = arr[i - 1]

            if curr > prev: # +1
                if switch <= 0:
                    current_range += 1
                else:
                    result = max(result, current_range)
                    current_range = 2
                switch = 1
            elif curr < prev: # -1
                if switch >= 0:
                    current_range += 1
                else:
                    result = max(result, current_range)
                    current_range = 2
                switch = -1
            else:
                result = max(result, current_range)
                switch = 0
                current_range = 1

        return max(current_range, result)
            
        