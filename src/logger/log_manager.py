# IMPORTS
from queue import SimpleQueue as Queue
from typing import List
import asyncio
import json
import logging
import logging.config


# CONSTANT DEFINITIONS
LOG_CONFIG_FILE_DEFAULT = "config/logger_config.json"


# CLASSES
class LocalQueueHandler(logging.handlers.QueueHandler):
    def emit(self, record: logging.LogRecord) -> None:
        # Removed the call to self.prepare(), handle task cancellation
        try:
            self.enqueue(record)
        except asyncio.CancelledError:
            raise
        except Exception:
            self.handleError(record)


# METHODS
def _setup_logging_queue(logger_name: str = '') -> None:
    """Move log handlers to a separate thread.

    Replace handlers on the root logger with a LocalQueueHandler,
    and start a logging.QueueListener holding the original
    handlers.

    """
    loggingQueue = Queue()
    queueHandler = LocalQueueHandler(loggingQueue)

    originalHandlers: List[logging.Handler] = []

    rootLogger = logging.getLogger(logger_name)
    rootLogger.addHandler(queueHandler)
    for h in rootLogger.handlers[:]:
        if h is not queueHandler:
            rootLogger.removeHandler(h)
            originalHandlers.append(h)

    listener = logging.handlers.QueueListener(
        loggingQueue, *originalHandlers, respect_handler_level=True
    )
    listener.start()


def setup_logger(logger_name: str = '', logger_config_path: str = LOG_CONFIG_FILE_DEFAULT):
    with open(logger_config_path) as logger_config_file:
        logger_config = json.load(logger_config_file)
    logging.config.dictConfig(logger_config)
    _setup_logging_queue(logger_name)
    logger = logging.getLogger(__name__)
    logger.info('Logger configured.')
