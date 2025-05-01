#!/usr/bin/env python

import os
from rich import print
from crewai import Agent, Task, Crew
from dotenv import load_dotenv
from src.config import (
    log_researcher,
    log_writer,
    log_prompt_master,
    log_crew,
    llm_model_name,
    planning_llm_name,
)
from src.tools import search_tool
from src.llm import LLMFactory
from src.agents import (
    ResearcherAgent,
    WriterAgent,
    PromptMasterAgent,
    create_tasks,
)
import subprocess

# Load environment variables
load_dotenv()

def create_crew():
    try:
        researcher = ResearcherAgent(search_tool=search_tool)
        writer = WriterAgent()
        prompt_master = PromptMasterAgent()
        tasks = create_tasks(researcher, writer, prompt_master)
        return Crew(
            agents=[researcher, writer, prompt_master],
            tasks=tasks, 
            verbose=True, 
            planning=True,
            planning_llm=LLMFactory.init_planning_llm(), 
            output_log_file=log_crew
        )
    except Exception as e:
        print(f"Error creating crew: {str(e)}")
        raise

def main():
    try:
        # Ensure the log directory exists
        log_directory = os.path.dirname(log_crew)
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)
        
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
            print(f"The system attempted to use the fallback model but still encountered issues.")
        return None
    except Exception as e:
        print(f"[ERROR] Application error: {str(e)}")
        import traceback
        print(traceback.format_exc())
        return None

if __name__ == "__main__":
    main()
