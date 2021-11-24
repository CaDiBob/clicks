# Обрезка ссылок с помощью Битли

Скрип укорачивает ссылки с помощью сервиса [Bitly](https://bitly.com/), 
а так же считает количество переходов по уже укороченным ссылкам.

Пример работы скрипта:
1. Обрезка ссылок.
```
user@home:~$ python main.py https://mail.ru
Битлинк: https://bit.ly/3FHRNIV

```
2. Просмотр количества переходов.
```
user@home:~$ python main.py https://bit.ly/3FHRNIV
По вашей ссылке прошли: 1 раз(a)

```

### Как установить

Для работы скрипта необходим API сервиса [Bitly](https://bitly.com/).
Для получения API необходимо зарегистрироваться на сервисе [Bitly](https://bitly.com/a/sign_up).

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).