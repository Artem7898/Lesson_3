 GeekBrains
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать, то реализуйте ф-цию-декоратор и пусть она считает время И примените ее к двум своим функциям.

############################################################################################################

Задание 2. Ваша программа должна запрашивать пароль Для этого пароля вам нужно получить хеш, используя функцию sha256 Для генерации хеша обязательно нужно использовать криптографическую соль Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно Вам нужно проверить, совпадает ли пароль с исходным Для проверки необходимо сравнить хеши паролей

ПРИМЕР: Введите пароль: 123 В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b Введите пароль еще раз для проверки: 123 Вы ввели правильный пароль.

#################################################################################################################

Задание 3. Определить количество различных подстрок с использованием хеш-функции. Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар ра ар ара р а.

####################################################################################################################

Задание 4. Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования Можете условжнить задачу, реализовав ее через ООП.
