<h1 align="center">REST API сервис</h1>

## Как пользоваться?
* Перейдите в каталог /app
```
cd src/app
```
* Создайте .env файл
* Укажите необходимые переменные, к примеру, для работы репозитория с памятью, укажите:
```
REPOSITORY_TYPE=Memory
```
* Или, для работы с базой данных Postgresql, укажите:
```
DB_URI=postgresql+asyncpg://user:password@host/db_name
REPOSITORY_TYPE=Postgres
```
* Далее запустите приложение
```
uvicorn src.main:app --host=0.0.0.0 --port 8000 --log-level=info
```