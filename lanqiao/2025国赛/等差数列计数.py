def main():
    n = 2025
    odd = (n + 1) // 2
    even = n // 2
    ans = odd * (odd - 1) + even * (even - 1)
    print(ans)

if __name__ == "__main__":
    main()