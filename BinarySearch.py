def main():
    a = [1,2,3,4,5,6,7,8]
    number = 2
    binary_search(a, number)

def binary_search(n, number):
    low = 0
    high = len(n)
    while low < high:
        m = (low + high)//2
        v = n[m]
        if v == number:
            print(m)
            return True
        elif v > number:
            high = m
        else:
            low = m + 1



if __name__ == "__main__":
    main()