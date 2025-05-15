'''
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:
- Every open bracket is closed by the same type of close bracket.
- Open brackets are closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.

'''

def isValid(s):
    validParantheses = { ')': '(', '}' : '{', ']' : '[' }

    stack = []

    for parantheses in s:
        if parantheses in validParantheses:
            if len(stack) < 1:
                return False
            
            if validParantheses[parantheses] == stack[-1]:
                stack.pop()

            else:
                return False
        else:
            stack.append(parantheses)

    return len(stack) == 0
