class Decimal:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator can't be zero")
        self._numerator = numerator
        self._denominator = denominator


    def input_data(self):
        try:
            num = int(input('Введите числитель: '))
            den = int(input('Введите знаменатель: '))

            if den == 0:
                raise ValueError("Denominator can't be zero")

            self._numerator = num
            self._denominator = den

        except ValueError:
            print('Ошибка ввода данных!')
