""""
Программа должна переводить число, введенное с клавиатуры в метрах, в километры.
1.
2.	Пример:
3.	Введите число в метрах:
4.	2048
5.	2.048 км
6.

"""
KM_METER = 1000
meter_1 = int(input('Введите число в метрах:'))
result = meter_1 / KM_METER
print('Результат =', result ,'км')
