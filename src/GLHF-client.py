# LLM Config -----------------------------------------------------------------
llm_model_name = "openai/hf:NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO"
planning_llm_name = "github/gpt-4o"
base_url = os.getenv("OPENAI_API_BASE")

llm = LLM(model=llm_model_name, temperature=0.3)
planning_llm = LLM(model=planning_llm_name, temperature=0.1)