from pickle import HIGHEST_PROTOCOL, load, dump

class NotePad:
    '''
    Class for notepad object. Can store note objects in a list, 
    print values contained in list and save itself to pickle for later use.
    '''

    def __init__(self, name):
        #Names self and creates empty array to store notes.
        self.notepad = []
        self.name = name
    
    def add(self, entry):
        #add note objects to list.
        self.notepad.append(entry)
    
    def print(self):
        #Prints all notes stored in list with some visual formatting
        print('--------------\n')
        print(f'{self.name}\n')
        print('--------------')
        for i in self.notepad:
            print(f'\nNote Title: {i.title}\nDate Added:{i.date}\n\nNote Body: {i.note}\n{i.tags}\n--------------')
    
    def save(self, note_to_add = None):
        #Adds note object to list only if necessary, then pickles itself and saves to file.
        if note_to_add:
            self.add(entry=note_to_add)
        with open('db.pickle', 'wb') as pickled_np:
                dump(self, pickled_np, protocol=HIGHEST_PROTOCOL)