class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_l = 0

        for num in nums:
            if num - 1 not in nums:
                i = num + 1
                curr = 1

                while num + curr in nums:
                    curr += 1
                    i += 1

                max_l = max(curr, max_l)
        
        return max_l
        