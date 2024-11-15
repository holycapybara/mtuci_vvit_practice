from math import sqrt

#task 1

def greet(name):
    print(f'Greetings, {name}')


def square(number):
    return number * number


def max_of_two(x, y):
    return x if x > y else y

#task 2

def describe_person(name, age=30):
    print(f'Person name: {name.strip()}\n'
          f'Age: {str(age).strip()}')

#task 3

def is_prime(n):
    if n == 1 or not n % 2 and n != 2 or n < 0:
        return False
    for i in range(3, int(sqrt(n)), 2):
        if not n % i:
            return False
    return True


if __name__ == '__main__':
    print(is_prime(int(input())))