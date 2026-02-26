# AGENTS.md - Development Guidelines for mineGPT

## Project Overview

This is a Python/Jupyter notebook project focused on LLM/AI experimentation. The project consists of Jupyter notebooks (`.ipynb` files) and Python modules.

## Build, Lint, and Test Commands

### Environment Setup
```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt
```

### Running Notebooks
```bash
# Launch Jupyter Lab
jupyter lab

# Launch Jupyter Notebook
jupyter notebook

# Run notebook programmatically (for automation)
jupyter nbconvert --to notebook --execute 1_about_llm.ipynb
```

### Linting and Code Quality
```bash
# Run flake8 on Python files
flake8 .

# Run flake8 with custom config
flake8 --max-line-length=100 --ignore=E203,W503 .

# Run ruff linter
ruff check .

# Run ruff with auto-fix
ruff check --fix .

# Run isort for import sorting
isort .

# Run black for formatting
black .

# Run all linters
pylint **/*.py
```

### Testing
```bash
# Run pytest on entire project
pytest

# Run a specific test file
pytest tests/test_file.py

# Run a single test function
pytest tests/test_file.py::test_function_name

# Run tests matching a pattern
pytest -k "test_pattern"

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=. --cov-report=html

# Run tests in a specific directory
pytest tests/
```

### Jupyter-Specific Commands
```bash
# Clear all notebook outputs
jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace *.ipynb

# Convert notebook to Python script
jupyter nbconvert --to python 1_about_llm.ipynb

# Check notebook for errors (lint)
jupyter nbconvert --to python --execute 1_about_llm.ipynb

# Install Jupyter kernel for virtual environment
python -m ipykernel install --user --name=mineGPT
```

## Code Style Guidelines

### General Principles
- Write clean, readable, and maintainable code
- Follow PEP 8 style guide for Python code
- Keep functions and methods focused on a single responsibility
- Use meaningful variable and function names
- Add docstrings to all public functions and classes

### Naming Conventions
- **Variables**: `snake_case` (e.g., `user_name`, `max_iterations`)
- **Functions**: `snake_case` (e.g., `calculate_loss`, `load_model`)
- **Classes**: `PascalCase` (e.g., `DataProcessor`, `LLMClassifier`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_TOKEN_LENGTH`, `DEFAULT_TEMPERATURE`)
- **Files**: `snake_case` (e.g., `data_loader.py`, `model_utils.py`)
- **Notebooks**: `snake_case` with descriptive names (e.g., `1_about_llm.ipynb`)

### Import Guidelines
```python
# Standard library imports first
import os
import sys
import json
from typing import List, Dict, Optional, Any

# Third-party imports second
import numpy as np
import pandas as pd
import torch
from transformers import AutoModel, AutoTokenizer

# Local imports last
from .utils import helper_function
from .models import base_model

# Avoid wildcard imports
from module import *  # BAD

# Use absolute imports
from package.module import function  # GOOD
```

### Formatting
- **Line length**: Maximum 100 characters (configurable)
- **Indentation**: 4 spaces (no tabs)
- **Blank lines**: Two blank lines between top-level definitions
- **Trailing whitespace**: Never leave trailing whitespace
- **Black** formatter is recommended for automatic formatting

### Type Hints
```python
# Always use type hints for function signatures
def process_data(data: List[Dict[str, Any]], config: Dict[str, int]) -> pd.DataFrame:
    """Process input data and return a DataFrame.
    
    Args:
        data: List of dictionaries containing raw data.
        config: Configuration dictionary with processing parameters.
        
    Returns:
        Processed DataFrame ready for modeling.
    """
    pass

# Use Optional for nullable types
def get_model(path: Optional[str] = None) -> Optional[torch.nn.Module]:
    if path is None:
        return None
    return torch.load(path)

# Use Union for multiple types
def parse_value(value: str) -> Union[int, float, str]:
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value
```

### Error Handling
```python
# Use specific exception types
try:
    result = dangerous_operation()
except ValueError as e:
    logger.error(f"Invalid value: {e}")
    raise CustomError("Operation failed") from e
except (ConnectionError, TimeoutError) as e:
    logger.warning(f"Network issue: {e}")
    return default_value

# Always log errors before re-raising
except Exception as e:
    logger.exception("Unexpected error occurred")
    raise

# Use context managers for resource management
with open('data.txt', 'r') as f:
    content = f.read()
# File automatically closed
```

### Jupyter Notebook Guidelines
- Clear all outputs before committing notebooks
- Add titles and descriptions to markdown cells
- Use meaningful variable names in cells
- Keep cells focused and modular
- Add comments in code cells for complex operations
- Restart kernel and run all cells before committing
- Use `print()` statements sparingly; use `display()` for rich output

### Documentation
- Use Google-style docstrings:
```python
def function(param1: int, param2: str = "default") -> bool:
    """Short one-line description.

    Longer description if needed.

    Args:
        param1: Description of param1.
        param2: Description of param2. Defaults to "default".

    Returns:
        Description of return value.

    Raises:
        ValueError: When param1 is negative.
        TypeError: When param2 is not a string.
    """
```

### Testing Guidelines
- Write tests using `pytest`
- Test file naming: `test_<module_name>.py`
- Test function naming: `test_<function_name>_<scenario>`
- Use descriptive assertion messages
- Mock external dependencies (API calls, file I/O)
- Aim for high test coverage on business logic
- Include both unit tests and integration tests

### Version Control
- Commit messages should be clear and descriptive
- Use conventional commit format: `type(scope): description`
- Never commit secrets, API keys, or credentials
- Add `.ipynb_checkpoints/` to `.gitignore`
- Use `.env` files for local environment variables

### File Organization
```
project/
├── notebooks/           # Jupyter notebooks
│   └── *.ipynb
├── src/               # Python source code
│   ├── __init__.py
│   ├── models/
│   ├── utils/
│   └── data/
├── tests/             # Test files
│   └── test_*.py
├── requirements.txt   # Dependencies
├── setup.py          # Package configuration
└── .env              # Environment variables (not committed)
```

## Dependencies

Core dependencies typically include:
- `numpy` - Numerical computing
- `pandas` - Data manipulation
- `torch` - Deep learning
- `transformers` - Hugging Face transformers
- `jupyter` - Notebook interface
- `pytest` - Testing framework

Install with: `pip install numpy pandas torch transformers jupyter pytest`
