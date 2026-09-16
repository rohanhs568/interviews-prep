class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        leftprod = [nums[0]]
        rightprod = [nums[-1]]

        for i in range(1,len(nums)):
            leftval = nums[i] * leftprod[i-1]
            rightval = nums[-i-1] * rightprod[i-1]

            leftprod.append(leftval)
            rightprod.append(rightval)

        rightprod.reverse()

        products = []

        for i in range(len(nums)):
            left = leftprod[i-1] if i > 0 else 1
            right = rightprod[i+1] if i < len(nums)-1 else 1

            products.append(left*right)

        return products