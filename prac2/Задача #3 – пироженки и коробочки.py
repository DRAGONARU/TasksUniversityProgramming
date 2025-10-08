def print_pack_report(pack):
    for i in range(pack, 0, -1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} - расфасуем по 3 или по 5")
        elif i % 3 == 0:
            print(f"{i} - расфасуем по 3")
        elif i % 5 == 0:
            print(f"{i} - расфасуем по 5")
        else:
            print(f"{i} - не заказываем!")
print_pack_report(int(input()))
