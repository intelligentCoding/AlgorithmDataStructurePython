# Given an integer, create a function which returns the sum of all the individual digits
# in that integer. For example:
# if n = 4321, return 4+3+2+1


def sum_func(n):
    #base case
    if len(str(n)) == 1:
        return 1
    else:
        # print(str(9%10))
        # print("N%10 = " + str(n%10) + " n /10 = " + str(n//10))
        return (n % 10) + sum_func(n//10)

print(sum_func(4321))