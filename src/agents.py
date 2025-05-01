import os
from rich import print
from crewai import Agent, Task, Crew
# Removed redundant load_dotenv import - environment variables are loaded in config.py
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


class EditorAgent(Agent):
    """
    Initializes an EditorAgent, responsible for reviewing and refining content.
    
    This agent is designed to review the content produced by the WriterAgent,
    improving grammar, tone, cohesion, and overall quality.
"""
    def __init__(self, **kwargs):
        super().__init__(
            role="Editor",
            goal=("Review and refine content to ensure clarity, accuracy, and quality"),
            backstory=(
                "You are an experienced editor with an eye for detail and a deep "
                "understanding of how to craft compelling narratives that connect "
                "current events with literary themes."
            ),
            allow_delegation=False,
            verbose=True,
            llm=LLMFactory.init_llm(),
            **kwargs,
        )


# Tasks are now defined in src/tasks.py