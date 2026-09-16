class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build frequency dictionary O(n)
        num_dict = {}

        for num in nums:

            if num not in num_dict:
                num_dict[num] = 1

            else:
                num_dict[num] += 1

        # return k largest values
        # bucket sort

        buckets = [[] for _ in range(len(nums)+1)]

        for val in num_dict:
            freq = num_dict[val]

            buckets[freq].append(val)

        output = []

        for sublist in reversed(buckets):
            if len(output) == k:
                break
            for value in sublist:
                if len(output) == k:
                    break

                output.append(value)
                
        return output