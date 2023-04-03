from fastapi import FastAPI
from enum import Enum
from tp_package.functions import add_one

import numpy


class AddoneMethod(str, Enum):
    python = "python"
    numpy = "numpy"
    tp_package = "tp_package"


app = FastAPI()


@app.get("/addone/{addend}")
async def addone(addend: float, method: AddoneMethod = AddoneMethod.python):
    match method:
        case AddoneMethod.numpy:
            sum = numpy.add(addend, 1)
        case AddoneMethod.tp_package:
            sum = add_one(addend)
        case AddoneMethod.python:
            sum = addend+1
    return {"sum": sum}
