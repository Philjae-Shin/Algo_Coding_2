# https://leetcode.com/problems/palindrome-number/description/

# false

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    if x % 10 == 0 and x != 0:
        return False

    reversed_num = 0

    while x > reversed_num:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10

    return x == reversed_num or x == reversed_num // 10
