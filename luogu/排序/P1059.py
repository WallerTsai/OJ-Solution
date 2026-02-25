import sys

if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    res = sorted(set(map(int, input_data[1:])))
    
    print(len(res))
    print(*(res))

