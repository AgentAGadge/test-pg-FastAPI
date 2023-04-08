"""
This file contains unit tests for main.py
"""
# --- IMPORTS ---
import pytest
from httpx import AsyncClient
from src.main import app
# ---

# --- CONSTANT DEFINITIONS ---
TEST_ADDITION_BASE_URL = "http://test/"
# ---


@pytest.mark.anyio
async def test_addone_success():
    async with AsyncClient(app=app, base_url=TEST_ADDITION_BASE_URL) as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the root of test-pg-FastAPI."}
