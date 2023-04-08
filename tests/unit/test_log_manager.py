"""
This file contains unit tests for log_manager.py
"""
# --- IMPORTS ---
import logging
import pytest
from src.logger.log_manager import setup_logger
# ---


def test_setup_logger_default_completion():
    success = False
    logging.basicConfig(force=True)
    try:
        setup_logger()
        success = True
    finally:
        assert success is True


@pytest.mark.parametrize("logger_config_path", [
    ('a_wrong_path'),
])
def test_setup_logger_config_path_completion(logger_config_path):
    success = False
    logging.basicConfig(force=True)
    try:
        setup_logger(logger_config_path=logger_config_path)
        success = True
    finally:
        assert success is True
