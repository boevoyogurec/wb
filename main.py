import pandas as pd
import re

# Функция для очистки номера телефона
def clean_phone_number(phone):
    # Удаляем все символы, кроме цифр
    cleaned = re.sub(r'\D', '', phone)
    return cleaned

# Чтение файла Excel
input_file = 'phone_numbers.xlsx'
df = pd.read_excel(input_file, engine='openpyxl')

# Предполагаем, что номера телефонов находятся в столбце с именем 'Телефон'
df['phone_number'] = df['phone_number'].apply(clean_phone_number)

# Сохранение результата в новый файл Excel
output_file = 'cleaned_phone_numbers.xlsx'
df.to_excel(output_file, index=False, engine='openpyxl')

#что-то неопнятное
