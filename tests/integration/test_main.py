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
async def test_api_up():
    """
        Verifies that the app API is up and running by checking the root call ("/")
    """
    async with AsyncClient(app=app, base_url=TEST_ADDITION_BASE_URL) as async_client:
        response = await async_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the root of test-pg-FastAPI."}
