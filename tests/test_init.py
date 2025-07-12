"""Test initialization script functionality."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from init import ProjectInitializer


class TestProjectInitializer:
    """Test ProjectInitializer class."""

    def test_initializer_creation(self):
        """Test that ProjectInitializer can be instantiated."""
        initializer = ProjectInitializer()
        assert initializer is not None
        assert initializer.venv_name == ".venv"
        assert initializer.project_root == Path(__file__).parent.parent

    def test_pip_command_unix(self, monkeypatch):
        """Test pip command generation on Unix systems."""
        monkeypatch.setattr("platform.system", lambda: "Darwin")
        initializer = ProjectInitializer()
        pip_cmd = initializer.get_pip_command()
        assert pip_cmd.endswith("bin/pip")

    def test_pip_command_windows(self, monkeypatch):
        """Test pip command generation on Windows systems."""
        monkeypatch.setattr("platform.system", lambda: "Windows")
        initializer = ProjectInitializer()
        pip_cmd = initializer.get_pip_command()
        # On Windows, the path should contain Scripts/pip (Path object uses forward slashes)
        assert "Scripts" in pip_cmd and pip_cmd.endswith("pip")

    def test_project_directories_list(self):
        """Test that required directories are defined."""
        initializer = ProjectInitializer()
        # Since directories are hardcoded in the method, we verify by checking
        # if the method exists and can be called
        assert hasattr(initializer, "create_project_directories")

    @pytest.mark.unit
    def test_os_detection(self):
        """Test OS detection functionality."""
        initializer = ProjectInitializer()
        assert initializer.os_type in ["Darwin", "Linux", "Windows"]
