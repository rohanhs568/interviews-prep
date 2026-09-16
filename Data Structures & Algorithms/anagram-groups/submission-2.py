class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_str_dict = {}
        anag_list = []
        dict_counter = 0

        for string in strs:
            # build array
            count = [0] * 26
            
            for char in string:
                count[ord(char) - ord("a")] += 1 # array built

            key = tuple(count) # hashable 

            # check in dictionary
            if key in all_str_dict:
                anag_list[all_str_dict[key]].append(string)

            else:
                anag_list.append([string])
                all_str_dict[key] = dict_counter
                dict_counter += 1

        return anag_list

        