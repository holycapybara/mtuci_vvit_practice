from lab3 import lab3


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

#task 1
        if task == 1:
            filename = input(f"Enter a name of the file (empty for default - 'example.txt'):\n")
            if not filename:
                filename = "lab3/user_input.txt"


            mode = input(f"Choose to read the entire file or line by line?\n"
                         f"(A) - Read the entire file\n"
                         f"(B) - Read the file line be line\n")

            while mode not in {"A", "B"}:
                mode = input("Invalid input. Please enter a correct option:\n"
                             f"(A) - Read the entire file\n"
                             f"(B) - Read the file line be line\n")

            mode = ["FULL", "LINES"][["A", "B"].index(mode)]
            lab3.read_print_file(filename, mode)


        if task == 2:
            filename = input(f"Enter a name of the file:\n")
            content = input(f"Enter file content:\n")
            lab3.write_to_file(filename, content)

            print()
        if task == 3:
            break



if __name__ == "__main__":
    main()