from crewai_tools import SerperDevTool
from src.config import search_country, search_n_results

search_tool = SerperDevTool(country=search_country, n_results=search_n_results)
