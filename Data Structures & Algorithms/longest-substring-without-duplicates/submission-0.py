class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            char = s[right]

            if char in hashmap:
                left = max(left, hashmap[char] + 1)

            hashmap[char] = right

            current_length = right - left + 1
            max_length = max(max_length, current_length)

        return max_length