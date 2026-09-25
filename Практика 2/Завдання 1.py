import string
while True:
    text = input("Введіть речення (щонайменше 7 слів): ")
    split_str = text.split()

    if len(split_str) >= 7:
        break
    print("Помилка: речення містить менше 7 слів. Спробуйте ще раз.\n")

count = 0
for word in split_str:
    cleaned = word.strip(string.punctuation + '«»')
    if cleaned.lower().endswith('р'):
        count += 1
print(f"Кількість слів у реченні, які закінчуються на літеру «р»: {count}")
