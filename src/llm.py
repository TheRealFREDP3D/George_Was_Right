import os
import logging
from dotenv import load_dotenv
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
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

load_dotenv()

class LLMFactory:
    @staticmethod
    def init_llm():
        """Initialize the main LLM with fallback support"""
        try:
            logger.info(f"Initializing LLM with model: {llm_model_name}")
            # First try the configured model (likely local Ollama)
            return LLM(
                model=llm_model_name, 
                base_url=os.getenv("OLLAMA_HOST", "http://0.0.0.0:11434"), 
                temperature=temperature_llm
            )
        except Exception as e:
            logger.warning(f"Error initializing primary LLM: {str(e)}")
            if use_fallback:
                logger.info(f"Using fallback LLM model: {fallback_llm_name}")
                # Fallback to OpenAI or another cloud provider
                return LLM(
                    model=fallback_llm_name,
                    temperature=temperature_llm
                )
            else:
                # Re-raise if fallback is disabled
                logger.error("Fallback is disabled, cannot proceed")
                raise

    @staticmethod
    def init_planning_llm():
        """Initialize the planning LLM with fallback support"""
        try:
            logger.info(f"Initializing planning LLM with model: {planning_llm_name}")
            return LLM(
                model=planning_llm_name,
                base_url=os.getenv("OLLAMA_HOST", "http://0.0.0.0:11434"), 
                temperature=temperature_planning_llm
            )
        except Exception as e:
            logger.warning(f"Error initializing planning LLM: {str(e)}")
            if use_fallback:
                logger.info(f"Using fallback LLM model for planning: {fallback_llm_name}")
                return LLM(
                    model=fallback_llm_name,
                    temperature=temperature_planning_llm
                )
            else:
                logger.error("Fallback is disabled, cannot proceed")
                raise
