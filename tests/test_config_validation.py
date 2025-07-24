"""Tests for configuration file validation."""

import pytest
import yaml
from pathlib import Path
from typing import Dict, Any


class TestConfigurationFiles:
    """Test suite for YAML configuration files."""

    def test_ai_tools_config_valid_yaml(self) -> None:
        """Test that ai-tools.yaml is valid YAML."""
        config_path = Path("configs/ai-tools.yaml")
        assert config_path.exists(), "ai-tools.yaml configuration file not found"

        with open(config_path, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)

        assert isinstance(config, dict), "Configuration should be a dictionary"
        assert "ai_tools" in config, "Configuration should have ai_tools section"

    def test_ai_tools_structure(self) -> None:
        """Test that ai-tools.yaml has expected structure."""
        config_path = Path("configs/ai-tools.yaml")
        with open(config_path, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)

        ai_tools = config["ai_tools"]
        assert isinstance(ai_tools, dict), "ai_tools should be a dictionary"

        # Check that expected providers exist
        expected_providers = ["anthropic", "google", "github"]
        for provider in expected_providers:
            assert provider in ai_tools, f"Provider {provider} should be in ai_tools"

            provider_config = ai_tools[provider]
            assert "name" in provider_config, f"Provider {provider} should have name"
            assert (
                "description" in provider_config
            ), f"Provider {provider} should have description"

    def test_code_stack_config_valid_yaml(self) -> None:
        """Test that code-stack.yaml is valid YAML."""
        config_path = Path("configs/code-stack.yaml")
        assert config_path.exists(), "code-stack.yaml configuration file not found"

        with open(config_path, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)

        assert isinstance(config, dict), "Configuration should be a dictionary"
        assert "code_stack" in config, "Configuration should have code_stack section"

    def test_code_stack_structure(self) -> None:
        """Test that code-stack.yaml has expected structure."""
        config_path = Path("configs/code-stack.yaml")
        with open(config_path, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)

        code_stack = config["code_stack"]
        assert isinstance(code_stack, dict), "code_stack should be a dictionary"

        # Check that expected sections exist
        expected_sections = [
            "programming_languages",
            "python_libraries",
            "development_tools",
        ]
        for section in expected_sections:
            assert section in code_stack, f"Section {section} should be in code_stack"

    def test_superclaude_config_valid_yaml(self) -> None:
        """Test that superclaude.yaml is valid YAML."""
        config_path = Path("configs/superclaude.yaml")
        assert config_path.exists(), "superclaude.yaml configuration file not found"

        with open(config_path, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)

        assert isinstance(config, dict), "Configuration should be a dictionary"

    @pytest.mark.parametrize(
        "config_file",
        [
            "ai-tools.yaml",
            "code-stack.yaml",
            "superclaude.yaml",
            "ide-tools.yaml",
            "os-support.yaml",
        ],
    )
    def test_all_configs_are_valid_yaml(self, config_file: str) -> None:
        """Test that all configuration files are valid YAML."""
        config_path = Path("configs") / config_file
        if not config_path.exists():
            pytest.skip(f"Configuration file {config_file} does not exist")

        with open(config_path, "r", encoding="utf-8") as file:
            try:
                config = yaml.safe_load(file)
                assert (
                    config is not None
                ), f"Configuration file {config_file} should not be empty"
            except yaml.YAMLError as e:
                pytest.fail(
                    f"Configuration file {config_file} contains invalid YAML: {e}"
                )

    def test_env_example_exists(self) -> None:
        """Test that .env.example file exists."""
        env_example = Path(".env.example")
        assert env_example.exists(), ".env.example file should exist"

        # Check that it contains expected environment variables
        content = env_example.read_text(encoding="utf-8")
        expected_vars = ["CLAUDE_API_KEY", "GEMINI_API_KEY"]

        for var in expected_vars:
            assert (
                var in content
            ), f"Environment variable {var} should be documented in .env.example"


class TestConfigurationLoadingUtils:
    """Test utility functions for configuration loading."""

    def test_config_directory_exists(self) -> None:
        """Test that configs directory exists."""
        configs_dir = Path("configs")
        assert configs_dir.exists(), "configs directory should exist"
        assert configs_dir.is_dir(), "configs should be a directory"

    def test_config_files_have_yaml_extension(self) -> None:
        """Test that all config files have .yaml extension."""
        configs_dir = Path("configs")
        config_files = list(configs_dir.glob("*"))

        for config_file in config_files:
            if config_file.is_file():
                assert config_file.suffix in [
                    ".yaml",
                    ".yml",
                ], f"Configuration file {config_file.name} should have .yaml or .yml extension"
