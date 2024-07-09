def isPalindrome(self, x):
    if x < 0:
        return False

    # Initialize variables
    original = x
    reversed_num = 0

    # Reverse the integer while keeping the original
    while x > 0:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10

    # Check if the reversed number is the same as the original
    return original == reversed_num