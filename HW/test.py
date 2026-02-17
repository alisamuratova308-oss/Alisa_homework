# #14.12.25
# #номер 1
# def add_score(scores, name, points):
#     if name in scores:
#         scores[name] += points
#     else:
#         scores[name] = points
# scores = {}
# while True:
#     u_input = input("Введите имя и очки (через пробел) или 'конец':")
#     if u_input.lower() == "конец":  
#         break
#     name, points = u_input.split()  
#     points = int(points)
#     add_score(scores, name, points) 
# print("Результаты:")  
# for name, points in scores.items():  
#     print(f"{name}: {points} очков") 
# max_points = max(scores.values())
# win = []
# for name, points in scores.items():
#     if points == max_points:
#         win.append(name)
#         print(win)

# #номер 2
# def text_pred():
#     text = input("Введите текст: ")
#     text = text.lower()
#     text = text.strip('.,!?;:')
#     text2 = ''
#     for i in text:
#         if i != ",":
#             text2 += i

#     print(text2)
#     words = text2.split()
#     un_words = set(words)
#     print(f"Всего уникальных слов: {len(un_words)}")
#     print("Уникальные слова в тексте:")
#     for words in un_words:
#         print(words,end = ' ')
# text_pred()

# #номер 3 н
# contact = {}
# def add_contact(name, phone):
#    contact[name] = phone
#    print(f"Контакт {name} добавлен.")
# def find_contact(contacts,name): 
#    if name in contacts:  
#        print(contacts[name])  
#    else:  
#        print("Контакт не найден.")
# def find_contact_phone(contact,phone):
#     input_phone = contact.values()
#     phone_p = []
#     for i in input_phone:
#         for name, phone in contact.items():
#             if i == phone:
#                 phone_p.append(name)
#     print(f"Найдено имя: {phone_p}")
                
        

# while True:  
#     command = input("Введите команду: ").strip().lower()  
      
#     if command == "добавить":  
#         name = input("Введите имя: ").strip()  
#         phone = input("Введите телефон: ").strip()  
#         add_contact(name, phone)  
          
#     elif command == "найти по имени":  
#         name = input("Введите имя для поиска: ").strip()  
#         find_contact(contact,name)  
#     elif command == "найти по телефону":  
#         phone = input("Введите телефон для поиска: ").strip()  
#         find_contact_phone(contact,phone)
          
#     elif command == "выход":    
#         break  
          
#     else:  
#         print("Неизвестная команда.")  
    

# #номер 4 н

# def  count_even_odd(number):
#     word = 0
#     words = 0
#     for numbers in number:
#         if numbers % 2 == 0:
#             word += 1
#         else:
#             words += 1
#     print(f"Четных чисел: {word}, нечетных: {words}")
# def sum_positive_negative(number):
#     num = 0
#     num2 = 0
#     for i in number:
#         if i >0:
#             num += i
#         else:
#             num2 += i
#     print(f"Сумма положительных: {num}, сумма отрицательных: {num2}")
# def find_max_min(number):
#     max_numbers = max(number)
#     min_numbers = min(number)
#     print(f"Максимальное: {max_numbers}, минимальное:{min_numbers}")
# number  = []
# while True:
#     u_input = input("Введите число (или стоп): ")
#     if u_input == "стоп":
#         break
#     numbers = int(u_input)
#     number.append(numbers)
# count_even_odd(number)
# sum_positive_negative(number)
# find_max_min(number)



# #номер 5 
# def shift_char(text, shift): 
#     for i in range(text_len):
#         code = ord(text[i])
#         if 97 <= code <= 122:
#             print(chr((code - 97 + shift) % 26 + 97),end="")
#         elif 65 <= code <= 90:    
#             print(chr((code - 65 + shift) % 26 + 65),end="") 
#         elif 1072 <= code <= 1103:
#             print(chr((code - 1072 + shift) % 32 + 1072),end="")
#         elif 1040 <= code <= 1071:  
#             print(chr((code - 1040 + shift) % 32 + 1040),end="")
    
# text = input("Введите текст: ")
# text_len = len(text)
# shift = int(input("Введите сдвиг:")) 
# shift_char(text, shift)



#номер 6 
import random
wariant = ["камень","ножницы","бумага"]
win = 0
los = 0
draw = 0
def get_computer_choice():
    return random.choice(wariant)
def determine_winner(user, comp, draw, los, win):
    if user == comp:
        draw += 1
        
        return "ничья"
    elif (user == "камень" and comp == "ножници") or (user == "ножницы" and comp == "бумага") or (user == "бумага" and comp == "камень"):
        win += 1
        
        return "победа"
    else:
        los += 1
        
        return "поражение"
while True:
    user = input("Выберите вариант (камень/ножницы/бумага/стоп): ")
    comp = get_computer_choice()
    print(f"Вы выбрали: {user}")  
    print(f"Компьютер выбрал: {comp}")
    rel = determine_winner(user,comp, draw, los, win)
    print(f"Результат: {rel}")
    if user == "стоп":
        print(f"побед {win}, поражений {los}, ничьих {draw}")
