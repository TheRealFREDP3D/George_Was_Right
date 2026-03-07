import sys
import streamlit as st
import os
import subprocess
import json
from dotenv import load_dotenv, set_key
from src.config import llm_model_name, planning_llm_name
import glob
import time

# Load environment variables
env_path = ".env"
load_dotenv(env_path, override=True)

st.set_page_config(page_title="George Was Right - AI Crew", layout="wide")

# Inject custom CSS to make st.code use full screen height
st.markdown(
    """
<style>
    /* Make st.code blocks taller and scrollable */
    [data-testid="stCodeBlock"] {
        max-height: 75vh !important;
        height: 75vh !important;
        overflow-y: auto !important;
    }
    [data-testid="stCodeBlock"] pre {
        max-height: 75vh !important;
        height: 75vh !important;
    }
</style>
""",
    unsafe_allow_html=True,
)


st.title("👁️ George Was Right - AI Crew")
st.markdown("Automated research and report generation based on Orwell's 1984 themes.")

# --- Sidebar: Configuration ---
st.sidebar.header("Configuration")

# API Keys
with st.sidebar.expander("API Keys", expanded=False):
    gemini_key = st.text_input(
        "Gemini API Key", value=os.getenv("GEMINI_API_KEY", ""), type="password"
    )
    openai_key = st.text_input(
        "OpenAI API Key", value=os.getenv("OPENAI_API_KEY", ""), type="password"
    )
    serper_key = st.text_input(
        "Serper API Key", value=os.getenv("SERPER_API_KEY", ""), type="password"
    )

    if st.button("Save API Keys"):
        set_key(env_path, "GEMINI_API_KEY", gemini_key)
        set_key(env_path, "OPENAI_API_KEY", openai_key)
        set_key(env_path, "SERPER_API_KEY", serper_key)
        st.sidebar.success("API Keys saved!")
        time.sleep(1)
        st.rerun()

# Model Selection
st.sidebar.subheader("LLM Settings")

# Load available models from Ollama API
available_models = []
try:
    import urllib.request

    req = urllib.request.Request("http://localhost:11434/api/tags")
    with urllib.request.urlopen(req, timeout=2.0) as response:
        data = json.loads(response.read())
        # CrewAI expects ollama models to be prefixed with 'ollama/'
        available_models = [
            f"ollama/{model['name']}" for model in data.get("models", [])
        ]
except Exception:
    # Fallback to json if API is unavailable
    try:
        with open("available_models.json", "r") as f:
            models_data = json.load(f)
            available_models = [
                m["name"] if m["name"].startswith("ollama/") else f"ollama/{m['name']}"
                for m in models_data
            ]
    except FileNotFoundError:
        pass
if not available_models:
    available_models = [llm_model_name]

current_model = os.getenv("LLM_MODEL_NAME", llm_model_name)
if current_model not in available_models:
    available_models.insert(0, current_model)

current_planning_model = os.getenv("PLANNING_LLM_MODEL_NAME", planning_llm_name)
if current_planning_model not in available_models:
    available_models.insert(0, current_planning_model)

available_models.append("Other (Custom)")

selected_model = st.sidebar.selectbox(
    "Select Main LLM Model",
    available_models,
    index=available_models.index(current_model)
    if current_model in available_models
    else available_models.index("Other (Custom)"),
)

if selected_model == "Other (Custom)":
    selected_model = st.sidebar.text_input(
        "Enter Custom Main LLM Model", value=current_model
    )

selected_planning_model = st.sidebar.selectbox(
    "Select Planning LLM Model",
    available_models,
    index=available_models.index(current_planning_model)
    if current_planning_model in available_models
    else available_models.index("Other (Custom)"),
)

if selected_planning_model == "Other (Custom)":
    selected_planning_model = st.sidebar.text_input(
        "Enter Custom Planning LLM Model", value=current_planning_model
    )

