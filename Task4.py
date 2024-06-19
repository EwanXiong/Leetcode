"""
Problem:
Given an integer x, if x is a palindrome, return true; otherwise, return false. 
Palindrome number it means that the integers are read the same in forward order (from left to right) and reverse order (from right to left).
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
      input_int = str(x)
      p_int = input_int[::-1]
      if input_int == p_int:
        print("The number ", x, " is a Palindrome")
        return(True)
      else:
        print("The number ", x, " is not a Palindrome")
        return(False)

S = Solution()
S.isPalindrome('121')
