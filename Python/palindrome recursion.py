def rec_palindrome(a):
    if len(a)<1:
        print("palindrome")
    else:
        if a[0]==a[-1]:
            return rec_palindrome(a[1:-1])
        else:
            print("not palindrome")
