#Лабораторная работа 3
## Задание 1 - Открытие и чтение файла
> 1.	Создайте текстовый файл **example.txt** и заполните его несколькими строками текста.
> 2.	Напишите функцию на Python, которая открывает файл **example.txt** в режиме чтения и выводит его содержимое на экран.
> 3.	Используйте разные методы чтения файла: чтение всего файла сразу, построчное чтение, реализуйте выбор типа чтения в принимаемых аргументах функции.
```python
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
```
Первым делом проверяем корректность указания парамтера чтения по строкам или целиком, если он задан некорректно - вызываем исключение.
Открываем файл при помощи конструкции `with open()` с указанием имени файла и режима открытия. В данном случае `'r'` означает открытие в режиме чтения.
Благодаря этой конструкции файл автоматически закроется при завершении программы.
Если файла не сущетвует - "ловим" ошибку `FileNotFoundError` и выводим сообщение на экран. 

##Задание 2 - Запись в файл
> 1.	Напишите программу, которая запрашивает у пользователя текст и записывает его в новый файл **user_input.txt**.
> 2.	Реализуйте функционал добавления текста в существующий файл, не удаляя его предыдущее содержимое.
```python
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
```
При входе в функцию создаем файл в данной папке с указанным именем. Для этого используем функцию `os.path()` из модуля os. Предварительно ее 
нужно импортировать с помощью команды `import os.path`. 
Далее задаем пользователю вопрос о режиме открытия файла - запись с очищением или дозапись. Получив корректиный ответ, открываем файл в нужном 
режиме ("w" и "а" соответсвенно).
