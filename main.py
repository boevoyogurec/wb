import pandas as pd
from openpyxl import load_workbook

def clean_phone_number(phone):
    # Преобразуем значение в строку, если оно число
    if isinstance(phone, int) or isinstance(phone, float):
        phone = str(int(phone))

    # Убираем все символы кроме цифр
    return ''.join([char for char in phone if char.isdigit()])

# Загружаем исходный файл
input_file = 'phone_numbers.xlsx' # изменить на свой путь
df = pd.read_excel(input_file)

# Указываем имя столбца с номерами телефонов
phone_column_name = 'phone_number'

# Проверяем наличие столбца
if phone_column_name not in df.columns:
    print(f"Столбец '{phone_column_name}' отсутствует в файле.")
else:
    # Очищаем номера телефонов
    df[phone_column_name] = df[phone_column_name].apply(clean_phone_number)

    # Сохраняем результат в новый файл
    output_file = 'cleaned_phones.xlsx'
    writer = pd.ExcelWriter(output_file, engine='openpyxl')
    df.to_excel(writer, index=False)
    writer.close()  # Используем close() вместо save()