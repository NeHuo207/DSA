GOLDEN_RATIO = 0.6180339887498949


def hash_multiplication(k, m, A=GOLDEN_RATIO):
    frac = (k * A) % 1
    return int(m * frac)


def hash_division(k, m):
    return k % m


if __name__ == "__main__":
    m = 16
    print(f"{'k':>6} {'chia':>6} {'nhan':>6}")
    for k in [1, 2, 3, 4, 100, 12345]:
        print(f"{k:>6} {hash_division(k, m):>6} {hash_multiplication(k, m):>6}")

    keys = [i * 4 for i in range(100)]

    b_div = [0] * m
    b_mul = [0] * m
    for k in keys:
        b_div[hash_division(k, m)] += 1
        b_mul[hash_multiplication(k, m)] += 1

    print(f"\nkhoa boi cua 4, m=16:")
    print(f"chia: {b_div}")
    print(f"nhan: {b_mul}")
