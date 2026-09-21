class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        best = 0

        for n in num_set:
            if n - 1 not in num_set:
                cur = n
                length = 1
                while cur + 1 in num_set:
                    cur += 1
                    length += 1
                best = max(best, length)

        return best





            
        