# Структура проекта
# Деплой проекта
## Проект развернут на удаленной ВМ
## Запуск проекта локально
1. Установить docker
2. Склонировать репозиторий
3. Создать виртуальное окружение для проекта
4. В файле _local-compose_ заменить переменные окружения _PROJECT_NAME, BACKEND_PORT, FRONTEND_PORT_ на другие или оставить как есть
5. Сделать bash скрипт запуска локального docker compose _local-compose_ исполняемым
```commandline
chmod +x local-compose
```
6. Запустить локально docker compose
```commandline
./local-compose
```
API доступен по localhost:_BACKEND_PORT_/docs  
WEB доступен  по localhost:_FRONTEND_PORT_

