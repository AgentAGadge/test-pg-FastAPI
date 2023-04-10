"""
    Main file of the test-pg-fastAPI app.
    - Set up the app logger
    - Starts the FastAPI app
    - Registers the API routers:
        - addition
"""
import logging
from fastapi import FastAPI
from src.logger import log_manager
from src.api.addition import addition


# --- LOGGING ---
log_manager.setup_logger_with_async()
logger = logging.getLogger(__name__)
logger.info('Logger available.')
# --- END OF: LOGGING ---

# --- Start FastAPI ---
logger.info('Starting FastAPI app...')
app = FastAPI()
logger.info('Started FastAPI app.')
# -------

# ------- FastAPI Routers ---
logger.info('Adding addition router...')
app.include_router(addition.router)
logger.info('All routers added.')
# -------


@app.get("/")
async def root():
    """
        Root controller of the app.
        Just displays a message for debug and monitoring purposes.
    """
    return {"message": "Welcome to the root of test-pg-FastAPI."}
