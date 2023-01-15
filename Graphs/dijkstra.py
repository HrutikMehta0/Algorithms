import operator
def evalRPN(tokens):
    notations = {'+': operator.add,
                 '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    st = []
    for i, j in enumerate(tokens):
        if j not in notations:
            st.append(int(j))
        else:
            right = st.pop()
            left = st.pop()
            st.append(int(notations[j](left, right)))

    return st.pop()


print(evalRPN(["5", "4", "+", "3", "2", "*", "8", "4", "/", "-", "+"]))
