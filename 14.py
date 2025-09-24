class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, character in enumerate(shortest):
            for other in strs:
                if other[i] != character:
                    return shortest[:i]