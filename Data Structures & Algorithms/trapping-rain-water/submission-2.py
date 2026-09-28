class Solution:
    def trap(self, height: List[int]) -> int:



        # next solution: one left sweep, one right sweep AND CALC

        # left sweep

        max_lefts = [0 for _ in range(len(height))]
        curr_max = 0

        for i in range(0, len(height)):
            
            max_lefts[i] = curr_max
            curr_max = max(curr_max, height[i])

        # right sweep

        max_rights = [0 for _ in range(len(height))]
        curr_max = 0
        total_water = 0

        for i in range(len(height)-1,-1,-1):
            
            max_rights[i] = curr_max
            curr_max = max(curr_max, height[i])
            water_held = max(0, min(max_lefts[i],max_rights[i]) - height[i])
            total_water += water_held


        return total_water
            
        
        