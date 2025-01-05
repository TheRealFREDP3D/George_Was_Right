from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# LLM parameters
llm_model_name = os.getenv('LLM_MODEL_NAME', 'ollama/Phi-3-mini-4k-instruct-q4:latest')
planning_llm_name = os.getenv('PLANNING_LLM_MODEL_NAME', 'ollama/Phi-3-mini-4k-instruct-q4:latest')
temperature_llm = float(os.getenv('TEMPERATURE_LLM', '0.7'))
temperature_planning_llm = float(os.getenv('TEMPERATURE_PLANNING_LLM', '0.1'))

# Search parameters
search_country = os.getenv('SEARCH_COUNTRY', 'us')
search_n_results = int(os.getenv('SEARCH_N_RESULTS', 5))

# A timestamp for the log files (filename-safe format)
TIMESTAMP = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# File paths for logs
log_researcher = f"./log/log_researcher-{TIMESTAMP}.md"
log_writer = f"./log/log_writer-{TIMESTAMP}.md"
log_prompt_master = f"./log/log_prompt_master-{TIMESTAMP}.md"
log_crew = f"./log/log_crew-{TIMESTAMP}.md"
