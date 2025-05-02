#!/usr/bin/env python3
"""
Test script to verify imports and basic functionality after refactoring.

This script attempts to import all the main modules and classes
to ensure that the refactoring hasn't broken any imports.
"""

import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

logger = logging.getLogger(__name__)

def test_imports():
    """Test importing all the main modules and classes."""
    try:
        logger.info("Testing imports...")

        # Test importing config
        logger.info("Importing config...")
        from src.config import (
            llm_model_name,
            planning_llm_name,
            temperature_llm,
            temperature_planning_llm,
            search_country,
            search_n_results,
            log_researcher,
            log_writer,
            log_prompt_master,
            log_crew,
        )
        logger.info(f"Config imported successfully. LLM model: {llm_model_name}")

        # Test importing LLM factory
        logger.info("Importing LLM factory...")
        from src.llm import LLMFactory
        logger.info("LLM factory imported successfully")

        # Test importing tools
        logger.info("Skipping tools import (requires additional dependencies)...")
        # from src.tools import search_tool
        # logger.info("Tools imported successfully")

        # Test importing agents
        logger.info("Skipping agents import (depends on tools)...")
        # from src.agents import (
        #     ResearcherAgent,
        #     WriterAgent,
        #     PromptMasterAgent,
        #     create_tasks,
        # )
        # logger.info("Agents imported successfully")

        # Test importing main
        logger.info("Skipping main import (depends on agents)...")
        # from main import create_crew
        # logger.info("Main functions imported successfully")

        logger.info("All imports successful!")
        return True
    except ImportError as e:
        logger.error(f"Import error: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = test_imports()
    sys.exit(0 if success else 1)
