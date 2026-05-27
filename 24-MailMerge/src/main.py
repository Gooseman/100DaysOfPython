
_input_location = '../Input'
_names_location = f'{_input_location}/Names/invited_names.txt'
_invite_letter_location = f'{_input_location}/Letters/starting_letter.txt'
_output_location = '../Output/ReadyToSend'

def load_letter_template(file_path):
    from file_loader import load_all

    return load_all(file_path)

def load_names(file_path):
    from file_loader import load_lines

    return load_lines(file_path)

def build_invite_letters(template, names):
    from letter_builder import replace_name
    from file_writer import write_letter

    for name in names:
        name = name.strip()
        new_letter = replace_name(template, name)

        write_letter(_output_location, new_letter, name)

if __name__ == "__main__":
    names = load_names(_names_location)
    template = load_letter_template(_invite_letter_location)

    build_invite_letters(template, names)