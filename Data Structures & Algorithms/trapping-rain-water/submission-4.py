class Solution:
    def trap(self, height: List[int]) -> int:
        # try optimal 2 pointer solution
        # work inwards. once we know that a height is limited by the other side we have its water. 
        # the side then moves. 

        l_max = height[0]
        r_max = height[-1]

        l = 0
        r = len(height)-1

        total_water = 0

        while l < r:
            if l_max <= r_max:
                total_water += max(0, l_max - height[l])
                l += 1
                l_max = max(l_max, height[l])

            elif r_max < l_max:
                total_water += max(0, r_max - height[r])
                r -= 1
                r_max = max(r_max, height[r])

        return total_water

