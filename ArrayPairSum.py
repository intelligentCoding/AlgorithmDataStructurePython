def pair_sum(arr,k):

    if len(arr)<2:
        return

    # Sets for tracking
    seen = set()
    output = set()

    # For every number in array
    for num in arr:

        # Set target difference
        target = k-num
        print("Target now is " + str(target))

        # Add it to set if target hasn't been seen
        if target not in seen:
            print(seen)
            seen.add(num)
            print("After adding" + str(seen))

        else:
            # Add a tuple with the corresponding pair
            print("Now we are in else condition and santosh is stupid.")
            output.add( (min(num,target),  max(num,target)) )


    # # FOR TESTING
    # return len(output)
    # Nice one-liner for printing output
    print('\n'.join(map(str,list(output))))


pair_sum([1,3,2,2], 4)