__all__ = [
    'app',
    'config',
    'controllers',
    'services',
    'utils'
]

import logging

logging.basicConfig(
    format='[%(asctime)s] '
           'Thread: %(threadName)s, '
           'module: %(module)s '
           'at %(funcName)s '
           '(line %(lineno)s) '
           '- %(levelname)s - '
           '%(message)s',
    level=logging.INFO
)
if logging.root.level > logging.DEBUG:
    # prevents log spam from infinite polling
    logging.getLogger("httpx").setLevel(logging.WARNING)
