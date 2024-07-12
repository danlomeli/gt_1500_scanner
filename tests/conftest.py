"""
conftest.py: Configuration file for pytest.

This module contains pytest fixtures and hooks used for testing the application.
It defines reusable fixtures that can be accessed across multiple test files and
provides setup and teardown logic for the testing environment.

Usage:
    pytest tests/
"""

import pytest


@pytest.fixture
def sample_data():
    """
    Fixture that provides sample data for testing.

    This fixture returns a dictionary containing sample data that can be used in
    various test cases. The data can be customized based on the specific testing
    requirements of the application.

    Returns:
        dict: A dictionary containing sample data for testing.
    """
    return {"key": "value"}
