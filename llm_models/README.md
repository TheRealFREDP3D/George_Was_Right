# LLM Models

# Check LiteLLM supported providers for the LLMs name formatting.
# For most of them, the format is "<provider>/<model_name>"
# Use crewai.LLM to initialize the LLM.
# Ex: llm = LLM(model="ollama/llama3.1")

# GLHF -----------------------------------------------------------------
# GLHF: need to mock an OpenAI model and add "hf:" before the model name

# Set OPENAI_API_KEY to your GLHF API key.
# Set OPENAI_BASE_URL to your GLHF base URL.
# Set OPENAI_MODEL_NAME to the model name you want to use.
# (Ex: openai/hf:Qwen2.5-72B-Instruct)