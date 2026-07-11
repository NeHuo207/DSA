def is_balanced(s):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack.pop() != pairs[ch]:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    print(is_balanced("([]{})"))
    print(is_balanced("([)]"))
    print(is_balanced("((("))
    print(is_balanced(""))
