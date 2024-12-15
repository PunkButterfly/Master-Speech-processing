# Описание проекта
Главная страница содержит текстовое окно с заранее заданным стандартным текстом, при заполнении которого текст автоматически озвучивается предобученной русскоязычной моделью **facebook/mms-tts-rus**, после чего появляется аудио-проигрыватель и возможность скачать озвучку
# Структура проекта
| -> .github/workflows - CI/CD  
| -> backend  
|--| -> [api.py](https://github.com/PunkButterfly/Master-Speech-processing/blob/main/backend/api.py) - Бэкенд, обрабатывающий запрос  
|--| -> [voicer.py](https://github.com/PunkButterfly/Master-Speech-processing/blob/main/backend/voicer.py) - Класс с предобученной моделью, работает в связке с основным бэкендом  
| -> frontend  
|--| -> [app.py](https://github.com/PunkButterfly/Master-Speech-processing/tree/main/frontend/app.py) - Фронтенд, отправляющий запрос  
| -> preimages - Файлы с зависимостями и системные файлы для docker images первого слоя  
| -> [docker-compose.yaml](https://github.com/PunkButterfly/Master-Speech-processing/blob/main/docker-compose.yaml) - Основной docker-compose файл для разворачивания проекта  
| -> [local-compose](https://github.com/PunkButterfly/Master-Speech-processing/blob/main/local-compose) - Файл для локального запуска docker-compose  

# Деплой проекта
## Проект развернут на удаленной ВМ
Доступен по http://voicing.punkbutterfly.tech/  
> Либо  
> FRONTEND http://158.160.17.229:20006  
> BACKEND http://158.160.17.229:20005/docs

**Для более быстрого разворачивания проекта настроен CI/CD**  
### [InitializingVMRepository.yml](https://github.com/PunkButterfly/Master-Speech-processing/blob/main/.github/workflows/InitializingVMRepository.yml)
При ручном запуске создает необходимое пространство на ВМ и делит проект на main и test ветки(окружения)  
### [Deploying.yml](https://github.com/PunkButterfly/Master-Speech-processing/blob/main/.github/workflows/Deploying.yml)
В зависимости от измененной ветки (push to test, closed PR to main) разворачивает на удаленной ВМ сервис в соответствующих портах
## Запуск проекта локально
1. Установить docker
2. Склонировать репозиторий
3. Создать виртуальное окружение для проекта
4. В файле _local-compose_ заменить переменные окружения _PROJECT_NAME, BACKEND_PORT, FRONTEND_PORT_ на другие  
   или оставить как есть
6. Сделать bash скрипт запуска локального docker compose _local-compose_ исполняемым
```commandline
chmod +x local-compose
```
6. Запустить локально docker compose
```commandline
./local-compose
```
API будет доступен по localhost:_BACKEND_PORT_/docs  
WEB будет доступен  по localhost:_FRONTEND_PORT_

