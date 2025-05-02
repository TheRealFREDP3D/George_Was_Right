
"""
Task definitions for the George_Was_Right project.
This module contains the implementation of various tasks
that can be assigned to agents.
"""

from crewai import Task
from src.config import (
    log_researcher,
    log_writer,
    log_prompt_master,
)

def create_research_task(researcher_agent):
    """Create a research task for the Researcher agent."""
    return Task(
        name="Researcher Task",
        description=(
            "Search for recent real world news that demonstrate how Orwell's book "
            "'1984' is still relevant today"
        ),
        agent=researcher_agent,
        expected_output=(
            "A report containing recent events that are linked to the themes "
            "described in Orwell's book, '1984'"
        ),
        output_file=log_researcher,
    )

def create_writer_task(writer_agent):
    """Create a writing task for the Writer agent."""
    return Task(
        name="Writer Task",
        description=(
            "Compare the news events with themes from '1984' and select the most "
            "relevant match to write a small article on the subject."
        ),
        agent=writer_agent,
        expected_output=(
            "A detailed comparison of a selected news event and a theme from "
            "'1984'"
        ),
        output_file=log_writer,
    )

def create_prompt_master_task(prompt_master_agent):
    """Create a prompt generation task for the Prompt Master agent."""
    return Task(
        name="Prompt Master Task",
        description=(
            "Create two sets of prompts: one for an illustration for a recent "
            "event and another one for a linked theme of the book '1984'."
        ),
        agent=prompt_master_agent,
        expected_output=(
            "Two sets of prompts that will be used to generate illustrations: one "
            "for the recent event and one for the '1984' related book theme."
        ),
        output_file=log_prompt_master,
    )

def create_editor_task(editor_agent):
    """Create an editing task for the Editor agent."""
    return Task(
        name="Editor Task",
        description=(
            "Review and refine the article produced by the Writer agent. Improve grammar, "
            "tone, cohesion, and overall quality. Ensure the article effectively "
            "connects real-world events with themes from '1984'."
        ),
        agent=editor_agent,
        expected_output=(
            "A polished, refined article that effectively compares a current event "
            "with themes from '1984', with improved clarity, coherence, and impact."
        ),
        output_file="log/log_editor.md",
    )

def create_tasks(researcher, writer, prompt_master, editor=None):
    """Create all tasks for the crew."""
    tasks = [
        create_research_task(researcher),
        create_writer_task(writer),
        create_prompt_master_task(prompt_master)
    ]
    
    # Add editor task if editor agent is provided
    if editor:
        tasks.append(create_editor_task(editor))
        
    return tasks
