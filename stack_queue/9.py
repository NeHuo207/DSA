class Stack:
    def __init__(self):
        self.arr = []
        self.top = -1

    def push(self, x):
        self.top += 1
        if self.top == len(self.arr):
            self.arr.append(x)
        else:
            self.arr[self.top] = x

    def pop(self):
        if self.isEmpty():
            raise Exception("Underflow")
        x = self.arr[self.top]
        self.top -= 1
        return x

    def top_val(self):
        if self.isEmpty():
            raise Exception("Stack Empty")
        return self.arr[self.top]

    def isEmpty(self):
        return self.top == -1


def infix_to_postfix(expr):
    prec = {"+": 1, "-": 1, "*": 2, "/": 2}
    output = []
    opStack = Stack()
    for token in expr.split():
        if token.isdigit():
            output.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            while opStack.top_val() != "(":
                output.append(opStack.pop())
            opStack.pop()
        else:
            while (
                not opStack.isEmpty()
                and opStack.top_val() != "("
                and prec[opStack.top_val()] >= prec[token]
            ):
                output.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        output.append(opStack.pop())
    return output


expr = "2 + 3 * 4"

print(infix_to_postfix(expr))
