from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt, IntPrompt, Confirm

console = Console()

def main_menu():
    console.clear()
    title = "Main Menu"
    options = [
        "1. Display Message",
        "2. Enter Number",
        "3. Confirm Action",
        "4. Exit"
    ]
    
    menu_text = Text("\n".join(options), style="bold")
    console.print(Panel(menu_text, title=title))
    
    choice = IntPrompt.ask("Enter your choice", choices=[str(i + 1) for i in range(len(options))])
    
    if choice == 1:
        display_message()
    elif choice == 2:
        enter_number()
    elif choice == 3:
        confirm_action()
    elif choice == 4:
        exit_app()

def display_message():
    console.clear()
    message = Prompt.ask("Enter a message to display")
    console.print(f"You entered: {message}", style="bold green")
    input("Press Enter to return to the main menu...")
    main_menu()

def enter_number():
    console.clear()
    number = IntPrompt.ask("Enter a number")
    console.print(f"You entered: {number}", style="bold blue")
    input("Press Enter to return to the main menu...")
    main_menu()

def confirm_action():
    console.clear()
    confirm = Confirm.ask("Do you want to proceed with the action?")
    
    if confirm:
        console.print("Action confirmed!", style="bold yellow")
        input("Press Enter to return to the main menu...")
        main_menu()
        
def exit_app():
    console.clear()
    console.print("Exiting the application...", style="bold red")
    
if __name__ == "__main__":
    main_menu()