# 회문 숫자 거꾸로 읽어도 똑같은 숫자
# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        temp = x
        revertedNumber = 0
        while temp > 0:
            revertedNumber = revertedNumber * 10 + temp % 10
            temp //= 10

        return x == revertedNumber