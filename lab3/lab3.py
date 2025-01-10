import os.path

#Task 1

def read_print_file(input_file, mode) -> None:
    """
    Reads the file and prints its content. Can read the entire file or line by line.

    :param str input_file: Name of the file to read and print
    :param str mode: Reading the entire file or line by line

    :raises ValueError: if the mode is not "full" or "lines"
    :return: None
    """
    mode_list = {"FULL", "LINES"}

    if mode not in mode_list:
        raise ValueError(f'print_file: mode must be on of {mode_list}, got "{mode}" instead')
    try:
        with open(input_file, 'r') as In:
            if mode=="FULL":
                content = In.read()
                print(content)
            else:
                content = [line[:-1] for line in In]
                print(*content, sep="\n")
    except FileNotFoundError:
        print(f"The file you trying to read doesn't exist. Please enter a correct file name.\n\n")
        return


def task_1() -> None:
    """Reads file 'example.txt' and prints it content."""
    read_print_file("exaple.txt", "LINES")


#Task 2

def write_to_file(filename, content):
    """
    Creates a file and writes content to it. If file already exists, asks if you want to update it


    :param filename: name of the file
    :param content: content written to the file

    :return: None
    """

    path = ("./" + filename)
    mode = "A"
    if os.path.isfile(path):
        mode = input(f'{filename} already exists. Would you like to recreate or update it?\n'
                     f'(A) - Recreate\n'
                     f'(B) - Update\n')


    while mode not in {"A", "B"}:
        mode = input(f'Invalid input. Please select a correct option.\n'
                     f'(A) - Recreate\n'
                     f'(B) - Update\n')



    with open(filename, ["w", "a"][["A", "B"].index(mode)]) as In:
        In.write(content)


def task_2() -> None:
    """Requests text and prints it to 'user_input.txt'"""
    write_to_file("user_input.txt", input("Enter text to be printed to 'user_input.txt':\n"))


if __name__ == "__main__":
    task_1()
