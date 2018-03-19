# Given two strings, check to see if they are anagrams. An anagram is when the two strings
#  can be written using the exact same letters (so you can just rearrange the letters to
# get a different phrase or word).
#
# For example:
#
# "public relations" is an anagram of "crap built on lies."
#
# "clint eastwood" is an anagram of "old west action"
#
# Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and
# "o d g".



# There are two ways to to do this program.

def anagram1(s1,s2):
    # We need to get rid of the empty spaces and
    # lower case the string

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Now we will return boolean for sorted match.
    return sorted(s1) == sorted(s2)
# let's see if it works.
print(anagram1('dog', 'god'))

# Second solution is longer but it is more optimal

def anagram2(s1, s2):
    # We will remove spaces and will lower case the string
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # We will do the edge case to check if both strings have same number of letters
    if len(s1) != len(s2):
        return False

    # will creat an empty dictionary.
    count = {}

    for letter in s1:
        if letter in count:
            # We are assigning value 1 for every letter in s1
            count[letter] += 1
        # if it is the start of loop u just want to assign one into it.
        else:
            count[letter] = 1

#     for s2 we will do the opposite.
    for letter in s2:
        if letter in count:
            # We are making every value of the letters from 1 to zero
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    # other wise just return true
    return True

print(anagram2('dog', 'god'))