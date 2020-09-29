# Demo for playwright-python

## Usage
Run tests with pytest

```
pytest
```

## Development
Ensure that pyenv is installed.

```sh
# Create a virtualenv
pyenv virtualenv 3.8.0 py-demo

# Activate the virtualenv
pyenv activate py-demo

# Install dependencies
pip install pytest playwright pytest-playwright
python -m playwright install

# Run the tests
pytest
```
