def task1_1():
    n = int(input("Enter number: "))
    for i in range(n):
        print(i+1)


def task1_2():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    print(f'Greater number: {max(a, b)}')


if __name__ == "__main__":
    task1_1()
