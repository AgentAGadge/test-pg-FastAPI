"""
    This module manages the "addition" part of the app API.
"""
# --- IMPORTS ---
from enum import Enum
import logging
from tp_package.functions import add_one
import numpy
from fastapi import APIRouter
# ---

# --- CONSTANT DEFINITIONS ---
ADDITION_API_PATH = "/addition/"
# ---


# --- CLASSES ---
class AddoneMethod(str, Enum):
    """
        Enum of the available methods for the addone call.
    """
    PYTHON = "python"
    NUMPY = "numpy"
    TP_PACKAGE = "tp_package"
# ---


# --- Setup the FastAPI Router ---
logger = logging.getLogger(__name__)
router = APIRouter()
# ---


# --- API DEFINITION ---
@router.get(ADDITION_API_PATH+"addone/{addend}")
async def addone(addend: float, method: AddoneMethod = AddoneMethod.PYTHON):
    """
        Controller for the addone call.

        Inputs:
            - addend: Float value to which 1 should be added
            - method: Computation method
    """
    logger.info('API Call to /addition/addone/ with (addend=%s, method=%s)', addend, method)

    match method:
        case AddoneMethod.NUMPY:
            logger.info('Running addone with numpy...')
            result = numpy.add(addend, 1)
        case AddoneMethod.TP_PACKAGE:
            logger.info('Running addone with tp_package...')
            result = add_one(addend)
        case AddoneMethod.PYTHON:
            logger.info('Running addone with python...')
            result = addend+1

    logger.info('Returning API Call to /addition/addone/ with (sum=%s)', result)
    return {"sum": result}
# ------
