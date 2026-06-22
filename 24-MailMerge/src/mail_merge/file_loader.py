
def load_all(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def load_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.readlines()
