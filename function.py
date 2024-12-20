import re

# Функция для очистки номера телефона
def clean_phone_number(phone):
    # Удаляем все символы, кроме цифр
    cleaned = re.sub(r'\D', '', phone)
    return cleaned