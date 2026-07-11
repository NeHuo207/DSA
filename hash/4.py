def common_elements(a, b):
    set_a = set(a)
    return {x for x in b if x in set_a}


if __name__ == "__main__":
    print(common_elements([1, 2, 3], [2, 3, 4]))
    print(common_elements([1, 2], [3, 4]))
