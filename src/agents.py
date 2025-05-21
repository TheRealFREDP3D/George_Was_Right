"""Agents module for the George_Was_Right project.

This module defines the agents used in the project and their tasks.
Each agent has a specific role, goal, and backstory.
"""

from typing import List

from crewai import Agent, Task

from src.config import (
    log_researcher,
    log_writer,
    log_prompt_master,
)
from src.llm import LLMFactory
from src.tools import search_tool

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
            role="Expert Researcher in Political and Societal Developments",
            goal=(
                "Investigate significant global political or societal developments that reflect similarities or parallels found within Orwell's '1984', focusing on surveillance practices or control over information narratives by governing bodies or powerful entities."
            ),
            backstory=(
                "An accomplished social science research analyst specialized in political surveillance studies or digital rights advocacy work, possessing unparalleled expertise in identifying societal trends indicative of totalitarianism or thought control mechanisms."
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
            role="Comparative Analyst and Writer",
            goal=(
                "Synthesize researched occurrences into comprehensive comparative analyses between modern-day developments and thematic elements from Orwell's '1984', highlighting why contemporary incidents mirror '1984' scenarios."
            ),
            backstory=(
                "An erudite academic or journalist specializing in contemporary socio-political commentary, with thorough knowledge of literary classics like '1984'. Skilled in translating abstract literary theories into concrete real-life examples."
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
            role="Visual Concept Creator for Socio-Political Commentary",
            goal=(
                "Generate visually compelling representations (infographics or artwork) based on the comparative analyses from the Researcher and Writer Agents, visually communicating connections between '1984' themes and modern occurrences."
            ),
            backstory=(
                "An artistic graphic designer adept at crafting vivid illustrations capable of conveying complex socio-political commentary, with experience working with socio-political publications or academic institutions on issues like digital surveillance and propaganda."
            ),
            allow_delegation=False,
            verbose=True,
            llm=LLMFactory.init_llm(),
            **kwargs,
        )


<<<<<<< HEAD
def create_tasks(researcher: Agent, writer: Agent, prompt_master: Agent) -> List[Task]:
    """
Creates and returns a list of Task objects for the crew.

Args:
    researcher: The researcher agent.
    writer: The writer agent.
    prompt_master: The prompt master agent.

Returns:
    List[Task]: A list of tasks for the crew.
=======
class EditorAgent(Agent):
    """
    Initializes an EditorAgent, responsible for reviewing and refining content.
    
    This agent is designed to review the content produced by the WriterAgent,
    improving grammar, tone, cohesion, and overall quality.
>>>>>>> 7250bbcd3257d20c5709e98c48bb63bfabf03032
"""
    def __init__(self, **kwargs):
        super().__init__(
            role="Guardian of Clarity and Thematic Cohesion",
            goal=(
                "Ensure all generated content (analyses, articles, and visual prompt descriptions) is clear, grammatically impeccable, thematically coherent with Orwellian concepts, and maintains a consistent tone and high quality suitable for publication."
            ),
            backstory=(
                "A meticulous editor with extensive experience in academic and journalistic publications, specializing in political science and literary analysis. Possesses a sharp eye for detail and a deep understanding of how to refine complex arguments into compelling, accessible narratives that resonate with a broad audience."
            ),
            allow_delegation=False,
            verbose=True,
            llm=LLMFactory.init_llm(),
            **kwargs,
        )


# Tasks are now defined in src/tasks.py