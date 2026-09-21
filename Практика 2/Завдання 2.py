def remove_duplicates(list):
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

user_input = input("Введіть елементи списку через пробіл: ")
my_list = user_input.split()

result = remove_duplicates(my_list)
print("\nОригінальний список:", my_list)
print("Список після видалення повторень:", result)