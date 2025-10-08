import random
def password_generator():
    special_symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]
    upper_case = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                   "U", "V", "W", "X", "Y", "Z"]
    lower_case = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print("Приветствует мастер создания паролей!")
    while True:
        print("Желаете создать пароль?")
        choose = input("Введите да или нет: ")
        if choose == "да":
            print("Пришла пора выставить параметры пароля")
            lower_case_choise = input("Нужны ли в пароле строчные буквы? (да/нет): ")
            upper_case_choise = input("Нужны ли в пароле прописные буквы? (да/нет): ")
            spec_symbols_choise = input("Нужны ли в пароле специальные символы? (да/нет): ")
            number_choise = input("Нужны ли в пароле цифры? (да/нет): ")
            len_password = int(input("Какой длины должен быть пароль? :  "))
            used_to_generate = []
            if lower_case_choise == "да":
                for i in lower_case:
                    used_to_generate.append(i)
            if upper_case_choise == "да":
                for i in upper_case:
                    used_to_generate.append(i)
            if spec_symbols_choise == "да":
                for i in special_symbols:
                    used_to_generate.append(i)
            if number_choise == "да":
                for i in number:
                    used_to_generate.append(i)
            if len(used_to_generate) != 0:
                password = ""
                for i in range(len_password):
                    password += random.choice(used_to_generate)
                print("Вот ваш пароль:")
                print(password)
        else:
            print("До свидания!")
            return 0
password_generator()
