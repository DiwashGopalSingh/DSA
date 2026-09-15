class Solution(object):
    def lengthOfLongestSubstring(self, s):
        sub = ""
        count = 0
        
        for ele in s:
            if ele in sub:
                sub = sub[sub.index(ele) + 1:]
            sub += ele
            if len(sub) > count:
                count = len(sub)
                
        return count