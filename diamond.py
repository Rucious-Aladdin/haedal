row = int(input("다이아몬드 크기: "))

for num1 in range(1, row * 2, 2):
    print((" " * ((row * 2 - 1 - num1) // 2)) + ("*" * num1))

for num2 in range(row * 2 - 3, 0, -2):
    print((" " * ((row * 2 - 1 - num2) // 2)) + "*" * num2)