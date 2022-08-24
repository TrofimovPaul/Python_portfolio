# -*- coding: utf-8 -*-
"""ДЗ №5. Классификация и кластеризация

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vJzUstUsPX_WiZc7sFgC3HJYGSi3LiQW
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

#     Возьмите датасет с цветками iris’а (функция load_iris из библиотеки sklearn)
iris_data = load_iris()
df1 = pd.DataFrame(iris_data.data, columns = iris_data.feature_names)
df1_target = iris_data.target

#     Оставьте два признака - sepal_length и sepal_width и целевую переменную - variety
df1 = df1[['sepal length (cm)', 'sepal width (cm)']]
df1
#     Разделите данные на выборку для обучения и тестирования
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df1, df1_target, test_size=0.3, random_state=42)

#     Постройте модель LDA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
lda = LinearDiscriminantAnalysis()

#     Обучаем модель
lda.fit(X_train, y_train)

#     Предсказываем значения по тестовым значениям признаков
lda.predict(X_test)

#     Сравнение результатов предсказания и тестовых целевых значений. Значение точности
difference_list = pd.DataFrame([y_test, lda.predict(X_test)]).T
from sklearn.metrics import accuracy_score
accuracy_score(y_test, lda.predict(X_test))

#     Коэффициенты дискриминантных линий
lda.coef_

#     Центры классов
lda.means_

#     Визуализируйте предсказания для тестовой выборки и центры классов
plt.scatter(x=X_test['sepal length (cm)'], y=X_test['sepal width (cm)'], c=lda.predict(X_test), cmap = 'summer')
plt.scatter(lda.means_[:, 0], lda.means_[:, 1], c='r', s=150, marker='o')
plt.show()

#     Визуализируйте y_test для тестовой выборки и центры классов
plt.scatter(x=X_test['sepal length (cm)'], y=X_test['sepal width (cm)'], c = y_test, cmap = 'summer')
plt.show()

#     Отбросьте целевую переменную и оставьте только два признака - sepal_length и sepal_width
df2 = pd.DataFrame(iris_data.data, columns = iris_data.feature_names)
df2 = df2[['sepal length (cm)', 'sepal width (cm)']]
df2

#     Подберите оптимальное число кластеров для алгоритма kmeans и визуализируйте полученную кластеризацию
from sklearn.cluster import KMeans
# явно указываем количество кластеров
kmeans = KMeans(n_clusters=3)
# fit_predict обучается на данных и каждому объекту присваивает кластер
clusters = kmeans.fit_predict(df2)
clusters
plt.scatter(df2['sepal length (cm)'], df2['sepal width (cm)'], cmap='winter', c=clusters, s=25)
plt.show()

# строим график локтя

# создаем список для инерции
k_inertia = []
# задаем диапазон кластеров
ks = range(1, 20)


for k in ks:
    clf_kmeans = KMeans(n_clusters=k)
    clusters_kmeans = clf_kmeans.fit_predict(df2)
    # добавляем инерцию каждой модели в список
    k_inertia.append(clf_kmeans.inertia_)

plt.plot(ks, k_inertia)
plt.plot(ks, k_inertia , 'bo')
plt.show()
#Согласно методу локтя целесообразно выбрать 2 или 3 кластера 

kmeans = KMeans(n_clusters=2)
# fit_predict обучается на данных и каждому объекту присваивает кластер
clusters = kmeans.fit_predict(df2)
clusters
plt.scatter(df2['sepal length (cm)'], df2['sepal width (cm)'], cmap='winter', c=clusters, s=25)
plt.show()