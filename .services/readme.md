1. **Скопировать файл в системную папку**
    ```sh
    sudo cp /путь/к/вашему/job_request_bot.service /etc/systemd/system/
    ```

1. **Перезагрузка systemd**: После внесения изменений в файл конфигурации не забудьте перезагрузить systemd, чтобы он увидел изменения:
   ```bash
   sudo systemctl daemon-reload
   ```

1. **Запуск и включение службы**: После этого вы можете запустить службу и включить её автозапуск:
   ```bash
   sudo systemctl start job_request_bot.service
   sudo systemctl enable job_request_bot.service
   ```

1. **Логи**: Если служба не запускается, вы можете просмотреть логи с помощью команды:
   ```bash
   journalctl -u job_request_bot.service
   ```

