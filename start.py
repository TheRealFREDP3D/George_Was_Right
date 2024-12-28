import os
import sys
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich import box
from typing import Dict, Optional
import shutil
import subprocess

# Define the theme with more colors
custom_theme = Theme({
    "primary": "#3498db",  # Blue
    "secondary": "#f1c40f",  # Yellow
    "success": "#2ecc71",  # Green
    "error": "#e74c3c",  # Red
    "warning": "#e67e22",  # Orange
    "info": "#95a5a6",  # Gray
})

console = Console(theme=custom_theme)


class EnvManager:
    def __init__(self, env_file: str = ".env.example"):
        self.env_file = env_file
        self.env_data: Dict[str, str] = {}
        self.backup_file = f"{env_file}.backup"
        self.modified = False

    def create_backup(self) -> None:
        """Create a backup of the current env file"""
        if os.path.exists(self.env_file):
            shutil.copy2(self.env_file, self.backup_file)
            console.print("[info]Backup created successfully[/info]")

    def restore_backup(self) -> None:
        """Restore from backup file"""
        if os.path.exists(self.backup_file):
            shutil.copy2(self.backup_file, self.env_file)
            os.remove(self.backup_file)
            console.print("[success]Backup restored successfully[/success]")
            self.load_env_file()
        else:
            console.print("[error]No backup file found![/error]")

    def load_env_file(self) -> bool:
        """Load environment variables from file"""
        try:
            if not os.path.exists(self.env_file):
                console.print(
                    f"[warning]File {self.env_file} not found. Creating new file.[/warning]"
                )
                return False

            self.env_data.clear()
            with open(self.env_file, "r") as f:
                for line_num, line in enumerate(f.readlines(), 1):
                    line = line.strip()
                    if line and not line.startswith("#"):
                        try:
                            key, value = line.split("=", 1)
                            self.env_data[key.strip()] = value.strip()
                        except ValueError:
                            console.print(
                                f"[error]Invalid format at line {line_num}: {line}[/error]"
                            )
            return True
        except Exception as e:
            console.print(f"[error]Error loading file: {str(e)}[/error]")
            return False

    def save_env_file(self) -> bool:
        """Save environment variables to file"""
        try:
            # Create backup before saving
            self.create_backup()

            with open(self.env_file, "w") as f:
                # Sort keys for consistent output
                for key in sorted(self.env_data.keys()):
                    f.write(f"{key}={self.env_data[key]}\n")

            console.print("[success]Changes saved successfully![/success]")
            self.modified = False
            return True
        except Exception as e:
            console.print(f"[error]Error saving file: {str(e)}[/error]")
            return False

    def display_values(self) -> None:
        """Display current environment variables in a table"""
        if not self.env_data:
            console.print("[warning]No environment variables found[/warning]")
            return

        table = Table(box=box.ROUNDED)
        table.add_column("Variable Name", style="primary")
        table.add_column("Value", style="secondary")

        for key in sorted(self.env_data.keys()):
            table.add_row(key, self.env_data[key])

        console.print(Panel(table, title="Current Environment Variables"))

    def edit_value(self, key: Optional[str] = None) -> None:
        """Edit value for a given key"""
        if not key:
            key = Prompt.ask("Enter key to edit")

        if key in self.env_data:
            current_value = self.env_data[key]
            console.print(f"Current value: [secondary]{current_value}[/secondary]")
            new_value = Prompt.ask("Enter new value", default=current_value)
            if new_value != current_value:
                self.env_data[key] = new_value
                self.modified = True
                console.print("[success]Value updated successfully[/success]")
        else:
            console.print("[error]Key not found![/error]")
            if Confirm.ask("Would you like to add this as a new key?"):
                self.add_new_entry(key)

    def add_new_entry(self, key: Optional[str] = None) -> None:
        """Add a new environment variable"""
        if not key:
            key = Prompt.ask("Enter new key").strip().upper()

        if key in self.env_data:
            console.print("[warning]Key already exists![/warning]")
            if Confirm.ask("Would you like to edit the existing value?"):
                self.edit_value(key)
            return

        value = Prompt.ask("Enter value")
        self.env_data[key] = value
        self.modified = True
        console.print("[success]New entry added successfully[/success]")

    def execute_main(self) -> None:
        """Execute main.py with current environment variables"""
        try:
            if self.modified and Confirm.ask("Save changes before executing?"):
                self.save_env_file()

            console.print("[info]Executing main.py...[/info]")
            result = subprocess.run(["python", "main.py"], capture_output=True, text=True)

            if result.returncode == 0:
                console.print("[success]Execution completed successfully[/success]")
                if result.stdout:
                    console.print(Panel(result.stdout, title="Output"))
            else:
                console.print("[error]Execution failed![/error]")
                if result.stderr:
                    console.print(Panel(result.stderr, title="Error", style="error"))
        except Exception as e:
            console.print(f"[error]Error executing main.py: {str(e)}[/error]")


def display_menu(env_manager: EnvManager) -> None:
    """Display the main menu with environment variables and a welcome message"""
    menu_items = [
        ("1", "View Current Values"),
        ("2", "Edit Value"),
        ("3", "Add New Entry"),
        ("4", "Save Changes"),
        ("5", "Restore from Backup"),
        ("6", "Execute main.py"),
        ("q", "Quit"),
    ]

    # Create a table for the environment variables
    env_table = Table(box=None, show_header=False)
    env_table.add_column("Variable Name", style="primary")
    env_table.add_column("Value", style="secondary")

    for key in sorted(env_manager.env_data.keys()):
        env_table.add_row(key, env_manager.env_data[key])

    # Create a panel for the environment variables
    env_panel = Panel(env_table, title="Current Environment Variables")

    # Create a panel for the welcome message and commands
    welcome_message = (
        "Welcome to the Environment Manager!\n\n"
        "Available commands:\n"
        "1. View Current Values\n"
        "2. Edit Value\n"
        "3. Add New Entry\n"
        "4. Save Changes\n"
        "5. Restore from Backup\n"
        "6. Execute main.py\n"
        "q. Quit"
    )
    welcome_panel = Panel(welcome_message, title="Environment Manager", subtitle="Choose an option")

    # Display both panels side by side
    console.print(Panel(Group(env_panel, welcome_panel), box=box.ROUNDED))


def main():
    env_manager = EnvManager()
    env_manager.load_env_file()

    while True:
        display_menu()
        while True:
            choice = Prompt.ask("> ", choices=["1", "2", "3", "4", "5", "6", "q"], show_choices=False)
            if choice:
                break
            console.print("Please select one of the available options")

        if choice == "q":
            if env_manager.modified:
                if Confirm.ask("You have unsaved changes. Save before quitting?"):
                    env_manager.save_env_file()
            break

        actions = {
            "1": env_manager.display_values,
            "2": env_manager.edit_value,
            "3": env_manager.add_new_entry,
            "4": env_manager.save_env_file,
            "5": env_manager.restore_backup,
            "6": env_manager.execute_main,
        }

        actions[choice]()

        # Add a blank line for better readability
        console.print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[warning]Program terminated by user[/warning]")
        sys.exit(0)
