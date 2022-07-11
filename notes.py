from datetime import date




class Note:
    def __init__(self, title, note, tags):
        self.date = date.today()
        self.title = title
        self.note = note
        self.tags = tags
