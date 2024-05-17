def max_product(nums):
    """Функцию, которая принимает на вход список целых чисел
    и возвращает максимальное произведение двух чисел из списка"""
    if len(nums) < 2:
        return 0
    nums.sort()
    return max(nums[-1] * nums[-2], nums[0] * nums[1])


# Примеры входных данных
input_data = [[2, 3, 5, 7, 11], [-5, -7, -9, -13], [1, 2], [4]]

# Вывод результатов для примеров
for data in input_data:
    output = max_product(data)
    print(output)
