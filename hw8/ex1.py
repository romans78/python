class Date:
    day = 1
    month = 1
    year = 2000

    def __init__(self, date_string):
        self.__date_string = date_string

    @classmethod
    def extract_dmy(cls, date_string):
        cls.day, cls.month, cls.year = map(int, date_string.split("-"))
        return (cls.day, cls.month, cls.year)

    @staticmethod
    def validate_date(date_string):
        # выдаст ошибку, если день, месяц, год не является числом
        day, month, year = map(int, date_string.split("-"))
        is_leap_year = (year % 4 == 0) and ((True if year % 400 == 0 else False) if year % 100 == 0 else True)
        if month < 1 or month > 12:
            print("Ошибка: месяц должен быть в промежутке от 1 до 12")
            return
        n_days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if is_leap_year:
            n_days_in_month[2] = 29
        if day < 1 or day > n_days_in_month[month]:
            print(f"Ошибка: день должен быть в промежутке от 1 до {n_days_in_month[month]}")
            return
        print("Формат даты верен")


print(Date.extract_dmy("31-10-1978"))
Date.validate_date("31-10-1978")
Date.validate_date(("29-2-1900"))
Date.validate_date(("29-2-2000"))
