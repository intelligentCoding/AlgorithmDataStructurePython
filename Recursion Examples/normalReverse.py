

def reverse(s):
    #base case
    if len(s) <= 1:
        return s


    return s[len(s)-1] + reverse(s[0:len(s)-1])



print(reverse('poilkj'))