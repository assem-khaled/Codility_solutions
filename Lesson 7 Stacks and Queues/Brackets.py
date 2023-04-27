def solution(S):
    stack = []
    match = {']' : '[', ')' : '(', '}' : '{'}

    for i in S:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        elif i == ')' or i == ']' or i == '}':
            if len(stack) < 1:
                return 0
            if match[i] != stack.pop():
                return 0

    return 1 if len(stack) == 0 else 0