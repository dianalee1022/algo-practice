class Solution:
    def candy(self, ratings: List[int]) -> int:
        total_candy = 0
        up, down, peak = 0, 0, 0

        for i in range(len(ratings)):
            total_candy += 1
            if i >= 1:
                if ratings[i - 1] > ratings[i]:
                    up = 0
                    down += 1
                    total_candy += down - int(peak >= down)
                elif ratings[i - 1] == ratings[i]:
                    up = down = peak = 0
                else:
                    up += 1
                    down = 0
                    peak = up
                    total_candy += peak 

        return total_candy




        