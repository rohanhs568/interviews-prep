class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        needed_dict = {}

        for i in range(len(nums)):
            
            num = nums[i]
            needed = target - num

            if needed in needed_dict:
                return [needed_dict[needed], i]

            else:
                needed_dict[num] = i
            


            