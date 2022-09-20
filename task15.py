class Notebook:

    def __init__(self, value):
        self._notes = value

    def get_notes(self):
        i = 1
        self._notes.sort()
        for v in self._notes:
            print(f'{i} {v}')
            i += 1

    def set_note(self, value):
        self._notes = value

    note_list = property(fget=get_notes, fset=set_note)


note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
note.note_list
