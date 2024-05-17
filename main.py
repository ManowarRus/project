from src.widget import convert_date, get_masks_bank_accounts_cards

card_check_number = str(input("Введите номер карты или счет: "))
print(get_masks_bank_accounts_cards(card_check_number))

date_number = str(input("Введите строку даты: "))
print(convert_date(date_number))


# Maestro 1596837868705199
# Счет 64686473678894779589
# MasterCard 7158300734726758
# Счет 35383033474447895560
# Visa Classic 6831982476737658
# Visa Platinum 8990922113665229
# Visa Gold 5999414228426353
# Счет 73654108430135874305
# 2018-07-11T02:26:18.671407
