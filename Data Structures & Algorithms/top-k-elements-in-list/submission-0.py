class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        final_arr = []

        for i in nums:
            hash_map[i] = hash_map.get(i, 0) + 1

        for j in range(k):
            highest_freq = 0
            highest_freq_elem = None

            for elem, freq in hash_map.items():
                if freq > highest_freq:
                    highest_freq = freq
                    highest_freq_elem = elem

            final_arr.append(highest_freq_elem)
            del hash_map[highest_freq_elem]

        return final_arr




