"""LLM Factory module for initializing language models.

This module provides a factory class for initializing language models
with appropriate configurations for the main application and planning.
"""

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
        """Initialize the main language model with configured parameters.

        Returns:
            LLM: Configured language model instance for main tasks.
        """
        return LLM(
            model=llm_model_name,
            temperature=temperature_llm
        )

    @staticmethod
    def init_planning_llm():
        """Initialize the planning language model with configured parameters.

        Returns:
            LLM: Configured language model instance for planning tasks.
        """
        return LLM(
            model=planning_llm_name,
            temperature=temperature_planning_llm
        )
