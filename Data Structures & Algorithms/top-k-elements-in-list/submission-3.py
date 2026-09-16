class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build frequency dictionary O(n)
        num_dict = {}

        for num in nums:
            num_dict[num] = num_dict.get(num, 0) +1 # num_dict.get(key, default) LEARN!

        # return k largest values
        # bucket sort

        buckets = [[] for _ in range(len(nums)+1)]

        for val, freq in num_dict.items(): # LEARN, Like enumerate. .items() on dict item

            buckets[freq].append(val)

        output = []

        for sublist in reversed(buckets):
            if len(output) == k:
                return output
            for value in sublist:
                if len(output) == k:
                    return output

                output.append(value)
                
        