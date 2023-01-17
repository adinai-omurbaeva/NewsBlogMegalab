[Документация в Postman](https://www.postman.com/adinai-omurbaeva/workspace/newsblogmegalab/documentation/10420266-0de44cd8-cb22-4be6-a7ce-b259d0571482?entity=folder-4400ea06-1d08-45ab-b484-1295139abff2)

[Pythonanywhere](https://adinaiomurbaeva.pythonanywhere.com)

# News Blog

- [Table of Contents](#news-blog)
  - [Summary](#summary)
  - [Rules](#rules)
  - [Grading](#grading)
  - [Get started](#get-started)


## Summary

[Документация в Postman](https://www.postman.com/adinai-omurbaeva/workspace/newsblogmegalab/documentation/10420266-0de44cd8-cb22-4be6-a7ce-b259d0571482?entity=folder-4400ea06-1d08-45ab-b484-1295139abff2)
[Pythonanywhere](https://adinaiomurbaeva.pythonanywhere.com)

Вашим заданием на близжайшие 4 недели будет реализовать API по дизайну.

- [Дизайн](https://www.figma.com/file/tvDHJjr7Nj1rrD3qoUs9v7/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%BD%D0%BE%D0%B9-%D0%BF%D0%BE%D1%80%D1%82%D0%B0%D0%BB?node-id=0%3A1)

Исходя из дизайна проекта, выясните основные требования и по ним реализуйте API, используя `Django`, `Django Rest Framework` и `PostgreSQL`

## Rules

С [общими правилами](/RULES.md) можете ознакомиться здесь

## Grading

Задание будет оцениваться по следующим критериям:

1. Код стилистически оформлен согласно конвенциям
2. Наличие коммитов демонстрирующих о проделанной работе (частота и оформление коммитов будут играть большую роль при оценивании)
3. Реализованная логика
4. Наличие документации в виде коллекции в Postman или Swagger. Здесь будет оцениваться:
    - насколько легко в ней ориентироваться
    - насколько понятно названы и описаны endpoint'ы
5. Проект развернут 
6. Написаны unit тесты с помощью pytest* (pytest-django, factory-boy, faker)
7. В проекте используется контейнеризация Docker*

Задания помеченные `*` являются бонусными, их можно не делать, но за них даются доп. баллы

## Get started

1) Создайте виртуальное окружение

У себя я делаю это командой:

```
python -m venv venv
```

> В зависимости от системы и установленных модулей команда может отличаться, имейте в виду.

2) Затем создайте файл для хранения переменных среды:  `.env`

Обязательно ознакомьтесь с тем, как работают переменные среды

В текущем проекте будет использоваться [django-environ](https://django-environ.readthedocs.io/en/latest/)

```
cp env.example .env
```

- [ ] Убедитесь, что .env файл занесен в реестр игнорируемых файлов в `.gitignore`
- [ ] Присвойте каждой переменной актуальные данные

3) Затем установите необходимые зависимости

> Убедитесь, что виртуально окружение активировано.
> Для этого у себя я запускаю команду `source venv/bin/activate`
 
У себя я делаю это командой:

```
poetry install
```
