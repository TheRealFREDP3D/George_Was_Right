#!/bin/env/python

# George_Was_Right
# v0.2 - Basic AI project setup - FINAL

# Importing necessary libraries and tools
from rich import print
import os
from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool

# Load environment variable from /.env
from dotenv import load_dotenv

load_dotenv()
import openai

llm_model_name = "github/gpt-4o"

# LLM Config-----------------------------------------------------
print("""
     * ************************************* *
    * |         Initialize LLM Model        | *  
    * |  llm_model_name = "github/gpt-4o"   | *
     * ************************************* *
     """
     )
     
llm = LLM(model=llm_model_name, temperature=0.3)

# ---------------------------------------------------------------

# Search Tool
search_country = os.getenv(
    "SEARCH_COUNTRY",
    "us",
)
search_n_results = os.getenv("SEARCH_N_RESULTS", 5)
search_tool = SerperDevTool(country=search_country, n_results=search_n_results)


# Define the agents
class ResearcherAgent(Agent):
    """
    An agent responsible for researching real-world news to find and compare with themes from Orwell's '1984'.

    Attributes:
        role (str): The role of the agent, which is "Researcher".
        goal (str): The goal of the agent, which is to research real-world news and compare it with Orwell's '1984' themes.
        backstory (str): The backstory of the agent, describing them as an expert researcher with a keen eye for current events and literary analysis.
        allow_delegation (bool): Whether the agent can delegate tasks, set to True.
        verbose (bool): Whether the agent should provide verbose output, set to True.
        llm (LLM): The language model used by the agent.
        tools (list): The tools available to the agent, including the search tool.
    """

    def __init__(self, **kwargs):
        super().__init__(
            role="Researcher",
            goal="Research real world news to find and compare with Orwell's '1984' themes.",
            backstory="You are an expert researcher with a keen eye for current events and literary analysis.",
            allow_delegation=True,
            verbose=True,
            llm=llm,
            tools=[search_tool],
        )


class WriterAgent(Agent):
    """
    An agent responsible for gathering examples of real-world news events that could be from Orwell's '1984'.

    Attributes:
        role (str): The role of the agent, which is "Writer".
        goal (str): The goal of the agent, which is to gather examples of real-world news events that could be from Orwell's '1984'.
        backstory (str): The backstory of the agent, describing them as a skilled writer with a deep understanding of literature and current affairs.
        allow_delegation (bool): Whether the agent can delegate tasks, set to True.
        verbose (bool): Whether the agent should provide verbose output, set to True.
        output_file (str): The file where the agent's output will be logged, set to "./log/writer_test.log".
        llm (LLM): The language model used by the agent.
    """

    def __init__(self, **kwargs):
        super().__init__(
            role="Writer",
            goal="Gather examples of real world news events that could be from the Orwell's '1984' book",
            backstory="You are a skilled writer with a deep understanding of literature and current affairs.",
            allow_delegation=True,
            verbose=True,
            output_file="./log/writer_test.log",
            llm=llm,
        )


class IllustratorAgent(Agent):
    """
    An agent responsible for creating visual concepts based on provided prompts.

    Attributes:
        role (str): The role of the agent, which is "Illustrator".
        goal (str): The goal of the agent, which is to create visual concepts based on provided prompts.
        backstory (str): The backstory of the agent, describing them as a talented illustrator with a knack for translating ideas into compelling visuals.
        allow_delegation (bool): Whether the agent can delegate tasks, set to False.
        verbose (bool): Whether the agent should provide verbose output, set to True.
        llm (LLM): The language model used by the agent.
    """

    def __init__(self, **kwargs):
        super().__init__(
            role="Illustrator",
            goal="Create visual concepts based on provided prompts",
            backstory="You are a talented illustrator with a knack for translating ideas into compelling visuals.",
            allow_delegation=False,
            verbose=True,
            llm=llm,
        )


# Create the crew
def create_crew():
    """
    Creates a crew of agents and tasks for the project.

    Returns:
        Crew: A crew object containing the agents and tasks.
    """
    # Create agents with the Ollama LLM and SerperDevTool
    researcher = ResearcherAgent()
    writer = WriterAgent()
    illustrator = IllustratorAgent()

    # Create tasks
    tasks = [
        Task(
            name="Researcher Task",
            description="""
            Search for recent real world news that demonstrate how Orwell's book
            '1984' is still relevant today
            """,
            agent=researcher,
            expected_output="""
            A report containing recent events that are linked to the themes
            described in Orwell's book, '1984'
            """,
        ),
        Task(
            name="Writer Task",
            description="""
            Compare the news events with themes from '1984' and
            select the most relevant match to write a small article on the
            subject.
            """,
            agent=writer,
            expected_output="""
            A detailed comparison of a selected news event and a theme from
            '1984'
            """,
            output_file="./log/log_writer.md",
        ),
        Task(
            name="Illustrator Task",
            description="""
            Create two sets of prompts: one for an illustration for a recent
            event and another one for a linked theme of the book '1984'
            """,
            agent=illustrator,
            expected_output="""
            Two sets of prompts that will be used to generate illustrations:
            one for the recent event and one for the '1984' book theme.
            """,
            output_file="./log/log_illustrator.md",
        ),
    ]

    return Crew(
        agents=[researcher, writer, illustrator],
        tasks=tasks,
        verbose=True,
        planning=True,
        planning_llm=LLM(model="github/gpt-4o", temperature=0.1),
    )


def main():
    crew = create_crew()
    crew.kickoff()

    print("""
     * ************************************* *
    * |                 DONE!               | *  
    * |  llm_model_name = "github/gpt-4o"   | *
     * ************************************* *
     """)


if __name__ == "__main__":
    main()
