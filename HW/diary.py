class Diary:
    def __init__(self): 
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject not in self.grades:  
            self.grades[subject] = []  
        self.grades[subject].append(grade) 
        return f"{subject}, {grade}"
    def get_average(self, subject):
        return sum(self.grades[subject]) / len(self.grades[subject])
    def get_all_average(self):
        oll_grades = self.grades.values()
        return sum(oll_grades)/len(oll_grades)
    def get_bad_subjects(self):
        
test = Diary()
while True:
    u_input = input("Введите 1) добавить оценку 2)Средний бал 3)средний балл по всем предметам или 'выход' : ")
    if u_input == "выход":
        break
    elif u_input == "1":
        subject = input("Введите предмет: ")
        grade =float( input("Введите оценку: ")) 
        print(test.add_grade(subject, grade)) 
    elif u_input == "2":
        subject = input("Введите предмет: ")
        print(test.get_average(subject))
    elif u_input == "3":
        print(test.get_average())



