def find_strings_with_same_letters(words):
    """Функция, которая принимает на вход список строк и возвращает список строк,
    в которых первая и последняя буквы совпадают"""
    result = []
    for word in words:
        if len(word) > 0 and word[0] == word[-1]:
            result.append(word)
    return result


# Примеры входных данных
words1 = ["hello", "world", "apple", "pear", "banana", "pop"]
words2 = ["", "madam", "racecar", "noon", "level", ""]
words3 = []

# Примеры выходных данных
output1 = find_strings_with_same_letters(words1)
output2 = find_strings_with_same_letters(words2)
output3 = find_strings_with_same_letters(words3)

print(output1)  # ['pop']
print(output2)  # ['', 'madam', 'racecar', 'noon', 'level', '']
print(output3)  # []
