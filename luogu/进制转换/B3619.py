def decimal_to_x(n: int, x: int) -> str:
    if n == 0:
        return "0"
    ans = []
    while n:
        rem = n % x
        if rem < 10:
            ans.append(str(rem))
        else:
            ans.append(chr(rem - 10 + ord('A')))
        n //= x
    return "".join(reversed(ans))

if __name__ == "__main__":
    n = int(input())
    x = int(input())

    print(decimal_to_x(n,x))