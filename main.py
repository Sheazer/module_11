import pprint
import matplotlib.pyplot as plt
import numpy as np


data = {'a': np.arange(50),#Создание последовательного списка от 0 до 50
        'c': np.random.randint(0, 50, 50),# Список из рандомных чисел от 1 до 50ти 50 элементов
        'd': np.random.randn(50)} #возвращает список чисел с небольим разбросом в диапазоне 0. 50 элементов
data['b'] = data['a'] + 15 * np.random.randn(50)# Задаем некий список вектора с диапазоном разброса 15 случайных чисел
data['d'] = np.abs(data['d']) * 100 #меняем середину диапазона на 100

plt.scatter('a', 'b', c='c', s='d', data=data)# Берем данные для таблицы с словаря data. 'c' отвечает за цвет а 's' за размеры
plt.xlabel('entry a') # Название строки X
plt.ylabel('entry b') # Название строки Y
plt.show() #Запустить показ