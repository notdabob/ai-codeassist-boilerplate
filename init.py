#!/usr/bin/env python3
"""Initialize AI Code Assist Boilerplate project."""

import sys
import subprocess
import platform
import shutil
from pathlib import Path
import argparse


class ProjectInitializer:
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.venv_name = ".venv"
        self.os_type = platform.system()

    def create_virtual_environment(self):
        """Create Python virtual environment."""
        print("📦 Creating virtual environment...")
        venv_path = self.project_root / self.venv_name

        if venv_path.exists():
            print(f"✅ Virtual environment already exists at " f"{venv_path}")
            return

        subprocess.run([sys.executable, "-m", "venv", str(venv_path)], check=True)
        print(f"✅ Virtual environment created at {venv_path}")

    def get_pip_command(self):
        """Get the correct pip command for the virtual environment."""
        if self.os_type == "Windows":
            return str(self.project_root / self.venv_name / "Scripts" / "pip")
        else:
            return str(self.project_root / self.venv_name / "bin" / "pip")

    def install_dependencies(self):
        """Install Python dependencies."""
        print("📥 Installing dependencies...")
        pip_cmd = self.get_pip_command()

        # Upgrade pip first
        subprocess.run([pip_cmd, "install", "--upgrade", "pip"], check=True)

        # Install requirements
        requirements_file = self.project_root / "requirements.txt"
        if requirements_file.exists():
            subprocess.run(
                [
                    pip_cmd,
                    "install",
                    "-r",
                    str(requirements_file),
                ],
                check=True,
            )
            print("✅ Dependencies installed successfully")
        else:
            print("⚠️  No requirements.txt found")

    def setup_environment_file(self):
        """Create .env file from .env.example."""
        print("🔧 Setting up environment file...")
        env_example = self.project_root / ".env.example"
        env_file = self.project_root / ".env"

        if env_file.exists():
            print("✅ .env file already exists")
            return

        if env_example.exists():
            shutil.copy(env_example, env_file)
            print("✅ Created .env file from .env.example")
            print("⚠️  Please update .env with your actual API keys")
        else:
            print("⚠️  No .env.example found")

    def create_project_directories(self):
        """Create essential project directories."""
        print("📁 Creating project directories...")
        directories = [
            "src",
            "tests",
            "scripts",
            "data",
            ".claude",
        ]

        for dir_name in directories:
            dir_path = self.project_root / dir_name
            dir_path.mkdir(exist_ok=True)

            # Create __init__.py for Python packages
            if dir_name in ["src", "tests"]:
                init_file = dir_path / "__init__.py"
                init_file.touch()

        print("✅ Project directories created")

    def setup_git_hooks(self):
        """Set up git pre-commit hooks."""
        print("🪝 Setting up git hooks...")
        pip_cmd = self.get_pip_command()

        try:
            subprocess.run([pip_cmd, "install", "pre-commit"], check=True)

            # Create pre-commit config
            pre_commit_config = self.project_root / ".pre-commit-config.yaml"
            if not pre_commit_config.exists():
                pre_commit_content = (
                    "repos:\n"
                    "  - repo: https://github.com/psf/black\n"
                    "    rev: 23.0.0\n"
                    "    hooks:\n"
                    "      - id: black\n"
                    "        language_version: python3\n"
                    "  - repo: https://github.com/pre-commit/mirrors-mypy\n"
                    "    rev: v1.5.0\n"
                    "    hooks:\n"
                    "      - id: mypy\n"
                    "        additional_dependencies: [types-requests]\n"
                )
                pre_commit_config.write_text(pre_commit_content)

            # Install pre-commit hooks
            if self.os_type == "Windows":
                pre_commit_cmd = str(
                    self.project_root / self.venv_name / "Scripts" / "pre-commit"
                )
            else:
                pre_commit_cmd = str(
                    self.project_root / self.venv_name / "bin" / "pre-commit"
                )

            subprocess.run([pre_commit_cmd, "install"], check=True)
            print("✅ Git hooks installed")
        except Exception as e:
            print(f"⚠️  Could not set up git hooks: {e}")

    def create_claude_config(self):
        """Create Claude configuration file."""
        print("🤖 Setting up Claude configuration...")
        claude_dir = self.project_root / ".claude"
        claude_config = claude_dir / "CLAUDE.md"

        if not claude_config.exists():
            claude_content = """# Project-specific Claude Configuration

## Project Overview
AI Code Assist Boilerplate - A foundation for AI-assisted development

## Key Technologies
- Python 3.7+
- PowerShell 7.0+
- Claude CLI
- Gemini CLI

## Development Guidelines
1. Follow PEP 8 for Python code
2. Use type hints for all functions
3. Write comprehensive docstrings
4. Maintain cross-platform compatibility

## Project Structure
- `/src` - Source code
- `/tests` - Test files
- `/scripts` - Utility scripts
- `/configs` - Configuration files
- `/docs` - Documentation

## Testing
Run tests with: `pytest`
Run with coverage: `pytest --cov=src`

## Code Quality
- Format: `black .`
- Lint: `flake8`
- Type check: `mypy src/`
"""
            claude_config.write_text(claude_content)
            print("✅ Claude configuration created")
        else:
            print("✅ Claude configuration already exists")

    def print_next_steps(self):
        """Print next steps for the user."""
        print("\n🎉 Project initialization complete!")
        print("\n📋 Next steps:")
        print("1. Update .env file with your API keys")

        if self.os_type == "Windows":
            print(
                f"2. Activate virtual environment: .\\{self.venv_name}\\Scripts\\activate"
            )
        else:
            print(
                f"2. Activate virtual environment: "
                f"source {self.venv_name}/bin/activate"
            )

        print("3. Run tests: pytest")
        print("4. Start developing! 🚀")

    def run(self):
        """Run the complete initialization process."""
        print("🚀 Initializing AI Code Assist Boilerplate...\n")

        try:
            self.create_virtual_environment()
            self.install_dependencies()
            self.setup_environment_file()
            self.create_project_directories()
            self.setup_git_hooks()
            self.create_claude_config()
            self.print_next_steps()
        except subprocess.CalledProcessError as e:
            print(f"\n❌ Error during initialization: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")
            sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Initialize AI Code Assist Boilerplate project"
    )
    parser.add_argument(
        "--skip-venv", action="store_true", help="Skip virtual environment creation"
    )
    parser.add_argument(
        "--skip-deps", action="store_true", help="Skip dependency installation"
    )
    args = parser.parse_args()

    initializer = ProjectInitializer()

    if not args.skip_venv and not args.skip_deps:
        initializer.run()
    else:
        print("⚠️  Partial initialization mode")
        if args.skip_venv:
            print("  - Skipping virtual environment creation")
        if args.skip_deps:
            print("  - Skipping dependency installation")
        print("\nRun without flags for complete initialization.")


if __name__ == "__main__":
    main()
