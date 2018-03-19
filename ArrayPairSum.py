# Array Pair Sum
# Problem
# Given an integer array, output all the unique pairs that sum up to a specific value k.
#
# So the input:
#
# pair_sum([1,3,2,2],4)
#
# would return 2 pairs:
#
# (1,3)
# (2,2)
#
# NOTE: FOR TESTING PURPOSES< CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS

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

        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)

        else:
            # Add a tuple with the corresponding pair
            output.add( (min(num,target),  max(num,target)) )
    # FOR TESTING
    # return len(output)
    # Nice one-liner for printing output
    print('\n'.join(map(str,list(output))))




pair_sum([6,2,5,4,5,8],10)