import re

def mask_card_or_account(input_str: str) -> str:
    if input_str.startswith("Счет"):
        return re.sub(r'(\d{2})(\d{14})', r'**\2', input_str, count=1)
    else:
        return re.sub(r'(\d{4}) (\d{2})(\*{4}) (\d{4})', r'\1 \2** **** \4', input_str, count=1)

input_data = input("Введите номер: ")  # Запрос на ввод данных

masked_data = mask_card_or_account(input_data)
print(masked_data)


# "Visa Platinum 7000 7922 8960 6361",
# "Maestro 7000 7922 8960 6361",
# "Счет 73654108430135874305"
