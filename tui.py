import notepad
import notes
from pickle import HIGHEST_PROTOCOL, load, dump


class Tui:
    def __init__(self):
        self.notepad = self._check_for_db()

        self.func_dict = {
            'new_note': self.new_note, 
            'print_pad':self.print_pad,
            }

        chosen_func = input('Quick_note:')
        self.active_func = self.func_dict[chosen_func]
        self.active_func()


    def _check_for_db(self):
        try:
            with open('db.pickle', 'rb') as pickled_np:
                np = load(pickled_np)
                return np
        except:
            TypeError
            self._new_notepad()
    
    def _new_notepad(self):
        response = input('Would you like to begin a new notepad? Y/N')
        
        if response == 'Y':
            notepad_name = input('What would you like to name your notepad?')
            new_notepad = notepad.NotePad(notepad_name)
            with open('db.pickle', 'wb') as pickled_np:
                dump(new_notepad, pickled_np, protocol=HIGHEST_PROTOCOL)
            return new_notepad
    
    def print_pad(self):
        self.notepad.print()

    
    def new_note(self):
        
        note_title = input('Enter note title:')
        note_content = input('Enter note content:')
        note_tag = input('Enter tag:')
        
        self.fresh_note = notes.Note(title=note_title, note=note_content, tags=note_tag)

        save_note = input(f'Save note? Y/N\nTitle: {self.fresh_note.title}\n{self.fresh_note.note}\n{self.fresh_note.tags}\n{self.fresh_note.date}')
        if save_note == 'Y':
            self.save_note()

    def save_note(self):
            self.notepad.add(self.fresh_note)
            with open('db.pickle', 'wb') as pickled_np:
                dump(self.notepad, pickled_np, protocol=HIGHEST_PROTOCOL)




active = 1

while active:
    Tui()

#dictionary of functions