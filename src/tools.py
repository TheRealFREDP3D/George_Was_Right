"""Tools module for the George_Was_Right project.

This module provides tools used by the agents in the project,
such as search functionality.
"""

from crewai_tools import SerperDevTool
from src.config import search_country, search_n_results

# Initialize the search tool with the specified country and number of results
search_tool = SerperDevTool(country=search_country, n_results=search_n_results)
