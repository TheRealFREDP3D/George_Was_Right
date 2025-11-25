"""LLM Factory module for initializing language models.

This module provides a factory class for initializing language models
with appropriate configurations for the main application and planning.
"""

import os
import logging
from crewai import LLM
from src.config import (
    llm_model_name,
    planning_llm_name,
    fallback_llm_name,
    temperature_llm,
    temperature_planning_llm,
    use_fallback,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Environment variables are loaded in config.py

class LLMFactory:
    """Factory class to create LLM instances based on configuration."""

    @staticmethod
    def init_llm():
        """Initialize the main LLM instance based on configuration."""
        try:
            return LLM(
                model=llm_model_name, 
                temperature=temperature_llm
                )
        except Exception as e:
            logger.error(
                f"Failed to initialize main LLM {llm_model_name}: {str(e)}")
            if use_fallback:
                logger.info(
                    f"Attempting to use fallback LLM: {fallback_llm_name}")
                return LLM(
                    model=fallback_llm_name, 
                    temperature=temperature_llm
                    )
            raise

    @staticmethod
    def init_planning_llm():
        """Initialize the planning LLM instance based on configuration."""
        try:
            return LLM(model=planning_llm_name,
                       temperature=temperature_planning_llm)
        except Exception as e:
            logger.error(
                f"Failed to initialize planning LLM {planning_llm_name}: {str(e)}"
            )
            if use_fallback:
                logger.info(
                    f"Attempting to use fallback LLM for planning: {fallback_llm_name}"
                )
                return LLM(model=fallback_llm_name,
                           temperature=temperature_planning_llm)
            raise
