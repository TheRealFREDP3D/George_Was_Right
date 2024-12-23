# v1.2 - Basic AI project setup - FINAL

# Importing necessary libraries and tools
import os
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool
import dotenv

dotenv.load_dotenv()


# Define the agents
class ResearcherAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(
            role="Researcher",
            goal="Research real world news to find and compare with Orwell's '1984' themes.",
            backstory="You are an expert researcher with a keen eye for current events and literary analysis.",
            allow_delegation=False,
            verbose=True,
            **kwargs,
        )


class WriterAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(
            role="Writer",
            goal="Gather examples of real world news events that could be from the Orwell's '1984' book",
            backstory="You are a skilled writer with a deep understanding of literature and current affairs.",
            allow_delegation=False,
            verbose=True,
            **kwargs,
        )


class IllustratorAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(
            role="Illustrator",
            goal="Create visual concepts based on provided prompts",
            backstory="You are a talented illustrator with a knack for translating ideas into compelling visuals.",
            allow_delegation=False,
            verbose=True,
            **kwargs,
        )


# Create the crew
def create_crew():
    # Initialize Ollama
    llm = LLM(model="ollama/llama3.1:latest")

    # Create agents with the Ollama LLM and SerperDevTool
    researcher = ResearcherAgent(llm=llm, tools=[SerperDevTool()])
    writer = WriterAgent(llm=llm, tools=[SerperDevTool()])
    illustrator = IllustratorAgent(llm=llm, tools=[SerperDevTool()])

    # Create tasks
    tasks = [
        Task(
            description="Search for recent real world news that demonstrate how Orwell's book '1984' is still relevant today",
            agent=researcher,
            expected_output="Top three relevant news that are related to '1984'",
        ),
        Task(
            description="Compare the news events with themes from '1984' and select the most relevant match to write a small article on the subject.",
            agent=writer,
            expected_output="A detailed comparison of a selected news event and a theme from '1984'",
        ),
        Task(
            description="Create two sets of prompts: one for an illustration of the current news event and another for an illustration of the similar event or theme from '1984'",
            agent=writer,
            expected_output="Two sets of illustration prompts: one for the news event and one for the '1984' theme",
        ),
        Task(
            description="Create visual concepts based on the provided prompts",
            agent=illustrator,
            expected_output="Descriptions of visual concepts for both the news event and the '1984' theme",
        ),
    ]

    return Crew(
        agents=[researcher, writer, illustrator],
        tasks=tasks,
        verbose=True,
        process=Process.sequential,
    )


def main():
    crew = create_crew()
    result = crew.kickoff()

    print(
        f"""
          *************************************************************************
          *                           JOB DONE!                                   *
          *************************************************************************
          {result}
        """
    )


if __name__ == "__main__":
    main()
