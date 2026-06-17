
from file_loader import load_all, load_lines
from file_writer import write_letter
from letter_builder import replace_name

INPUT_LOCATION = '../Input'
NAMES_LOCATION = f'{INPUT_LOCATION}/Names/invited_names.txt'
INVITE_LETTER_LOCATION = f'{INPUT_LOCATION}/Letters/starting_letter.txt'
OUTPUT_LOCATION = '../Output/ReadyToSend'

def load_letter_template(file_path):
    return load_all(file_path)

def load_names(file_path):
    return load_lines(file_path)

def build_invite_letters(template, names):
    for name in names:
        name = name.strip()
        new_letter = replace_name(template, name)

        write_letter(OUTPUT_LOCATION, new_letter, name)

def run_app():
    names = load_names(NAMES_LOCATION)
    template = load_letter_template(INVITE_LETTER_LOCATION)

    build_invite_letters(template, names)

if __name__ == "__main__":
    run_app()
