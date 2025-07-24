# Claude-Specific Development Guidelines

This file provides specific guidance for Claude Code (claude.ai/code) when working with this AI Code Assist Boilerplate repository.

## Project Context for Claude

This repository is an **AI Code Assist Boilerplate** - a template designed for setting up development environments optimized for AI-assisted coding. When working with this codebase, understand that:

1. **Template Nature**: This is meant to be cloned and customized, not used as-is
2. **AI-First Approach**: All patterns and structures are optimized for AI tool integration
3. **Cross-Platform**: Support for Windows, macOS, and Linux is essential
4. **Boilerplate Focus**: Prioritize flexibility and extensibility over specific functionality

## Claude-Specific Patterns

### Code Generation Guidelines

When generating code for this project:

1. **Follow Established Patterns**: Use existing code in `src/` and `tests/` as templates
2. **Maintain Type Safety**: All functions must have complete type hints
3. **Cross-Platform Compatibility**: Consider Windows, macOS, and Linux differences
4. **AI Tool Integration**: Code should work well with other AI assistants

### Documentation Best Practices

When updating documentation:
- **Keep template nature clear**: Remind users this is a boilerplate
- **Focus on AI integration**: Highlight features that benefit AI-assisted development
- **Maintain consistency**: Use established formatting and structure
- **Cross-reference appropriately**: Link related configurations and files

### Configuration Management

When working with configs:
- **Validate YAML syntax**: Ensure all YAML files are properly formatted
- **Document environment variables**: Clearly specify required `.env` entries
- **Maintain AI tool configs**: Keep `ai-tools.yaml` current with supported tools
- **Preserve examples**: Include example values but never real secrets

## Development Workflow for Claude

### Preferred Code Changes

1. **Start with tests**: Write failing tests first when implementing features
2. **Minimal, focused changes**: Make surgical modifications rather than large rewrites
3. **Preserve functionality**: Maintain existing behavior unless explicitly changing it
4. **Update documentation**: Keep docs in sync with code changes

### File Modification Priorities

When making changes, prioritize files in this order:
1. Core functionality in `src/`
2. Tests in `tests/`
3. Configuration files in `configs/`
4. Documentation files (README.md, etc.)
5. Scripts in `scripts/`

### Quality Assurance Steps

Before suggesting changes:
1. **Verify type hints**: Ensure all new code has proper typing
2. **Check cross-platform compatibility**: Consider path handling, commands, etc.
3. **Validate configurations**: Ensure YAML files are syntactically correct
4. **Test integration**: Consider how changes affect AI tool integration

## Repository-Specific Context

### Key Components

- **`init.py`**: Project initialization script - handles virtual environment and dependency setup
- **`scripts/Run-Python.psm1`**: Cross-platform Python execution module
- **`scripts/Get-ProviderModels.psm1`**: AI provider model fetching utility
- **`configs/ai-tools.yaml`**: Central AI tool configuration
- **`.github/copilot-instructions.md`**: GitHub Copilot specific instructions

### AI Integration Points

- **Environment Variables**: API keys stored in `.env` (use `.env.example` as template)
- **Model Configuration**: Provider-specific settings in `configs/`
- **Custom Instructions**: Tool-specific guidance in `.github/instructions/`
- **Command Patterns**: Claude-specific commands in `.claude/`

### Maintenance Considerations

- **Dependency Updates**: Use Poetry for Python dependencies
- **Documentation Sync**: Keep multiple docs consistent (README, CLAUDE.md, AGENTS.md)
- **Cross-Platform Testing**: PowerShell scripts must work on all platforms
- **Configuration Validation**: YAML files should have consistent structure

## Common Tasks for Claude

### Adding New AI Tool Support

1. Update `configs/ai-tools.yaml` with new tool configuration
2. Add environment variable documentation to `.env.example`
3. Create tool-specific instruction file in `.github/instructions/`
4. Update main documentation to mention the new tool
5. Test configuration loading and validation

### Implementing New Features

1. Create failing test in appropriate `tests/` subdirectory
2. Implement minimal code in `src/` to pass tests
3. Add comprehensive type hints and docstrings
4. Update relevant configuration files
5. Document the feature in appropriate README sections

### Debugging and Troubleshooting

1. Check virtual environment activation (`.venv/`)
2. Verify all dependencies installed (`poetry install`)
3. Run tests to identify specific failures (`pytest -v`)
4. Check configuration file syntax (YAML validation)
5. Verify environment variables are set correctly

## Integration with Other AI Tools

### GitHub Copilot Compatibility

- Follow patterns established in `.github/copilot-instructions.md`
- Use consistent naming and structure for better AI understanding
- Maintain clear, descriptive function and variable names
- Structure code in predictable, logical patterns

### Multi-AI Workflows

- Assume other AI tools may also work with this codebase
- Keep code self-documenting and well-structured
- Use configuration files rather than hardcoded values
- Maintain clear separation of concerns

---

**Remember**: This is a boilerplate project. Focus on creating patterns and structures that will be useful when this template is customized for specific use cases.