---
applyTo: ["*.md", "docs/**/*.md", ".claude/**/*.md"]
---

# Documentation Instructions

## Documentation Standards

### Writing Style
- Write in clear, concise English
- Use active voice when possible
- Structure content with logical headings and subheadings
- Include practical examples and code snippets
- Keep paragraphs focused and not overly long

### Markdown Formatting
- Use consistent heading levels (start with # for main title, ## for sections)
- Use code blocks with appropriate language highlighting
- Include table of contents for longer documents
- Use bullet points and numbered lists for clarity
- Format code inline with backticks for short snippets

Example structure:
```markdown
# Document Title

Brief overview of what this document covers.

## Table of Contents
- [Section 1](#section-1)
- [Section 2](#section-2)
- [Examples](#examples)

## Section 1

Detailed explanation with examples.

### Subsection

More specific information.

```language
code example here
```

## Examples

Practical examples showing usage.
```

### Code Examples
- Always include working, tested code examples
- Explain what each example demonstrates
- Use realistic data and scenarios
- Include both success and error cases when relevant
- Keep examples focused and not overly complex

## Project-Specific Documentation

### README.md Guidelines
- Start with a clear project description
- Include quick start instructions
- Provide comprehensive setup instructions
- Document all major features and capabilities
- Include links to more detailed documentation

### Technical Documentation
- Document all public APIs and interfaces
- Include parameter descriptions and return values
- Provide usage examples for complex features
- Document configuration options and their effects
- Explain architectural decisions and patterns

### User Guides
- Write from the user's perspective
- Include step-by-step instructions
- Anticipate common questions and problems
- Provide troubleshooting guidance
- Use screenshots or diagrams when helpful

## AI Tool Integration Documentation

### Claude-Specific Documentation
Files in `.claude/` directory should:
- Follow the established command structure
- Include clear descriptions of what each command does
- Provide examples of usage scenarios
- Document any prerequisites or dependencies
- Explain expected outputs and results

### Cross-Platform Considerations
- Document platform-specific differences when they exist
- Provide alternative instructions for different operating systems
- Test documentation instructions on multiple platforms
- Use platform-neutral examples when possible

## Documentation Maintenance

### Regular Updates
- Review documentation when code changes
- Update examples to reflect current API versions
- Remove or update deprecated information
- Ensure all links are working and relevant
- Verify that installation instructions still work

### Quality Assurance
- Proofread for spelling and grammar errors
- Verify that all code examples actually work
- Check that all referenced files and commands exist
- Ensure consistency in terminology and formatting
- Test instructions from a fresh environment when possible

### Version Control
- Commit documentation changes with clear commit messages
- Review documentation changes as carefully as code changes
- Consider the impact of documentation changes on users
- Keep documentation in sync with code releases

## Special Documentation Types

### API Documentation
- Document all public functions and classes
- Include parameter types and return value types
- Provide usage examples for each major function
- Document error conditions and exceptions
- Explain the purpose and context of each API

### Configuration Documentation
- Document all configuration options clearly
- Explain the effect of each configuration setting
- Provide examples of common configuration scenarios
- Document default values and valid value ranges
- Explain relationships between different configuration options

### Troubleshooting Guides
- Start with the most common issues
- Provide step-by-step diagnostic procedures
- Include specific error messages and their solutions
- Explain how to gather debugging information
- Provide contact information or resources for additional help

## Style Guide

### Tone and Voice
- Professional but approachable
- Helpful and instructive
- Assume the reader is intelligent but may be unfamiliar with the specific technology
- Avoid jargon without explanation
- Be encouraging and supportive

### Technical Accuracy
- All technical information must be accurate and current
- Test all procedures and examples
- Use precise terminology consistently
- Reference official sources when appropriate
- Acknowledge limitations and known issues

### Accessibility
- Use descriptive link text (not "click here")
- Provide alternative text for images
- Structure content with proper headings for screen readers
- Use sufficient color contrast in any diagrams
- Keep language clear and avoid unnecessary complexity

## Templates and Patterns

### Command Documentation Template
```markdown
## Command Name

Brief description of what the command does.

### Usage
```
command-syntax [options] arguments
```

### Parameters
- `parameter1`: Description of parameter
- `parameter2`: Description of parameter (optional)

### Examples
```
# Basic usage
command-example

# Advanced usage
command-example --option value
```

### Output
Description of expected output or results.
```

### Configuration Section Template
```markdown
### Configuration Section

Brief description of this configuration section.

#### Options
- `option_name` (type, default): Description of what this option controls
- `another_option` (type, required): Description of required option

#### Example
```yaml
section_name:
  option_name: value
  another_option: required_value
```
```

### Integration with AI Coding
- Write documentation that AI tools can easily parse and understand
- Use consistent patterns that AI can learn and replicate
- Include comprehensive context in each document
- Structure information in predictable ways
- Provide clear examples that demonstrate proper usage patterns