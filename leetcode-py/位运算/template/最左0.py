def f(num: int):
    res = ((num + 1) & ~num)
    return res

if __name__ == "__main__":
    x = 11 # 0b1011
    res = f(x)
    print(res)  # 4 0b100