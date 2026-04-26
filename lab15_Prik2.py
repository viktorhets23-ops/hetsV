class Teacher:
  
    
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

    def calculate_salary(self):
     
        base_rate = 10000
        experience_bonus = self.experience * 500
        return base_rate + experience_bonus

class CandidateTeacher(Teacher):
  
    
    def __init__(self, name, experience, degree):
        # Виклик конструктора батьківського класу
        super().__init__(name, experience)
        self.degree = degree

    def calculate_salary(self):
      
        standard_salary = super().calculate_salary()
        return standard_salary * 1.15


t1 = Teacher("Іван Петренко", 10)
t2 = CandidateTeacher("Олена Козак", 10, "Кандидат техн. наук")

print(f"\nВикладач: {t1.name}, Стаж: {t1.experience} років")
print(f"Зарплата: {t1.calculate_salary()} грн")

print(f"\nВикладач: {t2.name}, Стаж: {t2.experience} років, Ступінь: {t2.degree}")
print(f"Зарплата (з надбавкою 15%): {t2.calculate_salary():.2f} грн")