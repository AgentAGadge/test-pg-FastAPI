"""
This file contains unit tests for addition/addition.py
"""


import pytest
from httpx import AsyncClient
from src.main import app


@pytest.mark.parametrize("addend, method, expected", [
    (0, "python", 1),
    (0, "numpy", 1),
    (0, "tp_package", 1),
    (-1, "tp_package", 0),
    (1.2, "python", 2.2),
    (1.2, "numpy", 2.2),
    (1.2, "tp_package", 2.2),
])
@pytest.mark.anyio
async def test_addone_success(addend, method, expected):
    async with AsyncClient(app=app, base_url="http://test/") as ac:
        response = await ac.get("/addition/addone/"+str(addend)+"?method="+str(method))
    assert response.status_code == 200
    assert response.json() == {"sum": expected}


@pytest.mark.parametrize("addend, method, expected", [
    (0, "unknown", 1),
    ("string", "python", 1),
    (complex(1, 1), "python", complex(2, 1))
])
@pytest.mark.anyio
async def test_addone_wrong_param(addend, method, expected):
    async with AsyncClient(app=app, base_url="http://test/") as ac:
        response = await ac.get("/addition/addone/"+str(addend)+"?method="+str(method))
    assert response.status_code == 422


@pytest.mark.parametrize("addend, method, expected", [
    (0, "python", 1),
])
@pytest.mark.anyio
async def test_addone_optional_param(addend, method, expected):
    async with AsyncClient(app=app, base_url="http://test/") as ac:
        response = await ac.get("/addition/addone/"+str(addend))
    assert response.status_code == 200
    assert response.json() == {"sum": expected}


@pytest.mark.parametrize("addend, method, expected", [
    (0, "python", 1),
])
@pytest.mark.anyio
async def test_addone_missing_param(addend, method, expected):
    async with AsyncClient(app=app, base_url="http://test/") as ac:
        response = await ac.get("/addition/addone/?method=python")
    assert response.status_code == 404
