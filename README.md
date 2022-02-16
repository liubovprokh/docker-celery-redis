# test_task

Запуск проекта:
1. создать файл .env/.env_file в соответствии с .env_template
2. docker-compose build && docker-compose up -d && docker-compose logs -f
3. Урл запуска импорта http://localhost:80/run-import-task
4. Урл получения данных пользователей http://localhost:80/data_api/weight?user_id=12345
5. Так же они есть тут: https://www.getpostman.com/collections/1f6976db4760a800c591
6. Поменять данные пользователя можно в файле src/server/apps/service_api/views.py
