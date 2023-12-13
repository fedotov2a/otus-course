log_parser предназначен для парсинга файлов access.log

Запуск скрипта возможен в двух режимах:

- Парсинга файла: ./log_parser.py file [path-to-log-file]
- Парсинг файлов в указанной директории: ./log_parser.py dir [path-to-log-dir] - в указанной директории будут отобраны файлы, которые заканчиваются на .log


Скрипт также распознает симлинки и переходит по ним до целевого файла.

Результатом работы будет json файл со следующей структурой:
```json
{
    "total_requests": 0,
    "requests_by_methods": {
        "METHOD1": 0,
        "METHOD2": 0,
        ...
        "METHODN": 0
    },
    "top_ip": {
        "ip1": 0,
        "ip2": 0,
        "ip3": 0
    },
    "top_long_requests": [
        {
            "method": "METHOD1",
            "url": "/url",
            "http_code": 200,
            "ms": 0,
            "datetime": " [dd/mm/YYYY:HH:MM:SS +0000]",
            "ip": "ip"
        },
        {
            "method": "METHOD2",
            "url": "/url",
            "http_code": 200,
            "ms": 0,
            "datetime": " [dd/mm/YYYY:HH:MM:SS +0000]",
            "ip": "ip"
        },
        {
            "method": "METHOD3",
            "url": "/url",
            "http_code": 200,
            "ms": 0,
            "datetime": " [dd/mm/YYYY:HH:MM:SS +0000]",
            "ip": "ip"
        }
    ]
}
```
