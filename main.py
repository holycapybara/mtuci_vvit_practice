import lab1
import lab2
import lab3


def main():
    while True:
        task = input(f'Select a task:\n'
                         f'(1) - Reading a file\n'
                         f'(2) - Writing to a file\n'
                         f'(3) - Exit\n')
        if task not in {"1", "2", "3"}:
            print("Please enter a correct option")
            continue
        task = int(task)
        if task == 1:
            lab3.task_1()
            print()
        if task == 2:
            lab3.task_2()
        if task == 3:
            break



if __name__ == "__main__":
    main()