import pickle


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
            #print(i.date)
            #print(i.title)
            #print(i.note)
            #print(i.tags)