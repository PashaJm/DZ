from dataclasses import dataclass, field
from typing import List
from datetime import date

@dataclass
class Subject:
    name: str                  # Название предмета
    exam_date: date            # Дата экзамена
    teacher_full_name: str     # ФИО преподавателя

@dataclass
class GradeBook:
    subjects: List[Subject] = field(default_factory=list)

@dataclass
class Student:
    first_name: str            # Имя
    last_name: str             # Фамилия
    birth_date: date           # Дата рождения
    grade_book: GradeBook      # Зачётка

    def full_name(self) -> str:
        return f"{self.last_name} {self.first_name}"

def find_youngest_and_oldest(students: List[Student]):
    if not students:
        print("Список студентов пуст.")
        return

    # Инициализируем первого студента как самого старшего и младшего
    oldest = youngest = students[0]

    for student in students[1:]:
        if student.birth_date < oldest.birth_date:
            oldest = student
        if student.birth_date > youngest.birth_date:
            youngest = student

    print("Самый старший студент:")
    print(f"ФИО: {oldest.full_name()}")
    print(f"Дата рождения: {oldest.birth_date.strftime('%d.%m.%Y')}\n")

    print("Самый младший студент:")
    print(f"ФИО: {youngest.full_name()}")
    print(f"Дата рождения: {youngest.birth_date.strftime('%d.%m.%Y')}")

def main():
    # Пример данных
    students = [
        Student(
            first_name="Иван",
            last_name="Иванов",
            birth_date=date(1995, 5, 24),
            grade_book=GradeBook(subjects=[
                Subject(name="Математика", exam_date=date(2023, 6, 15), teacher_full_name="Петр Петров"),
                Subject(name="Физика", exam_date=date(2023, 6, 20), teacher_full_name="Сидор Сидоров"),
                Subject(name="Химия", exam_date=date(2023, 6, 25), teacher_full_name="Анна Ананова")
            ])
        ),
        Student(
            first_name="Мария",
            last_name="Смирнова",
            birth_date=date(1998, 12, 3),
            grade_book=GradeBook(subjects=[
                Subject(name="Биология", exam_date=date(2023, 7, 10), teacher_full_name="Елена Еленева"),
                Subject(name="История", exam_date=date(2023, 7, 15), teacher_full_name="Дмитрий Дмитриев")
            ])
        ),
        Student(
            first_name="Алексей",
            last_name="Кузнецов",
            birth_date=date(1992, 3, 17),
            grade_book=GradeBook(subjects=[
                Subject(name="Информатика", exam_date=date(2023, 5, 30), teacher_full_name="Ольга Ольгина"),
                Subject(name="Литература", exam_date=date(2023, 6, 5), teacher_full_name="Николай Николайчев"),
                Subject(name="География", exam_date=date(2023, 6, 10), teacher_full_name="Татьяна Татьянова"),
                Subject(name="Физкультура", exam_date=date(2023, 6, 12), teacher_full_name="Сергей Сергеев")
            ])
        ),
        Student(
            first_name="Екатерина",
            last_name="Лебедева",
            birth_date=date(2000, 8, 30),
            grade_book=GradeBook(subjects=[
                Subject(name="Музыка", exam_date=date(2023, 7, 20), teacher_full_name="Виктор Викторов"),
                Subject(name="Изобразительное искусство", exam_date=date(2023, 7, 25), teacher_full_name="Людмила Людмилова"),
                Subject(name="Театральное искусство", exam_date=date(2023, 7, 28), teacher_full_name="Галина Галинина")
            ])
        )
    ]

    find_youngest_and_oldest(students)

if __name__ == "__main__":
    main()