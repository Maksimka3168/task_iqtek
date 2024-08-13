<h1 align="center">REST API сервис</h1>

## Как пользоваться?
* Создайте файл .env в каталоге /src/app или настройте переменные окружения другим способом. 
* Укажите необходимые переменные, к примеру, для работы репозитория с памятью, укажите:
```
REPOSITORY_TYPE=Memory
```
* Или, для работы репозитория с базой данных Postgresql, укажите:
```
DB_URI=postgresql+asyncpg://user:password@host/db_name
REPOSITORY_TYPE=Postgres
```
* Установите
```
pip install -e .
```
* И запустите
```
iqtek_task
```