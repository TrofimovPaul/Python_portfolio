# -*- coding: utf-8 -*-
"""ДЗ Визуализация.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zyXnmCyvNATYVlvoSgI6nyRDTCC3x7of
"""

#1
"""
Домашнее задание к лекции "Визуализация данных"

Обязательная часть
Вам необходимо провести базовый EDA выбранного набора данных.

Требования к анализу:

    построить не менее 4 визуализаций различных видов;
    каждая визуализация должным образом оформлена и читается даже в отрыве от контекста;
    по каждой визуализации необходимо написать вывод (какую гипотезу на ее основе можно выдвинуть?).

Откуда брать данные?

Можете взять свои рабочие данные, либо найти открытые данные (например, на kaggle.com) по интересующей вас предметной области (тогда не забудьте их выложить на github вместе с ноутбуком).
Если идей нет, можете взять один из перечисленных ниже:

    данные приложений из Google Play;
    данные о видео из трендов YouTube;
    данные об уровне счастья в разных странах.
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df1 = pd.read_csv('SquirrelDF.csv')
df1.head()
df1.describe()
#df1.info()

df1['Primary Fur Color'].unique()

df2 = df1.loc[~df1[['Primary Fur Color']].isna().any(1)]
#df2.info()

a = len(df2.loc[df2['Primary Fur Color'] == df2['Primary Fur Color'].unique()[0]])
b = len(df2.loc[df2['Primary Fur Color'] == df2['Primary Fur Color'].unique()[1]])
c = len(df2.loc[df2['Primary Fur Color'] == df2['Primary Fur Color'].unique()[2]])

df3 = pd.DataFrame({'Color': ['Gray', 'Cinnamon', 'Black'], 'Count': [a, b, c]})

#Диаграмма №1
df3['Count'].plot(kind = 'pie', labels = df3.Color, autopct='%.2f')
#диаграмма показывает, что больше всего в парке белок серого цвета, а именно 83,32%.

#2
df2 = df2.groupby('Primary Fur Color').count()

#3
#второй вариант построения всеми нелюбимой диаграммы 
df2['Unique Squirrel ID'].plot.pie(autopct='%.2f', figsize=(6, 6), colors = ['gray', '#EE6A50', 'darkgray'], fontsize = 14, title = 'Соотношение белок в парке по цветам')

#4
from datetime import datetime
df4 = df1.copy()
df4 = df4.replace(False, np.nan)
def datefunc(i):
  i = datetime.strptime(str(i), "%m%d%Y")
  return i.strftime("%Y-%m-%d %A")
df4['Date'] = df4['Date'].apply(datefunc)
df4 = df4.groupby('Date').count()

from pandas.core.frame import DataFrame
hect_list = []
sect_list = []
for i in df1['Hectare']:
  k = list(i)
  m = k[0]+k[1]
  sect_list.append(k[2])
  hect_list.append(int(m))
df1['sector'] = sect_list
df1['hectare number'] = hect_list

#5
#Диаграмма №2
df4['Unique Squirrel ID'].plot(kind = 'line', title = 'Количество увиденных за день белок', fontsize = 10, figsize = (20,10), grid = True)
plt.show()
#Диаграмма показывает, сколько белок встретились наблюдателям за день. На диаграмме имеются два спада, начинающиеся после выходных дней.
#Возможно, это связано с тем, что в выходные дни в парке гуляет больше людей, которые подкармливают грызунов, тем самым выманивая их из нор/дупел.
#Сомнение в данной гипотезе возникает по той причине, что к 20 числам октября, количество увиденных белок снижается. Возможно, есть зависимость от погодных условий

df5 = df1.copy()
df5 = df5.replace(False, 0)
df5 = df5.replace(True, 1)
df5 = df5.groupby('Hectare Squirrel Number').count()

#Диаграммы №3,4
#Диаграммы показывают было ли безразлично белкам, которые ели, появление человека рядом. То есть отвлекли ли наблюдатели белок от еды.
#Из диаграмм можно предположить, что белкам, которые ели, по большей части появление человека было безразлично.
df4.plot(kind = 'scatter', x = 'Eating', y = 'Indifferent', title = 'Зависимость между состояниями "Употребление пищи" и "Безразличие при появлении человека"')
df4.plot(kind = 'scatter', x = 'Eating', y = 'Runs from',  title = 'Зависимость между состояниями "Употребление пищи" и "Побег при появлении человека"')
#Это подтверждается и расчётом корреляции
print(df4[['Eating','Indifferent']].corr(method = 'pearson'),'\n')
print(df4[['Eating','Runs from']].corr(method = 'pearson'),'\n')
plt.show()

#6
#Диаграммы №5,6,7
#Диаграммы показывают распределение белок разного цвета по гектарам
df6 = df1.groupby(['Hectare Squirrel Number', 'Primary Fur Color']).agg({'Primary Fur Color':'count'})
df6['PFC2'] = df6['Primary Fur Color']
df6 = df6.drop(columns = 'Primary Fur Color').reset_index()
df7 = df6.loc[df6['Primary Fur Color'] == 'Black']
df8 = df6.loc[df6['Primary Fur Color'] == 'Cinnamon']
df9 = df6.loc[df6['Primary Fur Color'] == 'Gray']
plt.show()
df7 = df7.reset_index()
df7 = df7.drop(columns = 'index')
df7['PFC2'].plot.bar(title = 'Количество чёрных белок по гектарам')
plt.show()
df8 = df8.reset_index()
df8 = df8.drop(columns = 'index')
df8['PFC2'].plot.bar(title = 'Количество коричневых белок по гектарам')
plt.show()
df9 = df9.reset_index()
df9 = df9.drop(columns = 'index')
df9['PFC2'].plot.bar(title = 'Количество серых белок по гектарам')
plt.show()

"""
Дополнительная часть (необязательная)

    построить дополнительно не менее 2 визуализаций (итого не менее 6);
    в работе должны присутствовать следующие визуализации: boxplot, heatmap, scatter plot matrix;
"""