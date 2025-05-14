# test_task

## Сборка и запуск:
### Для корректного отображения меню при запуске следует сначала создать его а так-же добавить в него элементы в админ панели Django

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Nunime/test_task.git
```

```
cd test_task
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
cd test_task
```

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```