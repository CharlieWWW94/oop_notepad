from pickle import HIGHEST_PROTOCOL, load, dump

class NotePad:
    def __init__(self, name):
        self.notepad = []
        self.name = name
    
    def add(self, entry):
        self.notepad.append(entry)
    
    def print(self):
        print('--------------\n')
        print(f'{self.name}\n')
        print('--------------')
        for i in self.notepad:
            print(f'\nNote Title: {i.title}\nDate Added:{i.date}\n\nNote Body: {i.note}\n{i.tags}\n--------------')
    
    def save(self, note_to_add = None):

        if note_to_add:
            self.add(entry=note_to_add)
        with open('db.pickle', 'wb') as pickled_np:
                dump(self, pickled_np, protocol=HIGHEST_PROTOCOL)