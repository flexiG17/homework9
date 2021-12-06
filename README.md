# Кожевников Арсений АТ-08
## Задание с профилированием, doc-тестами и прочим

### 1. Результат запуска файла new_filter.py (результат прошлого дз) с помощью профилизатора PyCharm:

![5. with input data.PNG](https://github.com/flexiG17/homework9/blob/main/Images/5.%20with%20input%20data.PNG?raw=true)
### 2. Результат запуска файла old_filter.py (изначально данный код):

![6. old_filter without input data](https://github.com/flexiG17/homework9/blob/main/Images/6.%20old_filter%20without%20input%20data.PNG?raw=true)
### 3. Результат работы нового фильтра:

![8. filter_with_filename.PNG](https://github.com/flexiG17/homework9/blob/main/Images/8.%20filter_with_filename.PNG?raw=true)
### 4. Выводы
Мы можем заметить сильную разницу во времени выполнения. 
Всё дело в том, что в случае 1 мы запускаем фильтр с ручным вводом данных, 
что занимает наибольшее кол-во времени и тормозит работу программы.
В случае работы файла из пункта 2 отстутвует ручной ввод данных, однако стандартные
алгоритмы работают очень медленно. И наконец случай 3, где мы проверяем скорость
работы нового файла filter_with_filename.py, где прописаны улучшенные алгоритмы
и не предусмотрен ручной ввод данных. По результатам мы видим, что код в данном
пункте работает в разы быстрее, чем в двух предыдущих.
## 5. Результат работы doc-тестов:

![9. doctests.png](https://github.com/flexiG17/homework9/blob/main/Images/9.%20doctests.png?raw=true)

## 6. Изаначально используемое изображение:
![img.jpg](https://github.com/flexiG17/homework9/blob/main/img.jpg?raw=true)
## 7. Изображение в результате работы пунктов 1 и 3: 
![first_res.jpg](https://github.com/flexiG17/homework9/blob/main/Images/first_res.jpg?raw=true)
## 8. Изображение в результате работы пункта 2:
![second_res.jpg](https://github.com/flexiG17/homework9/blob/main/Images/second_res.jpg?raw=true)