class Diary:
    def __init__(self): 
        self.__grades = {}

    def add_grade(self, subject, grade):
        if subject not in self.__grades:  
            self.__grades[subject] = []  
        self.__grades[subject].append(grade) 
        return f"{subject}, {grade}"
    def get_average(self, subject):
        return sum(self.__grades[subject]) / len(self.__grades[subject])
    def get_all_average(self):
        print(self.__grades)
        oll_grades = self.__grades.values()
        print(oll_grades)
        return sum(oll_grades)/len(oll_grades)
    def get_bad_subjects(self):
        bad_subjects = []
        for subject, grades in self.__grades.items():
            if (sum(grades) / len(grades)) < 3.5:
                bad_subjects.append(subject)
        return bad_subjects
    def reset_diary(self):
        self.__grades = {}
        return "Оценки очищены "
        
test = Diary()
while True:
    u_input = input("Введите 1) добавить оценку 2)Средний бал 3)средний балл по всем предметам 4)список предметов, где средний балл ниже 3.5 5)очищает весь дневник или 'выход' : ")
    if u_input == "выход":
        break
    elif u_input == "1":
        subject = input("Введите предмет: ")
        grade =float( input("Введите оценку: ")) 
        if subject != '':
            if 2<=grade<=5 and grade != "":
                 print(test.add_grade(subject, grade)) 
        else:
            print("Неверный ввод")
    elif u_input == "2":
        subject = input("Введите предмет: ")
        if subject != '':
            print(test.get_average(subject))
        else:
            print("Неверный ввод")
    elif u_input == "3":
        print(test.get_all_average())
    elif u_input == "4":
        print(test.get_bad_subjects())
    elif u_input == "5":
        print(test.reset_diary())
# my_diary = Diary()
# my_diary.add_grade("Биология", 5)
# my_diary.add_grade("Биология", 5)
# my_diary.add_grade("Биология", 5)
# my_diary.add_grade("Химия", 2)
# my_diary.add_grade("Химия", 3)
# print(my_diary.get_average("Биология"))
# print(my_diary.get_average("Химия"))
# print(my_diary.get_all_average())
# print(my_diary.get_bad_subjects())1
# my_diary.reset_diary()



