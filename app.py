import streamlit as st
import os
import subprocess
import json
from dotenv import load_dotenv, set_key
import glob
import time

# Load environment variables
env_path = ".env"
load_dotenv(env_path)

st.set_page_config(page_title="George Was Right - AI Crew", layout="wide")

st.title("👁️ George Was Right - AI Crew")
st.markdown("Automated research and report generation based on Orwell's 1984 themes.")

# --- Sidebar: Configuration ---
st.sidebar.header("Configuration")

# API Keys
with st.sidebar.expander("API Keys", expanded=False):
    gemini_key = st.text_input("Gemini API Key", value=os.getenv("GEMINI_API_KEY", ""), type="password")
    openai_key = st.text_input("OpenAI API Key", value=os.getenv("OPENAI_API_KEY", ""), type="password")
    serper_key = st.text_input("Serper API Key", value=os.getenv("SERPER_API_KEY", ""), type="password")
    
    if st.button("Save API Keys"):
        set_key(env_path, "GEMINI_API_KEY", gemini_key)
        set_key(env_path, "OPENAI_API_KEY", openai_key)
        set_key(env_path, "SERPER_API_KEY", serper_key)
        st.sidebar.success("API Keys saved!")
        time.sleep(1)
        st.rerun()

# Model Selection
st.sidebar.subheader("LLM Settings")

# Load available models if file exists
available_models = []
try:
    with open("available_models.json", "r") as f:
        models_data = json.load(f)
        available_models = [m["name"] for m in models_data]
except FileNotFoundError:
    available_models = ["gemini/gemini-pro", "gemini/gemini-1.5-flash", "gpt-4o-mini", "gpt-3.5-turbo"]

current_model = os.getenv("LLM_MODEL_NAME", "gemini/gemini-pro")
# Handle case where current model is not in the list (e.g. custom or old)
if current_model not in available_models:
    available_models.insert(0, current_model)

selected_model = st.sidebar.selectbox("Select LLM Model", available_models, index=available_models.index(current_model))

if st.sidebar.button("Update Model"):
    set_key(env_path, "LLM_MODEL_NAME", selected_model)
    set_key(env_path, "PLANNING_LLM_MODEL_NAME", selected_model)
    set_key(env_path, "FALLBACK_LLM_NAME", selected_model)
    st.sidebar.success(f"Model updated to {selected_model}")
    time.sleep(1)
    st.rerun()

# Search Settings
st.sidebar.subheader("Search Settings")
search_topic = st.sidebar.text_area("Search Topic", value=os.getenv("SEARCH_TOPIC", "Search for recent real world news that demonstrate how Orwell's book '1984' is still relevant today"))

if st.sidebar.button("Update Topic"):
    set_key(env_path, "SEARCH_TOPIC", search_topic)
    st.sidebar.success("Search topic updated!")
    time.sleep(1)
    st.rerun()


# --- Main Area ---
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
            # Run the main.py script
            process = subprocess.Popen(
                ["python", "main.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                cwd=os.getcwd()
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
    
    log_dir = "log"
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
