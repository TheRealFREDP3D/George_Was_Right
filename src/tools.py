from src.config import search_country, search_n_results
from crewai_tools import SerperDevTool

# Initialize the search tool with the specified country and number of results. The SerperDevTool is a tool that uses Serper Dev to search the web. The country and number of results are passed as arguments to the constructor of the SerperDevTool.
search_tool = SerperDevTool(country=search_country, n_results=search_n_results)
