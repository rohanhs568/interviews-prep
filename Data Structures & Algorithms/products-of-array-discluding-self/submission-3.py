class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        leftprod = [nums[0]]
        output = [nums[-1]]

        for i in range(1,len(nums)):
            leftval = nums[i] * leftprod[i-1]
            rightval = nums[-i-1] * output[i-1]

            leftprod.append(leftval)
            output.append(rightval)

        output.reverse()

        for i in range(len(nums)):
            left = leftprod[i-1] if i > 0 else 1
            right = output[i+1] if i < len(nums)-1 else 1

            output[i] = left*right

        return output