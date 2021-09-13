class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        # sliding window algorithm with a hash table
        
        left = 0
        right = 0
        substring = 0
        last_indexed = {}
        
        while right < len(s):
            if s[right] in last_indexed:
                left = max(left, last_indexed[s[right]] + 1)
            substring = max(substring, right - left + 1)
            last_indexed[s[right]] = right
            right += 1
        return substring
        