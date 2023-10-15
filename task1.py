from datetime import datetime

def get_birthdays_per_week(users):
    users = defaultdict(list)
    current_date = datetime.today().date() # Отримуємо поточну дату системи для подальшого порівняння з датами народження користувачів
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  # Конвертуємо час народження до типу date, видаляючи часову частину.
        birthday_this_year = birthday.replace(year=today.year) # Рядок використовує метод replace() для заміни значення року у даті на значення поточного року (today.year).
        if  birthday_this_year < today(): #Перевіряємо, чи вже минув день народження цього року
            delta_days = (birthday_this_year - datetime.today()).days




