class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        needed_dict = {}

        for i, num in enumerate(nums):

            needed = target - num

            if needed in needed_dict:
                return [needed_dict[needed], i]

            else:
                needed_dict[num] = i
            


            