def palidrome(n):
    reverse = "".join(reversed(n))
    if (n == reverse):
        return True
    return False

print(palidrome("aka"))



