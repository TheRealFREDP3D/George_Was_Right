"""Main module for the George_Was_Right project.

This module initializes and runs the CrewAI agents for the project.
Environment variables are loaded in config.py.
"""

import logging
import os
import traceback
from datetime import datetime

from crewai import Crew
from rich import print
from dotenv import load_dotenv

from src.config import (
    log_researcher,
    log_writer,
    log_prompt_master,
    log_editor,
    log_crew,
    llm_model_name,
    planning_llm_name,
    use_fallback,
    fallback_llm_name,
    log_directory,
)
from src.tools import search_tool
from src.llm import LLMFactory
from src.agents import (
    PromptMasterAgent,
    ResearcherAgent,
    WriterAgent,
    EditorAgent,
)
from src.tasks import create_tasks

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f"{log_directory}/app.log"),
        logging.StreamHandler()
    ]
)

def create_crew() -> Crew:
    """Create and configure the CrewAI crew with agents and tasks.

    Returns:
        Crew: Configured CrewAI crew instance.

    Raises:
        Exception: If there is an error creating the crew.
    """
    try:
        # Initialize agents
        researcher = ResearcherAgent(search_tool=search_tool)
        writer = WriterAgent()
        prompt_master = PromptMasterAgent()
        editor = EditorAgent()
        
        # Create tasks for the agents
        tasks = create_tasks(researcher, writer, prompt_master, editor)

        return Crew(
            agents=[researcher, writer, prompt_master, editor],
            tasks=tasks,
            verbose=True,
            planning=True,
            planning_llm=LLMFactory.init_planning_llm(),
            output_log_file=log_crew
        )
    except Exception as e:
        print(f"[ERROR] Failed to create crew: {str(e)}")
        print(traceback.format_exc())
        raise

def cleanup():
    """Cleanup resources properly when the application exits"""
    print("Cleaning up resources...")
    # Add cleanup code here if needed
    # For example: close file handles, terminate processes, etc.

def main():
    """Main function to run the application.

    This function creates the crew and kicks off the process.
    It handles any exceptions that occur during execution.
    """
    try:
        # Ensure the log directory exists
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)
            
        # Check for configuration issues
        from src.config import config_issues
        if config_issues:
            print("[ERROR] Configuration issues detected. Please fix them before continuing.")
            return None

        # Log and display the LLM models being used
        logging.info(f"Using LLM models: {llm_model_name} (main), {planning_llm_name} (planning)")
        print(
            f"""
            -------------------
            LLM Models:
            - llm_model_name = {llm_model_name}
            - planning_llm_name = {planning_llm_name}  
            - Fallback Enabled = {use_fallback}
            -------------------
            """
        )

        # Create and initialize the crew
        crew = create_crew()
        
        # Start the crew
        result = crew.kickoff()
        
        # Handle success
        print(
            f"""
            -------------------
              JOB DONE!
            - llm_model_name = {llm_model_name}
            - planning_llm_name = {planning_llm_name}
            -------------------
            """
        )
        return result
    except ConnectionError as e:
        print(f"[ERROR] Connection failed: {str(e)}")
        print("Please check if your LLM service is running or if you need to use a different model.")
        if use_fallback:
            try:
                print(f"Attempting to use fallback model: {fallback_llm_name}")
                # Here we could implement specific fallback logic if needed
                # For example, temporarily modify config and re-create crew
                print(f"Fallback mechanism activated. This feature needs implementation.")
            except Exception as fallback_error:
                print(f"[ERROR] Fallback attempt failed: {str(fallback_error)}")
        return None
    except Exception as e:
        print(f"[ERROR] Application error: {str(e)}")
        print(traceback.format_exc())
        # Log the error to a file for better debugging
        error_log_path = f"{log_directory}/error-{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
        with open(error_log_path, "w") as error_file:
            error_file.write(f"Error: {str(e)}\n\n")
            error_file.write(traceback.format_exc())
        print(f"Error details saved to {error_log_path}")
        return None

if __name__ == "__main__":
    try:
        result = main()
        if result is None:
            print("Application completed with no result.")
            exit(1)
        exit(0)
    except Exception as e:
        print(f"Unhandled exception: {str(e)}")
        exit(1)
    finally:
        cleanup()
