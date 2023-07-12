def most_wanted_letter(string):
    #Создаем словарь для хранения букв
    letter_count = {}

    # Подсчет количества вхождений 
    for letter in string:
        if letter.isalpha():  # Функция на проверку букв
            letter = letter.lower()  # Нижний регистр
            if letter in letter_count:
                letter_count[letter] += 1 
            else:
                letter_count[letter] = 1
    if not letter_count:
        return "String hasn't letter"
    max_count = 0
    most_frequent_letter = ''
    #Ищем самую чато встречающую букву
    for letter, count in letter_count.items():
        if count > max_count:
            max_count = count
            most_frequent_letter = letter

    return most_frequent_letter



input_string = input()
print("Most frequent letter :", most_wanted_letter(input_string))
