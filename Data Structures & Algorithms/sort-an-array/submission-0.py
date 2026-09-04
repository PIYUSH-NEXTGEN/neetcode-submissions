class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        sorted_arr = []

        while len(nums) > 0 :
            lowest = nums[0]

            for i in nums:
                if i < lowest:
                    lowest = i

            sorted_arr.append(lowest)
            nums.remove(lowest)

        return sorted_arr
                