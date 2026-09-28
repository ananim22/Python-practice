from datetime import datetime

# Функція виводить всі записи словника
def print_all(student_dict):
    if not student_dict:
        print("Словник пуст!")
        return
    
    print("\n--- Список всіх студентів ---")
    for full_name in student_dict.keys():
        year, month, day = student_dict[full_name]
        print(f"{full_name} | Дата народження: {day:02d}.{month:02d}.{year}")

# Функція добавляє новий запис
def add_record(students_dict):
    try:
        print("--- Введіть данні для нового учня ---")

        last_name = input("Прізвище: ")
        first_name = input("Ім'я: ")
        patronymic = input("По батькові: ")
        full_name = f"{last_name} {first_name} {patronymic}"

        if full_name in students_dict:
            print("Помилка: Учень з таким ПІБ вже існує!")
            return
            
        year = int(input("Рік народження: "))
        month = int(input("Місяць народження (1-12): "))
        day = int(input("День народження (1-31): "))

        datetime(year, month, day)
        students_dict[full_name] = (year, month, day)
        print("Запис успішно додано!")
    except ValueError:
        print("Помилка вводу! Переконайтеся, що ви вводите правильно ПІБ та дату.")

# Видаляє обраний запис
def delete_record(student_dict):
    if not student_dict:
        print("Словник пуст!")
        return
    
    try:
        full_name = input("Введіть ПІБ для видалення: ")
        del student_dict[full_name]
        print("Запис успішно видалений")
    except KeyError:
        print("Помилка! Запис із таким ПІБ не знайдено")

# Виводить всі записи які відсортовані за ключем
def print_sorted(student_dict):
    if not student_dict:
        print("Словник пуст!")
        return
    
    print("\n--- Відсортований список всіх студентів ---")
    for full_name in sorted(student_dict.keys()):
        year, month, day = student_dict[full_name]
        print(f"{full_name} | Дата народження: {day:02d}.{month:02d}.{year}")

# Перевіряє у кого сьогодні день народження
def check_birthdays(student_dict):
    if not student_dict:
        print("Словник пуст!")
        return
    
    today = datetime.today()
    birthday_students = []

    for full_name in student_dict.keys():
        year, month, day = student_dict[full_name]
        if month == today.month and day == today.day:
            birthday_students.append(full_name)
            
    if birthday_students:
        print(f"\nСьогодні {today.strftime('%d.%m.%Y')} святкують день народження:")
        for full_name in birthday_students:
            print(f"{full_name}")
    else:
        print(f"\nСьогодні {today.strftime('%d.%m.%Y')} ніхто зі студентів не святкує день народження.")


def main():

    students = {
        "Борозняк Олег Олександрович": (2006, 9, 28),
        "Шевченко Тарас Григорович": (2005, 3, 9),
        "Косач Лариса Петрівна": (2006, 2, 25),
        "Франко Іван Якович": (2006, 8, 27),
        "Стус Василь Семенович": (2005, 1, 6),
        "Костенко Ліна Василівна": (2006, 3, 19),
        "Симоненко Василь Андрійович": (2005, 1, 8),
        "Тичина Павло Григорович": (2005, 1, 23),
        "Довженко Олександр Петрович": (2006, 9, 24),
        "Грушевський Михайло Сергійович": (2005, 9, 29)
    }

    while True:
        print("\n--- ГОЛОВНЕ МЕНЮ ---")
        print("1. Вивести всі записи")
        print("2. Додати нового учня")
        print("3. Видалити учня")
        print("4. Вивести записи, відсортовані за ключем")
        print("5. Хто сьогодні святкує день народження?")
        print("0. Вихід")
        
        choice = input("Оберіть дію: ")
        
        match choice:
            case "1":
                print_all(students)
            case "2":
                add_record(students)
            case "3":
                delete_record(students)
            case "4":
                print_sorted(students)
            case "5":
                check_birthdays(students)
            case "0":
                print("Завершення роботи програми.")
                break
            case _:
                print("Некоректний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()