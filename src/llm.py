import os
from dotenv import load_dotenv
from crewai import LLM
from src.config import (
    llm_model_name,
    planning_llm_name,
    temperature_llm,
    temperature_planning_llm,
)

load_dotenv()

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
