class Solution(object):
    def longestCommonPrefix(strs):
        if not strs:
            return ""
        
        base = strs[0]
        for i in range(len(base)):
            for word in strs[1:]:  # Iterate over the remaining words
                if i == len(word) or word[i] != base[i]:  # Check if mismatch or end of a word
                    return base[:i]
        return base

strs1 =['flower','flow','flight']

print("longestCommonPrefix: ", Solution.longestCommonPrefix(strs1))