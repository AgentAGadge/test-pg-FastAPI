"""
This file contains unit tests for main.py
"""


import pytest
from httpx import AsyncClient
from src.main import app


@pytest.mark.anyio
async def test_addone_success():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the root of test-pg-FastAPI."}
