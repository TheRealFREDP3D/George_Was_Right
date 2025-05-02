"""Configuration module for the George_Was_Right project.

This module loads environment variables and defines configuration parameters
for the project. It is the central place for all configuration settings.
"""

from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file - centralized here
# This is the ONLY place where load_dotenv() should be called
load_dotenv()

# LLM parameters
llm_model_name = os.getenv('LLM_MODEL_NAME', 'ollama/Phi-3-mini-4k-instruct-q4:latest')
planning_llm_name = os.getenv('PLANNING_LLM_MODEL_NAME', 'ollama/Phi-3-mini-4k-instruct-q4:latest')
fallback_llm_name = os.getenv('FALLBACK_LLM_NAME', 'gpt-3.5-turbo')  # Add fallback model
temperature_llm = float(os.getenv('TEMPERATURE_LLM', '0.7'))
temperature_planning_llm = float(os.getenv('TEMPERATURE_PLANNING_LLM', '0.1'))

# Flag to enable/disable fallback to OpenAI if local model fails
use_fallback = os.getenv('USE_FALLBACK', 'True').lower() in ('true', '1', 't')

# Search parameters
search_country = os.getenv('SEARCH_COUNTRY', 'us')
<<<<<<< HEAD
search_n_results = int(os.getenv('SEARCH_N_RESULTS', '5'))
=======

# Validate configuration
def validate_config():
    """Validate the configuration settings."""
    issues = []

    # Check if LLM model names are set
    if not llm_model_name:
        issues.append("LLM_MODEL_NAME is not set")

    if not planning_llm_name:
        issues.append("PLANNING_LLM_MODEL_NAME is not set")

    # Check for valid temperature values
    if not (0 <= temperature_llm <= 1):
        issues.append(f"Invalid TEMPERATURE_LLM value: {temperature_llm} (should be between 0 and 1)")

    if not (0 <= temperature_planning_llm <= 1):
        issues.append(f"Invalid TEMPERATURE_PLANNING_LLM value: {temperature_planning_llm} (should be between 0 and 1)")

    return issues

# Run validation
config_issues = validate_config()
if config_issues:
    print("Configuration issues detected:")
    for issue in config_issues:
        print(f" - {issue}")
    print("Please fix these issues in your .env file.")

search_n_results = int(os.getenv('SEARCH_N_RESULTS', 5))
>>>>>>> 7250bbcd3257d20c5709e98c48bb63bfabf03032

# A timestamp for the log files (filename-safe format)
TIMESTAMP = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Ensure log directory exists
log_directory = "./log"
os.makedirs(log_directory, exist_ok=True)

# File paths for logs
<<<<<<< HEAD
log_researcher = f"{log_directory}/log_researcher-{TIMESTAMP}.md"
log_writer = f"{log_directory}/log_writer-{TIMESTAMP}.md"
log_prompt_master = f"{log_directory}/log_prompt_master-{TIMESTAMP}.md"
log_crew = f"{log_directory}/log_crew-{TIMESTAMP}.md"
=======
log_researcher = f"./log/log_researcher-{TIMESTAMP}.md"
log_writer = f"./log/log_writer-{TIMESTAMP}.md"
log_prompt_master = f"./log/log_prompt_master-{TIMESTAMP}.md"
log_editor = f"./log/log_editor-{TIMESTAMP}.md" #Added editor log file
log_crew = f"./log/log_crew-{TIMESTAMP}.md"
>>>>>>> 7250bbcd3257d20c5709e98c48bb63bfabf03032
