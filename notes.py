from datetime import date




class Note:
    '''
    Creates note object with variety of attributes for later access.
    All must be passed in to make a note.
    '''
    def __init__(self, title, note, tags):
        self.date = date.today()
        self.title = title
        self.note = note
        self.tags = tags
