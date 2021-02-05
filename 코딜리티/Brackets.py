def solution(S):
    stack = []
    if len(S) == 0:
        return 1

    for s in S:
        if len(stack) == 0:
            stack.append(s)

        else:
            if s == "}" and stack[-1] == "{":
                stack.pop()
            elif s == ")" and stack[-1] == "(":
                stack.pop()

            elif s == "]" and stack[-1] == "[":
                stack.pop()

            else:
                stack.append(s)

    if len(stack) == 0:
        return 1

    else:
        return 0
