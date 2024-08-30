class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = [0]
        stor = []
        for n in s:
            if n in stor:
                pos.append(len(stor)) # add the longest substring sequence length to the list
                stor = stor[stor.index(n)+1:] # if the letter in the storage list update the list by removing the first                                                 #incidence of the letter
                stor.append(n) # add the new letter to conintue calculating the longest substring
            else:
                stor.append(n) # the letter is not in the storage 
                
        return max(len(stor), max(pos)) # return the bigger
        