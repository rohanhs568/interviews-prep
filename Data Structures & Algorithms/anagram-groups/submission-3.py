class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_str_dict = {}

        for string in strs:
            # build array
            count = [0] * 26
            
            for char in string:
                count[ord(char) - ord("a")] += 1 # array built

            key = tuple(count) # hashable 

            # check in dictionary
            if key in all_str_dict:
                all_str_dict[key].append(string)

            else:
                all_str_dict[key] = [string]

        return list(all_str_dict.values())

        