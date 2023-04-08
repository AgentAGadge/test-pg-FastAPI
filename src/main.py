from fastapi import FastAPI
import src.logger.log_manager as log_manager
import src.addition.addition as addition
import logging


# --- LOGGING ---
log_manager.setup_logger(__name__)
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
    return {"message": "Welcome to the root of test-pg-FastAPI."}
