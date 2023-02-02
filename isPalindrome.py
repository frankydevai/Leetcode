def isPalindrome(self, x: int) -> bool:
    if str(x)[::-1] == str(x)[::]:
        return True
    else:
        return False


# Second Solutaion

def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        new_n = 0
        n = x
        while x > 0:
            new_n = new_n * 10 + x%10
            x //=10
        return new_n == n