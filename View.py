import Constants
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QMenu, qApp, QAction


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        _widget = QWidget()
        h_box = QHBoxLayout()
        _widget.setLayout(h_box)
        self.init_menu()
        self.enable()

    def init_menu(self):
        # menu_bar
        _menu_bar = self.menuBar()
        self.init_file_menu(_menu_bar)

    def init_file_menu(self, _menu_bar):
        # creating file menu
        _file_menu = _menu_bar.addMenu("Файл")
        _adding_menu = QMenu("Добавить", self)
        self._add_book_action = QAction("Книгу", self)
        self._add_reader_action = QAction("Читателя", self)
        _adding_menu.addActions([self._add_book_action, self._add_reader_action])
        _file_menu.addMenu(_adding_menu)
        
        # exit button
        self.exit_action = QAction("Выход", self)
        _file_menu.addAction(self.exit_action)
        self.exit_action.triggered.connect(qApp.quit)
        
        # separate exit and others by line
        _file_menu.insertSeparator(self.exit_action)

    def enable(self):
        self.resize(Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT)
        #self.showMaximized()
        self.setWindowTitle(Constants.PROGRAM_TITLE)
        self.show()
