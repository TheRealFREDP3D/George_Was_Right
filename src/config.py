from datetime import datetime
import os

# Configuration variables

# LLM Models

# Check LiteLLM supported providers for the LLMs name formatting.
# For most of them, the format is "<provider>/<model_name>"
# Use crewai.LLM to initialize the LLM.
# Ex: llm = LLM(model="ollama/llama3.1")

# GLHF -----------------------------------------------------------------
# GLHF: need to mock an OpenAI model and add "hf:" before the model name

# Set OPENAI_API_KEY to your GLHF API key.
# Set OPENAI_BASE_URL to your GLHF base URL.
# Set OPENAI_MODEL_NAME to the model name you want to use.
# (Ex: openai/hf:Qwen2.5-72B-Instruct)

from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# LLM Models
llm_model_name = os.getenv(
    "LLM_MODEL_NAME", "openai/hf:meta-llama/Llama-3.1-405B-Instruct"
)
planning_llm_name = os.getenv(
    "PLANNING_LLM_NAME", "openai/hf:meta-llama/Llama-3.1-405B-Instruct"
)

# Temperature settings
temperature_llm = 0.7
temperature_planning_llm = 0.3

# Search parameters
search_country = "ca"
search_n_results = 5

# A timestamp for the log files (filename-safe format)
TIMESTAMP = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# File paths for logs
log_researcher = f"./log/log_researcher-{TIMESTAMP}.md"
log_writer = f"./log/log_writer.md-{TIMESTAMP}"
log_prompt_master = f"./log/log_prompt_master-{TIMESTAMP}.md"
log_crew = f"./log/log_crew-{TIMESTAMP}.md"
