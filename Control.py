class Controller:
    def __init__(self, model, view):
        self.MODEL = model
        self.VIEW = view
        self.set_triggers()
    
    def set_triggers(self):
        # file actions
        self.VIEW._issuing_action.triggered.connect(self.issue_book)
        self.VIEW._accepting_action.triggered.connect(self.accept_book)
        self.VIEW._add_book_action.triggered.connect(self.add_book)
        self.VIEW._add_reader_action.triggered.connect(self.add_reader)
        self.VIEW._delete_book_action.triggered.connect(self.delete_book)
        self.VIEW._delete_reader_action.triggered.connect(self.delete_reader)



    def add_book(self):
        pass

    def add_reader(self):
        pass

    def delete_book(self):
        pass

    def delete_reader(self):
        pass

    def issue_book(self):
        pass

    def accept_book(self):
        pass


    