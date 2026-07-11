def eval_rpn(tokens):
    stack = []

    for tok in tokens:
        if tok in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if tok == "+":
                stack.append(a + b)
            elif tok == "-":
                stack.append(a - b)
            elif tok == "*":
                stack.append(a * b)
            elif tok == "/":
                stack.append(int(a / b))
        else:
            stack.append(int(tok))

    return stack.pop()


if __name__ == "__main__":
    print(eval_rpn(["3", "4", "+", "2", "*"]))
    print(eval_rpn(["2", "3", "4", "*", "+"]))
    print(eval_rpn(["5", "1", "2", "+", "4", "*", "+", "3", "-"]))
