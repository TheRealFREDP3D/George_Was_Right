# ==================================================+ #
# George_Was_Right - Env. Variables Manager/Launcher  #
# --------------------------------------------------- #
# Filename: start.py                                  #
# --------------------------------------------------- #
# Author: Frederick Pellerin <fredp3d@proton.me>      #
# Github: https://github.com/TheRealFREDP3D/          #
# Twitter/X: https://x.com/TheRealFredP3D/            #
# --------------------------------------------------- #
# Modified: <date>                                    #
# =================================================== #

import os
import rich
from rich.console import Console
from rich.table import Table
from rich.console import JustifyMethod

# Initialize Rich Console for pretty printing
console = Console()


# Function to clear the screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# Function to load .env file content
def load_env_file():
    # List of characters that indicate a line should be skipped if it starts with them
    skip_characters = [" ", "#", "\n", "\t"]
    
    try:
        # Determine which env file to use - prefer .env, fall back to .env.example
        env_file = ".env" if os.path.exists(".env") else ".env.example"

        # If neither file exists, return an empty list
        if not os.path.exists(env_file):
            return []

        # Open and read the determined file
        with open(env_file, "r") as file:
            # Process each line, keeping only valid environment variable entries
            valid_lines = []
            for line in file.readlines():
                # Skip empty lines
                if not line.strip():
                    continue
                    
                # Skip lines that start with any character from skip_characters
                if any(line.startswith(char) for char in skip_characters):
                    continue
                    
                # If we get here, the line is valid - add it to our list
                valid_lines.append(line.strip())
                
            return valid_lines
            
    except Exception as e:
        console.print(f"[bold red]Error loading {env_file} file: {e}[/bold red]")
        return []


# Function to save .env file content
def save_env_file(lines):
    try:
        # First, let's create a backup of the existing .env file if it exists
        if os.path.exists(".env"):
            # Read the current contents of .env before we overwrite it
            with open(".env", "r") as current_file:
                current_contents = current_file.read()
            
            # Save the current contents to .env.bak
            with open(".env.bak", "w") as backup_file:
                backup_file.write(current_contents)

        # Now we can safely write the new contents to .env
        with open(".env", "w") as file:
            for line in lines:
                file.write(line + "\n")
                
        # If we get here, everything worked successfully
        console.print("[bold green]Environment file saved successfully with backup.[/bold green]")
        
    except PermissionError:
        console.print("[bold red]Error: No permission to write to .env or .env.bak file[/bold red]")
    except IOError as e:
        console.print(f"[bold red]Error: Failed to write to environment files: {e}[/bold red]")


# Function to show user feedback
def show_feedback(message):
    console.print(f"[bold green]{message}[/bold green]")


# Main function to create and run the TUI
def main():
    env_lines = load_env_file()
    show_message = None  # Add a variable to store feedback messages

    while True:
        clear_screen()
        console.print("[bold blue]     [.env] MasterManager[/bold blue]")
        console.print("=" * 30)

        # Display the table as before
        table = Table(
            title="",
            show_header=False,
            box=None,
            show_lines=True,
            title_justify="center",
        )
        for i, line in enumerate(env_lines):
            table.add_row(f"{i + 1}", line)

        console.print(table)

        # If there's a feedback message, display it
        if show_message:
            console.print(f"[bold green]{show_message}[/bold green]")
            show_message = None  # Clear the message after showing it

        # Display options menu with styling
        console.print("\n[bold yellow]Options:[/bold yellow]")
        console.print("1. Edit Line")
        console.print("2. Add New Line")
        console.print("3. Delete Line")
        console.print("4. Save Changes")
        console.print("5. Execute main.py")
        console.print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            try:
                line_num = int(input("Enter line number to edit: ")) - 1
                new_value = input(f"Edit: {env_lines[line_num].split('=')[0]}=")
                env_lines[line_num] = f"{env_lines[line_num].split('=')[0]}=" + new_value.strip()
                show_message = "Line updated."
            except (ValueError, IndexError):
                show_message = "[bold red]Invalid line number.[/bold red]"

        elif choice == "2":
            new_line = input("Enter new line: ").strip()
            if new_line:
                env_lines.append(new_line)
                show_message = "New line added."

        elif choice == "3":
            try:
                line_num = int(input("Enter line number to delete: ")) - 1
                del env_lines[line_num]
                show_message = "Line deleted."
            except (ValueError, IndexError):
                show_message = "[bold red]Invalid line number.[/bold red]"

        elif choice == "4":
            save_env_file(env_lines)
            show_message = "Changes saved."

        elif choice == "5":
            show_message = "Executing main.py..."
            time.sleep(1.5)  # Give time to read the message
            os.system("python main.py")
            break

        elif choice == "6":
            break

if __name__ == "__main__":
    main()
