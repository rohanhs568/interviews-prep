class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)

        curr = 0
        max_l = 0
        counting = False

        for num in nums:

            if counting == False: # check suitable starter
                if num - 1 in nums: # not suitable starter
                    continue

                else: # suitable starter
                    counting = True # now counting
                    curr = 1 # sequence of length 1

            if counting == True:
                
                i = num + 1
                while i in nums:
                    curr += 1
                    i +=1

                max_l = max(curr, max_l)
                counting = False
        
        return max_l
            

                

        
        