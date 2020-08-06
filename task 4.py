"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import urllib.request
import hashlib
import uuid

doc = urllib.request.urlopen("http://mail.ru")
hash_big = hashlib.sha256(b"http//mail.ru")
salt = uuid.uuid4().hex
hex_dig = hash_big.hexdigest()
doc = urllib.request.urlopen("http://mail.ru")
print(doc.read()[:350],[hex_dig])
print(doc.info())