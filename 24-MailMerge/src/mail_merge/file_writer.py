
def write_letter(output_path, letter, name):
    with open(f'{output_path}/letter_for_{name}.txt', 'w', encoding='utf-8') as f:
        f.write(letter)
