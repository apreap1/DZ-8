from datetime import date, timedelta, datetime


    
def get_birthdays_per_week(users):
    #print(users)    
    data = {}

    if not users: #перевірка на порожній список колег
        return data
  
    date_today = date.today() #поточна дата
 
    period = {}

    for i in range(7):   # створимо словник з датами які перевірятимимо на дні народження
        period[date_today.day, date_today.month] = date_today.year
        date_today += timedelta(1) 

    for user in users:    #перебираємо кожного колегу зі списку
        date_birthday = user["birthday"]
        day_month = date_birthday.day, date_birthday.month    #створюємо tuple з днем та місяцем народження колег

        if day_month in list(period):    #якшо день та місяць дня народження входить в список дат для перевірки

            date_birthday = date_birthday.replace(year = period[day_month])    #замінюємо рік народження на рік в періоді перевірки

            if date_birthday.weekday() in (5, 6):   #якщо день народження у вихідні, то переносимо на понеділок
                day_wekk = "Monday"
            else:
                day_wekk = date_birthday.strftime("%A")   #день тижня коли випадає день народження
            if day_wekk not in data:    #якщо дня тижня немає в словнику то додаємо день тижня як ключ і пустий список як значення
                data[day_wekk] = []
            data[day_wekk].append(user["name"])    #до списку по ключу дня тижня додаємо ім'я колеги
    #print(data)
    return data

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Doe Koum", "birthday": datetime(1976, 11, 5).date()},
        {"name": "Kim", "birthday": datetime(1976, 11, 10).date()},
        {"name": "Li", "birthday": datetime(1976, 11, 9).date()},
        {"name": "Bill", "birthday": datetime(1976, 11, 11).date()},
    ]

    result = get_birthdays_per_week(users)
    #print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")