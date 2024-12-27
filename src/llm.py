from crewai import LLM
from src.config import (
    llm_model_name,
    planning_llm_name,
    temperature_llm,
    temperature_planning_llm,
)


class LLMFactory:
    @staticmethod
    def init_llm():
        return LLM(model=llm_model_name, temperature=temperature_llm)

    @staticmethod
    def init_planning_llm():
        return LLM(
            model=planning_llm_name,
            temperature=temperature_planning_llm
        )
