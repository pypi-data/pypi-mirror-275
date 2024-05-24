import user_input
import persistence
import synopsis_generator
import character_generator
import outline_generator
import beat_generator
import content_generator
import post_processing
import os
import sys
import subprocess
import logging

logging.basicConfig(level=logging.INFO)

def edit_file(filename):
    try:
        if os.name == 'nt':  # For Windows
            os.startfile(filename)
        elif os.name == 'posix':  # For macOS and Linux
            if sys.platform == 'darwin':
                subprocess.call(['open', filename])
            else:
                subprocess.call(['xdg-open', filename])
    except FileNotFoundError:
        logging.error(f"File {filename} not found.")
    except PermissionError:
        logging.error(f"Permission denied to open file {filename}.")
    except Exception as e:
        logging.error(f"Failed to open file {filename}: {e}")

def main_menu():
    print("Main Menu:")
    print("1. Generate Synopsis and Character Sheets")
    print("2. Generate Chapter Outline")
    print("3. Export Content as PDF")
    print("4. Exit")


def run_interactive_session():
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            inputs, synopsis, characters = user_input.collect_inputs()
            #user_input.validate_inputs(inputs)
            serialized_inputs = user_input.serialize_inputs(inputs, synopsis, characters)
            print("Inputs collected and serialized:", serialized_inputs)
            
            # Generate synopsis
            synopsis = serialized_inputs + synopsis + characters
            synopsis = synopsis_generator.generate_synopsis(synopsis)
            with open("synopsis.txt", "w") as f:
                f.write(synopsis)
            print("Synopsis generated. Please edit the synopsis in 'synopsis.txt' before proceeding.")
            edit_file("synopsis.txt")
            
            # Generate character sheets
            characters = character_generator.generate_character(serialized_inputs, synopsis, characters)
            with open("character_sheets.txt", "w") as f:
                f.write(characters)
            print("Character sheets generated. Please edit the character sheets in 'character_sheets.txt' before proceeding.")
            edit_file("character_sheets.txt")

            # Generate chapter outline
            chapter_outline = outline_generator.generate_outline(serialized_inputs, synopsis, characters)
            with open("chapter_outline.txt", "w") as f:
                f.write(chapter_outline)
            print("Chapter outline generated. Please edit the chapter outline in 'chapter_outline.txt' before proceeding.")
            edit_file("chapter_outline.txt")
        
            filename = input("Enter the filename to load: ")
            state = persistence.load_state(filename)
            print("State loaded:", state)
        elif choice == '3':
            content = input("Enter the content to export: ")
            filename = input("Enter the filename to save as PDF: ")
            persistence.export_pdf(content, filename)
            print("PDF exported successfully.")
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    run_interactive_session()