if st.sidebar.button("Update Models"):
    set_key(env_path, "LLM_MODEL_NAME", selected_model)
    set_key(env_path, "PLANNING_LLM_MODEL_NAME", selected_planning_model)
    st.sidebar.success(
        f"Models updated to {selected_model} and {selected_planning_model}"
    )
    time.sleep(1)
    st.rerun()


def safe_parse_search_n_results():
    """Safely parse SEARCH_N_RESULTS environment variable with fallback and bounds checking."""
    try:
        value = int(os.getenv("SEARCH_N_RESULTS", "5"))
        # Ensure value is within supported range (1-20)
        return max(1, min(20, value))
    except (ValueError, TypeError):
        # Fallback to default if parsing fails
        return 5


# Search Settings
st.sidebar.subheader("Search Settings")
search_topic = st.sidebar.text_area(
    "Search Topic",
    value=os.getenv(
        "SEARCH_TOPIC",
        "Search for recent real world news that demonstrate how Orwell's book '1984' is still relevant today",
    ),
)
search_country = st.sidebar.text_input(
    "Country Code", value=os.getenv("SEARCH_COUNTRY", "us")
)
search_n_results = st.sidebar.number_input(
    "Num Results", value=safe_parse_search_n_results(), min_value=1, max_value=20
)

if st.sidebar.button("Update Search Settings"):
    set_key(env_path, "SEARCH_TOPIC", search_topic)
    set_key(env_path, "SEARCH_COUNTRY", search_country)
    set_key(env_path, "SEARCH_N_RESULTS", str(search_n_results))
    st.sidebar.success("Search settings updated!")
    time.sleep(1)
    st.rerun()


# --- Main Area ---
log_dir = "log"
tab1, tab2, tab3 = st.tabs(["🚀 Run Crew", "📄 Results", "📝 Logs"])

# Tab 1: Run Crew
with tab1:
    st.subheader("Execute Agents")

    if st.button("Start Crew", type="primary"):
        st.info("Starting the crew... This may take a few minutes.")

        # Create a placeholder for logs
        log_placeholder = st.empty()
        full_output = ""

        try:
            # Ensure proper encoding for logs containing emojis and special characters
            env = os.environ.copy()
            env["PYTHONIOENCODING"] = "utf-8"

            # Run the main.py script
            process = subprocess.Popen(
                [sys.executable, "main.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding="utf-8",
                env=env,
                cwd=os.getcwd(),
            )

            # Stream output
            for line in process.stdout:
                full_output += line
                log_placeholder.code(full_output, language="bash")

            process.wait()

            if process.returncode == 0:
                st.success("Crew execution completed successfully!")
            else:
                st.error("Crew execution failed. Check the logs above.")

        except Exception as e:
            st.error(f"An error occurred: {e}")

# Tab 2: Results
with tab2:
    st.subheader("Generated Reports")

    # List markdown files in log directory (assuming reports are saved there based on config)
    # Actually, let's check where reports are saved.
    # src/tasks.py says output_file=log_writer (which is in log/ directory)

    if os.path.exists(log_dir):
        files = glob.glob(f"{log_dir}/*.md")
        files.sort(key=os.path.getmtime, reverse=True)

        if files:
            selected_file = st.selectbox("Select a report to view", files)
            if selected_file:
                with open(selected_file, "r", encoding="utf-8") as f:
                    content = f.read()
                st.markdown(content)
        else:
            st.info("No reports found yet.")
    else:
        st.warning("Log directory not found.")

# Tab 3: Logs
with tab3:
    st.subheader("System Logs")
    if os.path.exists(log_dir):
        log_files = glob.glob(f"{log_dir}/*.log")
        log_files.sort(key=os.path.getmtime, reverse=True)

        if log_files:
            selected_log = st.selectbox("Select a log file", log_files)
            if selected_log:
                with open(selected_log, "r", encoding="utf-8") as f:
                    log_content = f.read()
                st.code(log_content)
        else:
            st.info("No log files found.")
