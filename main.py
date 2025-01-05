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
            -------------------
            """
        )

        crew = create_crew()
        crew.kickoff()

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
        print(f"Error running application: {str(e)}")
        raise

if __name__ == "__main__":
    main()
