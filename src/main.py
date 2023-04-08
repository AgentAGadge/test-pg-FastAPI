from fastapi import FastAPI
from enum import Enum
from tp_package.functions import add_one
import logging
import logging.config
import numpy
from queue import SimpleQueue as Queue
from typing import List
import asyncio
import json


class AddoneMethod(str, Enum):
    python = "python"
    numpy = "numpy"
    tp_package = "tp_package"


# --- LOGGING ---
LOG_CONFIG_FILE = "config/logger_config.json"


class LocalQueueHandler(logging.handlers.QueueHandler):
    def emit(self, record: logging.LogRecord) -> None:
        # Removed the call to self.prepare(), handle task cancellation
        try:
            self.enqueue(record)
        except asyncio.CancelledError:
            raise
        except Exception:
            self.handleError(record)


def setup_logging_queue() -> None:
    """Move log handlers to a separate thread.

    Replace handlers on the root logger with a LocalQueueHandler,
    and start a logging.QueueListener holding the original
    handlers.

    """
    loggingQueue = Queue()
    queueHandler = LocalQueueHandler(loggingQueue)

    originalHandlers: List[logging.Handler] = []

    rootLogger = logging.getLogger()
    rootLogger.addHandler(queueHandler)
    for h in rootLogger.handlers[:]:
        if h is not queueHandler:
            rootLogger.removeHandler(h)
            originalHandlers.append(h)

    listener = logging.handlers.QueueListener(
        loggingQueue, *originalHandlers, respect_handler_level=True
    )
    listener.start()


with open(LOG_CONFIG_FILE) as logger_config_file:
    logger_config = json.load(logger_config_file)
logging.config.dictConfig(logger_config)
setup_logging_queue()

logger = logging.getLogger(__name__)
logger.info('Logger configured.')
# --- END OF: LOGGING ---

# --- Start FastAPI ---
logger.info('Starting FastAPI app...')
app = FastAPI()
logger.info('Started FastAPI app.')
# -------

# --- API DEFINITION ---


@app.get("/addone/{addend}")
async def addone(addend: float, method: AddoneMethod = AddoneMethod.python):
    logger.info('API Call to /addone/ with (addend=%s, method=%s)', addend, method)

    match method:
        case AddoneMethod.numpy:
            logger.info('Running addone with numpy...')
            sum = numpy.add(addend, 1)
        case AddoneMethod.tp_package:
            logger.info('Running addone with tp_package...')
            sum = add_one(addend)
        case AddoneMethod.python:
            logger.info('Running addone with python...')
            sum = addend+1

    logger.info('Returning API Call to /addone/ with (sum=%s)', sum)
    return {"sum": sum}
# ------
