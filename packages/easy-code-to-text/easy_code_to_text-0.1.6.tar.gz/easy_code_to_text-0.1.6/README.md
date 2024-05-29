
# easy_code_to_text Project

A Python package to concatenate code files into a single document, with support for multiple programming languages and customizable ignore patterns.

## Features

- Support for multiple programming languages including Python, JavaScript, HTML, CSS, Java, and YAML.
- Customizable ignore patterns to exclude specific files or directories.
- Generates a single document with clear demarcation for each file's path and language.

## Installation

The package can be installed via pip:

```
pip install easy-code-to-text
```

## Configuration

### Ignore File

Create an ignore file (e.g., `.codeToTextIgnore`) in your project root with patterns to ignore, example:

```
# Your environment files
.venv

# Your private files
.env

# Python cache and logs files
__pycache__
*.log

# Your output and ignore file
my_project_output.txt
.codeToTextIgnore
```

## Usage

After installation, you can use the package as follows:

```py
from code_to_text.code_to_text import read_and_combine_files

read_and_combine_files(input_directory='your_code_directory',
                       output_file='your_output_file.txt',
                       ignore_file_path='your_ignore_file.txt')
```

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for each feature or improvement.
3. Submit a pull request with a comprehensive description of changes.

## License

This project is open source and available under the MIT License. Benjamin QUINET.