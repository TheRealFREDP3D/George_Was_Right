echo "This code snippet creates a virtual environment for a Python project, activates it, and installs the necessary dependencies as specified in a requirements.txt file. Using a virtual environment helps manage project dependencies separately from system-wide Python installations, simplifying dependency management and avoiding version conflicts.\n"

echo "Creating a virtual environment..."
python -m venv .venv
echo "Activating the virtual environment..."
source .venv/bin/activate
echo "Installing requirements..."
pip install -r requirements.txt
echo "All done!\nexecute start.py to start George_Was_Right."
