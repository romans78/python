def print_user_data(firstname, lastname, birth_year, city, email, phone):
    print(f"Информация о пользователе. Имя: {firstname} {lastname}, Год рождения:"
          f" {birth_year}, Город проживания: {city}, Email : {email}, Телефон: {phone}")


firstname = input("Введите Ваше имя: ")
lastname = input("Введите Вашу фамилию: ")
birth_year = input("Введите Ваш год рождения: ")
city = input("Введите Ваш город проживания: ")
email = input("Введите Ваш email: ")
phone = input("Введите Ваш телефон: ")

print_user_data(firstname=firstname, lastname=lastname, birth_year=birth_year, city=city, email=email, phone=phone)