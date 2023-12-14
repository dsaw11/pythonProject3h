import random

try:
    n = int(input())
    if n in range(4, 31):
        while n > 1:
            hod_user = n
            hod_computer = n
            while n - hod_user < 1:
                hod_user = input("Выберете какое количество камней вы хотите убрать (1 или 2 или 3)")
                if hod_user.isdigit():
                    hod_user = int(hod_user)
                if hod_user not in range(1, 4):
                    print("Введенные данные некорректны")
                    break
                if n - hod_user == 1:
                    n -= hod_user
                    print("Остался 1 камень,победа пользователя")
                    break
                if n - hod_user > 1:
                    n -= hod_user
                    print(f"Осталось {n} каммей")
                    while n - hod_computer < 1:
                        hod_computer = random.randint(1, 3)
                        if n - hod_computer == 1:
                            n -= hod_computer
                            print("Ход компьютера: ", hod_computer)
                            print("Остался 1 камень, победа компьютера")
                            break
                        if n - hod_computer > 1:
                            print('Ход компьтeра: ', hod_computer)
                            n -= hod_computer
                            print(f"Осталось {n} камней")
                            break
                if n==1:
                    break
                else:
                    print("Введенные данные не корректны")
                    break
    else:
        print("диапозон n от 4 до 30")
except ValueError:
    print("Введите число!")
