# Проект API для Yatube

Колтаков Матвей Александрович 8В13

Клонировать репозиторий и перейти в него в терминале:

```
git clone https://github.com/nykerty/api_final_yatube.git
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv .venv
source .venv/bin/activate
```

Установить зависимости:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграцию:

```
python manage.py migrate
```

Запустить сервер:

```
python manage.py runserver
```

- Удаление комментария

```
DEL /api/v1/posts/{post_id}/comments/{comment_id}/
```
