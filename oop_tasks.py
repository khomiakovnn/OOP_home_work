class Student:
    '''Student's class'''

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lecturer(self, lecturer, course, grade):
        '''Rate lecturer'''
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        '''Мodifies the magic method for 'print' '''
        res = (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self.avg_grade()}\n'
            f'Курсы в процессе изучения: {self.format_list(self.courses_in_progress)}\n'
            f'Завершенные курсы: {self.format_list(self.finished_courses)}\n'
        )
        return res
    
    def __lt__(self, other):
        '''Modifies the magic method of comparing students by average grade'''
        if not isinstance(other, Student):
            print(f'{other.surname} не студент!')
            return        
        if self.avg_grade() != "Оценки отсутствуют" and other.avg_grade() != "Оценки отсутствуют":
            print(self.avg_grade() < other.avg_grade()) # Method demonstration
            return self.avg_grade() < other.avg_grade()
            print()
        if self.avg_grade() == "Оценки отсутствуют" or other.avg_grade() == "Оценки отсутствуют":
            print("Невозможно сравнить экземляры:")
        if self.avg_grade() == "Оценки отсутствуют":
            print(f"{self} не имеет оценок")
        if other.avg_grad == "Оценки отсутствуют":
            print(f"{other} не имеет оценок")
        print()
        return
    
    def avg_grade(self):
        """Average grade"""
        sum_grades, num_grades = 0, 0
        for cours in self.grades.values():
            sum_grades += sum(cours)
            num_grades += len(cours)
        if num_grades == 0:
            res = "Оценки отсутствуют"
        else:
            res = sum_grades / num_grades
        return res
    
    def format_list(self, courses):
        """Format list of courses for print"""
        res = str()
        for cours in courses:
            res += cours + ", "
        res = res[:-2]
        return res

class Mentor:
    '''Mentor's parent class'''

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    '''Lecturer's class'''

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def __str__(self):
        res = (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {self.avg_grade()}\n'
        )
        return res
    
    def __lt__(self, other):
        '''Modifies the magic method of comparing lecturers by average grade'''
        if not isinstance(other, Lecturer):
            print(f'{other.surname} не читает лекции!')
            return        
        if self.avg_grade() != "Оценки отсутствуют" and other.avg_grade() != "Оценки отсутствуют":
            print(self.avg_grade() < other.avg_grade()) # Method demonstration
            return self.avg_grade() < other.avg_grade()
        if self.avg_grade() == "Оценки отсутствуют" or other.avg_grade() == "Оценки отсутствуют":
            print("Невозможно сравнить экземляры:")
        if self.avg_grade() == "Оценки отсутствуют":
            print(f"{self} не имеет оценок")
        if other.avg_grade() == "Оценки отсутствуют":
            print(f"{other} не имеет оценок")
        return
    
    def avg_grade(self):
        """Average grade"""
        sum_grades, num_grades = 0, 0
        for cours in self.grades.values():
            sum_grades += sum(cours)
            num_grades += len(cours)
        if num_grades == 0:
            res = "Оценки отсутствуют"
        else:
            res = sum_grades / num_grades
        return res

class Reviewer(Mentor):
    '''Reviewer's class'''

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        res = (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
        )
        return res


def avg_grade_hw_course(students, course):
    """Calculate average grade for student's homework in course"""
    
    res_sum = 0
    res_count = 0
    for student in students:
        for hw_cource in student.grades:
            if hw_cource == course:
                res_sum += (sum(student.grades[hw_cource]))
                res_count += (len(student.grades[hw_cource]))
    return res_sum / res_count

def avg_grade_lecturer_course(lecturers, course): # Скопировать из студента
    """Calculate average grade for lecturers in course"""
    
    res_sum = 0
    res_count = 0
    for lecturer in lecturers:
        for lc_cource in lecturer.grades:
            if lc_cource == course:
                res_sum += (sum(lecturer.grades[lc_cource]))
                res_count += (len(lecturer.grades[lc_cource]))
    return res_sum / res_count


if __name__ == '__main__':
    
    # Lists for average rate calculation
    students = []
    lecturers = []
    
    # Create instances-----------------------------------------
    # Students
    best_student = Student('Ruoy', 'Eman', 'male')
    best_student.courses_in_progress += ['Python', 'SQL']
    best_student.finished_courses += ['Git', 'Introduction']
    best_student.grades['Git'] = [10,8] # Курс завершен. Оценки задним числом не выставить методом
    best_student.grades['Introduction'] = [10,10] # Курс завершен. Оценки задним числом не выставить методом
    students.append(best_student)

    worst_student = Student('Emma', 'Leman', 'female')
    worst_student.courses_in_progress += ['Git', 'SQL']
    worst_student.finished_courses += ['Python', 'Introduction']
    worst_student.grades['Python'] = [8,6] # Курс завершен. Оценки задним числом не выставить методом
    worst_student.grades['Introduction'] = [10,10] # Курс завершен. Оценки задним числом не выставить методом
    students.append(worst_student)

    # Reviewers
    cool_reviewer = Reviewer('Some', 'Buddy')
    cool_reviewer.courses_attached += ['Python', 'SQL']

    hot_reviewer = Reviewer('John', 'Doe')
    hot_reviewer.courses_attached += ['Git', 'Introduction']

    # Lecturers
    cool_lecturer = Lecturer('Aulo', 'Agerio')
    cool_lecturer.courses_attached += ['Python', 'Introduction']
    lecturers.append(cool_lecturer)

    hot_lecturer = Lecturer('Numerius', 'Negidius')
    hot_lecturer.courses_attached += ['Git', 'SQL']
    hot_lecturer.grades['SQL'] = [9,7] # Текущие экземпляры студентов не могут сами оценивать курс SQL
    lecturers.append(hot_lecturer)
    # ----------------------------------------------------------

    # Function's and method's tests
    # Rate lecturers
    best_student.rate_lecturer(hot_lecturer, 'Git', 10)
    best_student.rate_lecturer(hot_lecturer, 'Git', 6)
    worst_student.rate_lecturer(cool_lecturer, 'Python', 10)
    worst_student.rate_lecturer(cool_lecturer, 'Python', 10)
    worst_student.rate_lecturer(cool_lecturer, 'Introduction', 8)
    best_student.rate_lecturer(cool_lecturer, 'Introduction', 10)

    # Rate students
    cool_reviewer.rate_hw(best_student, 'Python', 10)
    cool_reviewer.rate_hw(best_student, 'Python', 8)
    cool_reviewer.rate_hw(best_student, 'SQL', 9)
    cool_reviewer.rate_hw(best_student, 'SQL', 7)
    hot_reviewer.rate_hw(worst_student, 'Git', 8)
    hot_reviewer.rate_hw(worst_student, 'Git', 8)
    cool_reviewer.rate_hw(worst_student, 'SQL', 5)
    cool_reviewer.rate_hw(worst_student, 'SQL', 7)

    # Average rate of student's and lecturer's grades by course
    print(f'Средняя оценка студентов по курсу Git: {avg_grade_hw_course(students, "Git")}')
    print(f'Средняя оценка студентов по курсу Python: {avg_grade_lecturer_course(lecturers, "Python")}\n')

    # Print instances (modified '__str__')
    print('Представления экземпляров классов:\n')
    print(best_student)
    print(worst_student)
    print(cool_reviewer)
    print(hot_reviewer)
    print(cool_lecturer)
    print(hot_lecturer)

    # Compare instances (modified '__lt__')
    print("Сравнение экземпляров:\n")
    worst_student < best_student
    worst_student < cool_lecturer
    hot_lecturer < worst_student
    hot_lecturer < cool_lecturer