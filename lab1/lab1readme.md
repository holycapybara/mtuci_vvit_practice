# Лабраторная работа 1
## Задача 1
> Напишите программу, которая запрашивает у пользователя ввод числа и выводит на экран все числа от 1 до введенного числа включительно.  
```python
n = int(input("Enter number: "))
for i in range(n):
    print(i+1)
```
Запрашиваем ввод числа с помощью функции `input()`, с помощью функции `int()` приводим ее к целочисленному типу и записываем в переменную с именем n. Далее применяем цикл `for` и печатаем значение перменной-счетчика
i увеличенное на 1 каждую итерацию при помощи функции `print()`. Цикл работает по схеме `for(start, stop, step)`, `start` - начальное значение счетчика,
`stop` - конечное значенеие`step` - шаг счетчика на итерации. При подаче в качестве аргументов только одного значния оно применится к `stop`, 
для двух других будут использованы значения по умолчанию `start=0` и `step=1`. Именно из-за того что началом цикла является 0 мы печатаем увеличенное на 1 
значение счетчика.

## Задача 2
> Напишите программу, которая запрашивает у пользователя ввод 2 чисел и выводит на экран большее из них.  
```python
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print(f'Greater number: {max(a, b)}')
```
Запрашиваем два числа, записываем их в переменные a и b. Далее выводим наибольшее значние с помощью встроенной функции `max()`, возвращающей
наибольшее значение из двух или более аргументов.

