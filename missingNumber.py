def finder3(arr1, arr2):
    result=0

    # Perform an XOR between the numbers in the arrays
    for num in arr1+arr2:
        # 1234134
        print("*" *50)
        print("Result is = " + str(result))
        print("*" *50)
        print("Number is " + str(num))
        result^=num
        print("result is " + str(result))

    return result


finder3([5,6,7,8], [8,6,5,6])