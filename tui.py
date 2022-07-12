import notepad
import notes
from pickle import HIGHEST_PROTOCOL, load, dump


class Tui:
    '''
    Class that manages the terminal interface.
    Can create a new notebook if not existing.
    Listens for user input and then interacts with Notepad and Note objects accordingly.
    '''

    def __init__(self):
        
        #Checks for existing notepad, if not creating a new one.
        self.notepad = self._check_for_db()
        
        #Point of reference for user input actions.
        self.func_dict = {
            'new_note': self.new_note, 
            'print_pad':self.print_pad,
            }
        #Checks dict for function, then carries it out.
        chosen_func = input('Quick_note:')
        self.active_func = self.func_dict[chosen_func]
        self.active_func()



    def _check_for_db(self):

        #Checks to see if notepad exists.
        try:
            with open('db.pickle', 'rb') as pickled_np:
                np = load(pickled_np)
                return np
        #Creates new notepad if notepad does not exist
        except:
            TypeError
            return self._new_notepad()
        #Both functions return Notepad function so user can execute commands

    def _new_notepad(self):
        #Creates new notepad Object with title based on user input
        response = input('Would you like to begin a new notepad? Y/N')
        
        if response == 'Y':
            notepad_name = input('What would you like to name your notepad?')
            new_notepad = notepad.NotePad(notepad_name)
            new_notepad.save()
            print(f'{new_notepad.name} has been saved.')
            return new_notepad

    def print_pad(self):
        #Carries out command to print contents of notepad object
        self.notepad.print()

    
    def new_note(self):
        #Creates new Note with title, content and tag based on user input
        note_title = input('Enter note title:')
        note_content = input('Enter note content:')
        note_tag = input('Enter tag:')
        self.fresh_note = notes.Note(title=note_title, note=note_content, tags=note_tag)
        #Checks if user wants to save note
        save_note = input(f'Save note? Y/N\nTitle: {self.fresh_note.title}\n{self.fresh_note.note}\n{self.fresh_note.tags}\n{self.fresh_note.date}')
        #Saves note to notepad object
        if save_note == 'Y':
            self.notepad.save(note_to_add=self.fresh_note)
           




active = 1

while active:
    Tui()

