

def reverse(s):
    #base case
    if len(s) <= 1:
        return s


    return reverse(s[1:]) + s[0]



print(reverse('abcdef'))