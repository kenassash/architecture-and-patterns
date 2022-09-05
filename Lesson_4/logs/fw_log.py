"""Кофнфигурация логгера framework"""

import sys
import os
import logging
sys.path.append('../')


LOGGING_LEVEL = logging.DEBUG
FRAMEWORK_FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')


PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'framework.log')


STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(FRAMEWORK_FORMATTER)
STREAM_HANDLER.setLevel(logging.ERROR)
LOG_FILE = logging.FileHandler(PATH, encoding='utf-8')
LOG_FILE.setFormatter(FRAMEWORK_FORMATTER)


LOGGER = logging.getLogger('framework')
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(LOGGING_LEVEL)


if __name__ == '__main__':
    LOGGER.critical('Критическая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.debug('Отладочная информация')
    LOGGER.info('Информационное сообщение')