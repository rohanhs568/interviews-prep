class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        result = []

        fixed = 0

        seen = set()

        while fixed < len(nums)-2:

            if fixed > 0 and nums[fixed] == nums[fixed - 1]:
                    fixed += 1
                    continue

        
            # now run two sum with pointers for fixed

            left = fixed + 1
            right = len(nums) - 1

            while left < right:
                

                total = nums[left] + nums[right] 

                if total == -nums[fixed]:
                    if (nums[left], nums[right], nums[fixed]) not in seen:
                        result.append([nums[left], nums[right], nums[fixed]])
                        seen.add((nums[left], nums[right], nums[fixed]))
                        left += 1
                        right -= 1
                        continue

                    left += 1
                    right -= 1

                    continue

                elif total < -nums[fixed]:
                    left += 1
                    continue

                elif total > -nums[fixed]:
                    right -= 1
                    continue
            
            fixed += 1

        return result
                



        