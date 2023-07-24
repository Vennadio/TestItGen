#Предметы ученика
def subjects_for_student(student_name, class_data):
    for name, subjects in class_data.items():
        if name == student_name:
            return subjects
    return []
#Ученики и их предметы
def students_for_subject(subject, class_data):
    students = []
    for name, subjects in class_data.items():
        if subject in subjects:
            students.append(name)
    return students
#Метод показывающий всех учеников и его изучаемые предметы
def show_all(class_data):
    sorted_data = sorted(class_data.items(), key=lambda x: x[0], reverse=True)
    for name, subjects in sorted_data:
        print(f"Ученик {name} изучает предметы: {', '.join(subjects)}")

def main():
    num_students = int(input("Введите количество учеников в классе: "))
    class_data = {}  # Словарь для хранения данных об учениках и их предметах

    # Запрашиваем данные для каждого ученика
    for i in range(num_students):
        name = input("Введите имя ученика: ")
        subjects = input("Введите предметы, которые он изучает (через пробел): ").split()
        class_data[name] = subjects

    while True:
        print("\nМеню:")
        print("1. Показать данные обо всех учениках и их предметах")
        print("2. Показать предметы ученика по его имени")
        print("3. Показать учеников, изучающих определенный предмет")
        print("4. Выйти из программы")

        choice = input("Введите номер пункта меню: ")

        if choice == "1":
            show_all(class_data)
        elif choice == "2":
            student_name = input("Введите имя ученика, чтобы узнать его предметы: ")
            student_subjects = subjects_for_student(student_name, class_data)
            print(f"Ученик {student_name} изучает предметы: {', '.join(student_subjects)}")
        elif choice == "3":
            subject = input("Введите предмет, чтобы узнать учеников, которые его изучают: ")
            subject_students = students_for_subject(subject, class_data)
            print(f"Ученики, изучающие предмет {subject}: {', '.join(subject_students)}")
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите пункт из меню.")

if __name__ == "__main__":
    main()
