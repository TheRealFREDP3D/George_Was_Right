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

class ResearcherAgent(Agent):
    """
Initializes a ResearcherAgent with a specified search tool and additional
parameters.

The ResearcherAgent is designed to find recent news that illustrate the
continued relevance of Orwell's '1984'. It requires a search tool for
operation and utilizes an LLM for processing. The agent is characterized
by its role, goal, backstory, and the ability to delegate tasks.

Parameters:
    search_tool: A tool used for searching relevant news articles.
    **kwargs: Additional parameters for the Agent initialization.

Raises:
    ValueError: If no search_tool is provided.
"""
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
            **kwargs,
        )


class WriterAgent(Agent):
    """
    Initializes a WriterAgent with specific role, goal, backstory, and LLM.

    This agent is designed for gathering real-world news examples that resemble events from Orwell's '1984'.
    It is configured with delegation enabled and verbose output.
"""
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
            **kwargs,
        )


class PromptMasterAgent(Agent):
    """
    Initializes a PromptMasterAgent, responsible for creating visual concepts prompts.

    This agent is configured with a specific role, goal, backstory, and LLM.
    It does not allow task delegation.
"""
    def __init__(self, **kwargs):
        super().__init__(
            role="Prompt Master",
            goal=("Create visual concepts based on provided prompts"),
            backstory=(
                "You are a talented illustrator with a knack for translating ideas "
                "into compelling visuals."
            ),
            allow_delegation=False,
            verbose=True,
            llm=LLMFactory.init_llm(),
            **kwargs,
        )


def create_tasks(researcher, writer, prompt_master):
    """
Creates and returns a list of Task objects for the crew.

Each task is assigned to a specific agent and includes a description,
expected output, and an output file for logging.
"""
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
            output_file=log_researcher,
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
                "for the recent event and one for the '1984' related book theme."
            ),
            output_file=log_prompt_master,
        ),
    ]