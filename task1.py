from datetime import datetime
from collections import defaultdict

def get_birthdays_per_week(users):

    birthdays = defaultdict(list) # Створюємо порожній словник 
    today = datetime.today().date() # Отримуємо поточну дату системи для подальшого порівняння з датами народження користувачів

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  # Конвертуємо час народження до типу date, видаляючи часову частину.
        birthday_this_year = birthday.replace(year=today.year) # Рядок використовує метод replace() для заміни значення року у даті на значення поточного року (today.year).

        if  birthday_this_year < today: #Перевіряємо, чи вже минув день народження цього року
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7: # Що день народження користувача відбудеться протягом наступного тижня
            weekday = birthday_this_year.strftime('%A') # 
            
            if weekday in ['Saturday', 'Sunday']: 
                weekday = 'Monday' 
            birthdays[weekday].append(name)

    for weekday, names in birthdays.items():# Результат розрахунку
        print(f"{weekday}: {', '.join(names)}")







