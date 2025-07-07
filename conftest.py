"""Pytest configuration and fixtures."""

import pytest
import tempfile
from pathlib import Path


@pytest.fixture
def temp_project_dir():
    """Create a temporary directory for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def mock_project_files(temp_project_dir):
    """Create mock project files in temporary directory."""
    # Create requirements.txt
    requirements = temp_project_dir / "requirements.txt"
    requirements.write_text("requests>=2.28.1\npytest>=7.4.0\n")

    # Create .env.example
    env_example = temp_project_dir / ".env.example"
    env_example.write_text("API_KEY=your_key_here\n")

    # Create configs directory
    configs_dir = temp_project_dir / "configs"
    configs_dir.mkdir()

    return temp_project_dir


@pytest.fixture(autouse=True)
def cleanup_test_artifacts():
    """Clean up any test artifacts after each test."""
    yield
    # Cleanup logic here if needed
    pass
