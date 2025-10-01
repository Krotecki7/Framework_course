# TG-бот с напоминанием о ваших привычках

### Локальный запуск проекта

1. Клонируйте репозиторий командой: `gh repo clone Krotecki7/homework30`
2. Установите зависимости: `pip install --no-cache-dir -r requirements.txt`
3. Введите команду `python manage.py runserver` и перейдите http://127.0.0.1:8000/

### Настройка сервера и работы CI/CD

1. Подключаемся к серверу с помощью команды: `ssh -l username@server_ip`
2. Устанавливаем Docker командой: `sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`
3. Устанавливаем Git командой: `sudo apt-get install git`
4. Устанавливаем Nginx командой: `sudo apt-get install nginx`
5. Работа CI/CD pipeline:
   - workflow активируется при каждом push и pull request
   - В процессе происходит проверка кода линтером flake8, тестирование, сборка и деплой
6. Деплой:
   - После успешного выполнения pipeline происходит автоматический деплой на сервер
   - Статус выполнения каждого этапа можно посмотреть в Git-репозитории во вкладке actions
7. Приложение будет доступно по адресу: http://158.160.202.4:8001/