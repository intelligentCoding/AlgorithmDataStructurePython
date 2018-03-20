
def recursive(s):
    if(len(s) <= 1 ):
        return s
    for index,c in enumerate(s):
        print(index)
        newstr = s[0:index] + s[index+1]
        return c + recursive(newstr)




print(recursive('abc'))