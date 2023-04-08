# --- IMPORTS ---
from enum import Enum
from tp_package.functions import add_one
import numpy
from fastapi import APIRouter
import logging
# ---


# --- CLASSES ---
class AddoneMethod(str, Enum):
    python = "python"
    numpy = "numpy"
    tp_package = "tp_package"
# ---


# --- Setup the FastAPI Router ---
logger = logging.getLogger(__name__)
router = APIRouter()
# ---


# --- API DEFINITION ---
@router.get("/addition/addone/{addend}")
async def addone(addend: float, method: AddoneMethod = AddoneMethod.python):
    logger.info('API Call to /addition/addone/ with (addend=%s, method=%s)', addend, method)

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

    logger.info('Returning API Call to /addition/addone/ with (sum=%s)', sum)
    return {"sum": sum}
# ------
