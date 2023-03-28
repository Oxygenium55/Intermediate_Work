notebook = []
path = 'notes.json'

def get_notes():
    global notebook
    return notebook

def get_note(text: str):
    global notebook
    result = []
    for i, note in enumerate(notebook):
        for field in note:
            if text in field:
                result.append((note, i))
                break
    if len(result) > 1:
        return False
    elif result == []:
        return result
    else:
        return result[0]

def open_file():
    global notebook
    global path
    with open(path, 'r', encoding="utf-8") as data:
        file = data.readlines()
    for note in file:
        notebook.append(note.strip().split(';'))
    print(notebook)

def add_new_note(new_note: list):
    global notebook
    notebook.append(new_note)

def search_note(find: str):
    global notebook
    result = []
    for note in notebook:
        for field in note:
            if find in field:
                result.append(note)
                break
    return result

def save_file():
    global notebook
    global path
    nb_str = []
    for note in notebook:
        nb_str.append(';'.join(note))
    with open(path, 'w', encoding="utf-8") as data:
        data.write('\n'.join(nb_str))
    
def remove_note(note: list):
    global notebook
    notebook.remove(note)

def edit_note(index: int, new: list):
    global notebook
    notebook[index][0] = new[0] if new[0] != '' else notebook[index][0]
    notebook[index][1] = new[1] if new[1] != '' else notebook[index][1]
    notebook[index][2] = new[2] if new[2] != '' else notebook[index][2]