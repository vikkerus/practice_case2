import datetime

# Функция для определения дня недели, по введенным данным
def weekDay(day, month, year):
    days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
    day_num = datetime.datetime(year, month, day).weekday()
    return days[day_num]

# Функция для определения високосный ли год
def leapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# Функция для определения возраста пользователя
def ageCalc(year):
    this_year = datetime.datetime.now().year
    age = this_year - year
    return age


# 1. функция, которая запрашивает у пользователя последовательно день его рождения, месяц и год
day = int(input('Введите день рождения в формате ДД: '))
month = int(input('Введите иеяц рождения в формате ММ: '))
year = int(input('Введите год рождения в формате ГГГГ: '))

# 2. функция, которая выводит, какому дню недели соответствует эта дата
print(f"День недели: {weekDay(day, month, year)}")

# 3. функция, которая выводит високосный ли год
if leapYear(year):
    print("Високосный год")
else:
    print("Не високосный год")

# 4. функция, которая выводит возраст пользователя
age = ageCalc(year)
print(f"Вам {age} лет")

# 5. функция для вывода даты рождения пользователя в формате со звездочками
print(f"Дата рождения: {'*'*day} {'*'*month} {'*'*year}")
