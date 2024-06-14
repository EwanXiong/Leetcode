"""
Problem:
Given a string s, please find the longest sub string that does not contain repeated characters
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length = 0
        
        queue = []
        for i in s:
            if i in queue:
                length = max(length, len(queue))
                while i in queue:
                    queue.pop(0)

            queue.append(i)

        return max(length, len(queue))

S = Solution()
t1 = 'alskdjfhsjfkglkslaksjdhfhghdjakalskfdjghdalskdjfhghfjdkslalakdkaassdddffffgggjjhkkhllgk'
S.lengthOfLongestSubstring(t1)
