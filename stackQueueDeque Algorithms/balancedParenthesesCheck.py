# Problem Statement
# Given a string of opening and closing parentheses, check whether it’s balanced.
#  We have 3 types of parentheses: round brackets: (), square brackets: [], and
# curly brackets: {}. Assume that the string doesn’t contain any other character
#  than these, no spaces words or numbers. As a reminder, balanced parentheses
# require every opening parenthesis to be closed in the reverse order opened.
# For example ‘([])’ is balanced but ‘([)]’ is not.
#
# You can assume the input string has no spaces.

def BalanceParenCheck(s):
    # Let's do the edge case check if the numbers of chars are even numbers
    # If it is not we know that it is not balance Parentheses.

    if len(s)%2 != 0:
        return False

    # We will make a set of opening parenthesis
    opening = set('([{')
    # We will make a set of tulips of what our parenthesis should look like.
    matches = set( [ ('(',')'), ('[',']'), ('{','}') ] )

    # We will use Stack data structures to solve our problem.
    # list in python work as stacks we are not implementing stack here and just using lists
    stack = []

    for parenth in s:
        # We find out if the characters is one of opening parenthesis.
        if parenth in opening:
            stack.append(parenth)
        # If it is the opening parenthesis it will be added to the stack.
        # Other wise we will see if stack is empty, cause if it is empty then
        # it means that there is no opening parenthesis.
        else:
            if len(stack) == 0:
                return False

            # Now we will see the last appended Opening parenthesis and compare it with
            # the current parenthesis and see if it matches.
            last_open = stack.pop()
            # Now let's compare it will the current parenthesis and see if it makes a set
            # in matches.
            if (last_open, parenth) not in matches:
                return False
    return len(stack) == 0





