import math
import datetime
import my_module
import animolz as zveri


def calculate_square_root():
    print(math.sqrt(float(input(f'Enter a number to calculate square root:\n'))))

def get_current_date_and_time():
    print(f'Current date: {datetime.datetime.today()}\n'
          f'Current time: {datetime.datetime.now()}')

def get_sum_of_two():
    print(my_module.sum_of_two(int(input("Enter first number:")), int(input("Enter second number:"))))



if __name__ == "__main__":
    zveri.goat.attack()