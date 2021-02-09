import datetime as dt


class Record:
    def __init__(self, amount, comment, date = dt.date.today()):
        self.amount = amount
        self.comment = comment
        if type(date) == dt.date:
            self.date = date
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date() 
    def show(self):
        print(f'{self.amount},{self.comment},{self.date}')


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def show(self):
        print(f'{self.records}')

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        constant = 0
        for record in self.records:
            if record.date == dt.datetime.now().date():
                constant += record.amount
        return constant
    
    def get_week_stats(self):
        constant = 0
        week = dt.date.today() - dt.timedelta(days = 7)
        for record in self.records:
            if week < record.date <= dt.date.today():
                constant += record.amount
        return constant


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        constant = 0
        for record in self.records :
            if record.date == dt.datetime.now().date():
                constant += record.amount
        calories = self.limit - constant
        if calories > 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calories} кКал'
        else :
            return f'Хватит есть!'


class CashCalculator(Calculator):
    USD_RATE = float(75)
    EURO_RATE = float(90)
    def get_today_cash_remained(self, currency):
        currency_str = {
            'rub': 'руб',
            'eur': 'Euro',
            'usd': 'USD'
        }
        sum_today = self.get_today_stats()
        rest = self.limit - sum_today
        if currency == 'usd':
            rest = round(rest / self.USD_RATE, 2)
        elif currency == 'eur':
            rest = round(rest / self.EURO_RATE, 2)
        else:
            rest = round(rest, 2)
        if rest > 0:
            return f'На сегодня осталось {rest} {currency_str[currency]}'
        elif rest == 0:
            return f'Денег нет, держись'
        else:
            rest = (-1) * rest
            return f'Денег нет, держись: твой долг - {rest} {currency_str[currency]}'