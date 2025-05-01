import os
# Removed redundant load_dotenv import - environment variables are loaded in config.py
from crewai import LLM
from src.config import (
    llm_model_name,
    planning_llm_name,
    temperature_llm,
    temperature_planning_llm,
)

# Removed redundant load_dotenv() call

class LLMFactory:
    @staticmethod
    def init_llm():
        return LLM(
            model=llm_model_name,
            # base_url=os.getenv("OLLAMA_HOST", "http://localhost:11434"),
            temperature=temperature_llm
        )

    @staticmethod
    def init_planning_llm():
        return LLM(
            model=planning_llm_name,
            # base_url=os.getenv("OLLAMA_HOST", "http://localhost:11434"),
            temperature=temperature_planning_llm
        )
