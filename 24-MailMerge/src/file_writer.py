
def write_letter(output_path, letter, name):
    with open(f'{output_path}/letter_for_{name}.txt', 'w') as f:
        f.write(letter)