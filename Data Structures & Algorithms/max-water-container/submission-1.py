class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # brute force done time to think
        # O(n^2) combos , need clever way to know when to skip or ignore...
        # hmm

        # calculation is min(heights[i], heights[j]) * (j-i)

        # fix i. imagine two pointer solution. we move from the smallest one
        # if i shorter than j, we can only increase the size by moving outwards, hence we have already found the max for this i 
        # how can we be sure we're not missing any? we are guaranteed at soem point to reach all (note we need to account for equal case. if equal move random one)
        # how can we be sure that every short one will reach its outermost "tall partner"
        # dk
        # ok - not two pointer in same sense. we fix one and work inwards. then reset poitner


        fixed = 0
        outer = len(heights) - 1
        maximum = 0

        while fixed < len(heights) - 1 and fixed < outer:
            


            if heights[outer] < heights[fixed]:
                maximum = max(maximum, min(heights[fixed], heights[outer]) * (outer-fixed))
                outer -= 1

            elif heights[outer] >= heights[fixed]:
                maximum = max(maximum, min(heights[fixed], heights[outer]) * (outer-fixed))
                fixed += 1
                outer = len(heights) - 1

        return maximum




        