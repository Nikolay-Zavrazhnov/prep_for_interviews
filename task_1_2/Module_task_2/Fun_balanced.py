

def balanced_parenthesis(string_of_parenthesis, stack):

    open_parenthesis = ['[', '{', '(']
    close_parenthesis = [']', '}', ')']

    for prts in string_of_parenthesis:
        if prts in open_parenthesis:
            stack.push(prts)
        elif prts in close_parenthesis:
            id_ = close_parenthesis.index(prts)
            if stack.peek() == open_parenthesis[id_]:
                stack.pop()
            else:
                return 'UNBALACED'
    if stack.isEmpty() is False:
        return 'BALANСED'
    else:
        return 'UNBALANСED'
