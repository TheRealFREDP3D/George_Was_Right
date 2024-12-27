#!/usr/bin/env python

import os
from rich import print
from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv
from src.config import *
from src.tools import search_tool
from src.llm import LLMFactory

# Load environment variables before any other operations
load_dotenv()


# Validate required environment variables
def validate_environment():
    required_vars = [
        "LLM_MODEL_NAME",
        "PLANNING_LLM_NAME",
    ]  # Changed to match config.py
    if missing_vars := [var for var in required_vars if not os.getenv(var)]:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing_vars)}"
        )


class ResearcherAgent(Agent):
    def __init__(self, search_tool=None, **kwargs):
        if not search_tool:
            raise ValueError("search_tool is required for ResearcherAgent")
            
        super().__init__(
            role="Researcher",
            goal=(
                "Finding recent real world news that demonstrate how Orwell's book "
                "'1984' is still relevant in our days."
            ),
            backstory=(
                "You are an expert researcher with a keen eye for current events "
                "and literary analysis."
            ),
            allow_delegation=True,
            verbose=True,
            llm=LLMFactory.init_llm(),
            tools=[search_tool],
            **kwargs
        )

class WriterAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(
            role="Writer",
            goal=(
                "Gather examples of real world news events that could be from "
                "Orwell's '1984' book"
            ),
            backstory=(
                "You are a skilled writer with a deep understanding of literature "
                "and current affairs."
            ),
            allow_delegation=True,
            verbose=True,
            llm=LLMFactory.init_llm(),
            **kwargs
        )

class PromptMasterAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(
            role="Prompt Master",
            goal=(
                "Create visual concepts based on provided prompts"
            ),
            backstory=(
                "You are a talented illustrator with a knack for translating ideas "
                "into compelling visuals."
            ),
            allow_delegation=False,
            verbose=True,
            llm=LLMFactory.init_llm(),
            **kwargs
        )

def create_tasks(researcher, writer, prompt_master):
    return [
        Task(
            name="Researcher Task",
            description=(
                "Search for recent real world news that demonstrate how Orwell's book "
                "'1984' is still relevant today"
            ),
            agent=researcher,
            expected_output=(
                "A report containing recent events that are linked to the themes "
                "described in Orwell's book, '1984'"
            ),
            output_file=log_researcher
        ),
        Task(
            name="Writer Task",
            description=(
                "Compare the news events with themes from '1984' and select the most "
                "relevant match to write a small article on the subject."
            ),
            agent=writer,
            expected_output=(
                "A detailed comparison of a selected news event and a theme from "
                "'1984'"
            ),
            output_file=log_writer,
        ),
        Task(
            name="Prompt Master Task",
            description=(
                "Create two sets of prompts: one for an illustration for a recent "
                "event and another one for a linked theme of the book '1984'."
            ),
            agent=prompt_master,
            expected_output=(
                "Two sets of prompts that will be used to generate illustrations: one "
                "for the recent event and one for the '1984' book theme."
            ),
            output_file=log_prompt_master,
        )
    ]

def create_crew():
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
            output_log_file=log_crew,
        )
    except Exception as e:
        print(f"Error creating crew: {str(e)}")
        raise

def main():
    try:
        validate_environment()
        
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
