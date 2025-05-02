
"""
Utility functions for the George_Was_Right project.
"""

import os
import logging
from datetime import datetime

def ensure_directory_exists(directory):
    """Ensure that a directory exists, creating it if necessary."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        return True
    return False

def setup_logging(log_file=None, level=logging.INFO):
    """Set up logging for the application."""
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    # Configure root logger
    logging.basicConfig(
        level=level,
        format=log_format
    )
    
    # Add file handler if a log file is specified
    if log_file:
        ensure_directory_exists(os.path.dirname(log_file))
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter(log_format))
        
        # Get the root logger and add the file handler
        root_logger = logging.getLogger()
        root_logger.addHandler(file_handler)
    
    return logging.getLogger()

def get_timestamp():
    """Get a filename-safe timestamp."""
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def print_banner(title, width=50):
    """Print a nicely formatted banner with the given title."""
    border = "=" * width
    padding = (width - len(title)) // 2
    title_line = " " * padding + title + " " * (width - padding - len(title))
    
    print("\n" + border)
    print(title_line)
    print(border + "\n")
