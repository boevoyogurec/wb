from function import *

df = input_excel_file('phone_numbers.xlsx') # изменить на свой путь
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