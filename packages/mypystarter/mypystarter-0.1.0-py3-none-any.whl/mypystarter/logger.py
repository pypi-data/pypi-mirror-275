import sys

import loguru


def custom_filter(record):
    extra = record.get('extra', {}).copy()
    record['reqId'] = extra.pop('reqId', None) if extra.get('reqId', None) else None
    record['user'] = extra.pop('user', None) if extra.get('user', None) else None
    record['extra'] = extra
    return record


def formatter(record):
    colors: dict = {'DEBUG': 'blue', 'INFO': 'green', 'WARNING': 'yellow', 'ERROR': 'red', 'CRITICAL': 'magenta'}
    color = colors.get(record["level"].name, 'white')

    result = [
        f'<green>{record["time"]:YYYY-MM-DD HH:mm:ss.SSS}</green>',
        f'<{color}>{"{level}"}</{color}>',
        f'<{color}>{"{reqId}"}</{color}>',
        f'<{color}>{"{name}"}:{"{function}"}:{"{line}"}</{color}>',
        f'<{color}>{"{message}"}</{color}>',
        f'<white>{"{user}"}</white>',
        '<red>{extra}</red>',
    ]
    return ' | '.join(result) + '\n'


app_logger = loguru.logger

log_handlers = [
    {'sink': sys.stderr, 'colorize': True, 'format': formatter, 'filter': custom_filter},
    {'sink': 'logs/info.log', 'rotation': '1 week', 'level': 'INFO', 'format': formatter, 'filter': custom_filter},
    {'sink': 'logs/error.log', 'rotation': '1 week', 'level': 'ERROR', 'format': formatter, 'filter': custom_filter},
    {'sink': 'logs/debug.log', 'rotation': '1 week', 'level': 'DEBUG', 'format': formatter, 'filter': custom_filter},
    {'sink': 'logs/critical.log', 'rotation': '1 week', 'level': 'CRITICAL', 'format': formatter, 'filter': custom_filter},
]

app_logger.configure(handlers=log_handlers)
