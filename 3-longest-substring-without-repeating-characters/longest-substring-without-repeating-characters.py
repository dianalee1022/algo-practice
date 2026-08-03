class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0

        maxLength = 0
        left = right = 0
        dups = set()
        for right in range(len(s)):
            character = s[right]
            while character in dups:
                dups.remove(s[left])
                left += 1
            dups.add(character)
            maxLength = max(maxLength, right - left + 1)
        return maxLength



        