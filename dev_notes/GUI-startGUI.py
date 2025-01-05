# ================================================= #
# George_Was_Right - .env Manager                   #
# ------------------------------------------------- #
# Filename: startGUI.py                                #
# ------------------------------------------------- #
# Author: Frederick Pellerin <fredp3d@proton.me>    #
# Github: https://github.com/TheRealFREDP3D/        #
# Twitter/X: https://x.com/TheRealFredP3D/          #
# ------------------------------------------------- #
# Modified: 29-12-2024                              #
# ================================================= #

import PySimpleGUI as sg
import os


"""
This is a small tool that load the .env file in a GUI  
for editing values.   
Execute the main.py script.  
"""


# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to load .env file content
def load_env_file():
    try:
        if not os.path.exists('.env'):
            return []
        with open('.env', 'r') as file:
            return [line.strip() for line in file.readlines()]
    except Exception as e:
        sg.popup(f"Error loading .env file: {e}")
        return []


# Function to save .env file content
def save_env_file(lines):
    try:
        with open('.env', 'w') as file:
            for line in lines:
                file.write(line + '\n')
    except Exception as e:
        sg.popup(f"Error saving .env file: {e}")


# Function to show user feedback
def show_feedback(message):
    sg.popup(message)


# Main function to create and run the GUI
def main():
    # Load .env file content
    env_lines = load_env_file()
    
    # Define the layout of the GUI
    layout = [
        [sg.Text('Edit .env File')],
        [sg.Listbox(env_lines, size=(100, 25), key='-LIST-', enable_events=True)],
        [sg.InputText(key='-INPUT-', visible=False)],
        [sg.Button('Save .env'), sg.Button('Execute main.py'), sg.Button('Add New Line'), sg.Button('Delete Selected Line'), sg.Button('Cancel')],
    ]
    
    # Create the window
    window = sg.Window('George-Was-Right - .env Manager', layout)
    
    # Event loop to process "events" and get the "values" of the inputs
    current_line = None
    
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        
        elif event == '-LIST-':  # A line was selected
            current_line = values['-LIST-'][0]
            window['-INPUT-'].update(value=current_line)
            window['-INPUT-'].update(visible=True)
        
        elif event == 'Save .env':
            if current_line is not None:
                env_lines[env_lines.index(current_line)] = values['-INPUT-']
                current_line = None
                window['-INPUT-'].update(visible=False)
                show_feedback("Changes saved.")
            
            save_env_file(env_lines)

        elif event == 'Execute main.py':
            show_feedback("Executing main.py...")
            os.system('python main.py')
            break
        
        elif event == 'Add New Line':
            new_line = sg.popup_get_text("Enter new line:")
            if new_line is not None and new_line.strip():
                env_lines.append(new_line.strip())
                window['-LIST-'].update(values=env_lines)
                show_feedback("New line added.")
        
        elif event == 'Delete Selected Line':
            if current_line is not None:
                env_lines.remove(current_line)
                current_line = None
                window['-LIST-'].update(values=env_lines)
                show_feedback("Selected line deleted.")
        
        elif event == '\r' or event == '\n':  # Enter key pressed in input box
            if current_line is not None:
                env_lines[env_lines.index(current_line)] = values['-INPUT-']
                current_line = None
                window['-INPUT-'].update(visible=False)
                window['-LIST-'].update(values=env_lines)
    
    # Close the window
    window.close()


if __name__ == '__main__':
    main()
