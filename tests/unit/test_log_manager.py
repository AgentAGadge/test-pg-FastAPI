"""
This file contains unit tests for log_manager.py
"""
# --- IMPORTS ---
import logging
import pytest
from src.logger.log_manager import setup_logger_with_async
# ---


@pytest.mark.parametrize("logger_config_path", [
    (None),
    ('a_wrong_path'),
])
def test_setup_logger_with_async_default_completion(logger_config_path):
    """
        Checks that setup_logger_with_async runs successfully with various configurations.
    """
    success = False
    logging.basicConfig(force=True)
    try:
        if logger_config_path is None:
            setup_logger_with_async()
        else:
            setup_logger_with_async(logger_config_path)
        success = True
    finally:
        assert success is True
