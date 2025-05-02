"""Main module for the George_Was_Right project.

This module initializes and runs the CrewAI agents for the project.
Environment variables are loaded in config.py.
"""

import logging

from crewai import Crew
from rich import print

from src.agents import (
    PromptMasterAgent,
    ResearcherAgent,
    WriterAgent,
    create_tasks,
)
from src.config import (
    llm_model_name,
    log_crew,
    log_directory,
    planning_llm_name,
)
from src.llm import LLMFactory
from src.tools import search_tool

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

        # Create tasks for the agents
        tasks = create_tasks(researcher, writer, prompt_master)

        # Create and return the crew
        return Crew(
            agents=[researcher, writer, prompt_master],
            tasks=tasks,
            verbose=True,
            planning=True,
            planning_llm=LLMFactory.init_planning_llm(),
            output_log_file=log_crew
        )
    except Exception as e:
        logging.error(f"Error creating crew: {str(e)}")
        print(f"[bold red]Error creating crew: {str(e)}[/bold red]")
        raise

def main() -> None:
    """Main function to run the application.

    This function creates the crew and kicks off the process.
    It handles any exceptions that occur during execution.
    """
    try:
        # Log and display the LLM models being used
        logging.info(f"Using LLM models: {llm_model_name} (main), {planning_llm_name} (planning)")
        print(
            f"""
            -------------------
            LLM Models:
            - llm_model_name = {llm_model_name}
            - planning_llm_name = {planning_llm_name}
            -------------------
            """
        )

        # Create and run the crew
        crew = create_crew()
        crew.kickoff()

        # Log and display completion message
        logging.info("Job completed successfully")
        print(
            f"""
            -------------------
              JOB DONE!
            - llm_model_name = {llm_model_name}
            - planning_llm_name = {planning_llm_name}
            -------------------
            """
        )
    except Exception as e:
        logging.error(f"Error running application: {str(e)}")
        print(f"[bold red]Error running application: {str(e)}[/bold red]")
        raise

if __name__ == "__main__":
    main()
