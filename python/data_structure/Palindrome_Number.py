# https://leetcode.com/problems/palindrome-number/description/

# false

def isPalindrome(x: int) -> bool:
    # Negative != Palindrome
    if x < 0:
        return False

    if x % 10 == 0 and x != 0:
        return False

    reversed_num = 0

    # revered num and compare
    while x > reversed_num:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10

    # check reversed_num == [:x]
    return x == reversed_num or x == reversed_num // 10
