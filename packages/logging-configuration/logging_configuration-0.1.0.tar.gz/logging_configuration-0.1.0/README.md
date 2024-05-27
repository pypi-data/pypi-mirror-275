# Logging Config

A simple logging configuration module for Python projects. This package provides a convenient way to set up and manage logging across multiple projects.  I mostly created the package because of frustration with manually adding the file across projects.

## Features

- Dynamic filename support for log files
- Rotating log files with daily rotation and backup retention
- Customizable logging levels via environment variables

## Installation

Install the package using pip:

```bash
pip install logging_config
```

## Usage

### Basic Usage
To use the logging configuration in your project, import the setup_logging function from the configuration module and call it with the desired log filename.

```python
from custom_logging.configuration import setup_logging

# Set up logging with a custom log filename
setup_logging('my_custom_log')

# Set up logging with the default log filename of "app_log"
setup_logging()

```

## Environment Variabls
You can set the logging level using an environment variable. By default, the logging level is set to INFO. To change it, set the `LOGGING_LEVEL` environment variable to one of the valid logging levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).

Example (in a .env file):

```makefile
LOGGING_LEVEL=DEBUG
```


## Configuration
The setup_logging function in the configuration.py module is responsible for setting up the logging configuration. It supports dynamic log filenames and uses the TimedRotatingFileHandler to create new log files every midnight and keep the last 30 days of log files.


## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
I mostly use this for personal use, and am a super amateur programmer.  Contributions are welcome, but I'm pretty sure you have better things to do with your time!
