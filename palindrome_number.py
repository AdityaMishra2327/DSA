class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False 
        rsum = 0
        n =x
      

        while n>0:
            digit = n % 10
            rsum = rsum * 10 + digit 
            n = n // 10
        return rsum == x 
