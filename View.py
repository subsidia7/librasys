import Constants
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QMenu, qApp, QAction, QTabWidget, QTableWidget, QAbstractItemView


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        _widget = QWidget()
        h_box = QHBoxLayout()
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(False)
        h_box.addWidget(self.tabs)
        _widget.setLayout(h_box)
        self.setCentralWidget(_widget)
        self.init_menu()
        self.add_books_tab()
        self.add_readers_tab()
        self.add_issues_tab()
        self.enable()

    def init_menu(self):
        # menu_bar
        _menu_bar = self.menuBar()
        self.init_file_menu(_menu_bar)

    def init_file_menu(self, _menu_bar):
        # creating file menu
        _file_menu = _menu_bar.addMenu("Файл")
        
        # issuing submenu
        self._update_tables_action = QAction("Обновить таблицу", self)
        _file_menu.addAction(self._update_tables_action)

        # issuing submenu
        self._issuing_action = QAction("Выдать книгу", self)
        _file_menu.addAction(self._issuing_action)

        # issuing submenu
        self._accepting_action = QAction("Принять книгу", self)
        _file_menu.addAction(self._accepting_action)

        # adding submenu
        _adding_menu = QMenu("Добавить", self)
        self._add_book_action = QAction("Книгу", self)
        self._add_reader_action = QAction("Читателя", self)
        _adding_menu.addActions([self._add_book_action, self._add_reader_action])
        _file_menu.addMenu(_adding_menu)
        
        # deleting submenu
        _deliting_menu = QMenu("Удалить", self)
        self._delete_book_action = QAction("Книгу", self)
        self._delete_reader_action = QAction("Читателя", self)
        _deliting_menu.addActions([self._delete_book_action, self._delete_reader_action])
        _file_menu.addMenu(_deliting_menu)
        
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

    def add_books_tab(self):
        self.books_tab = QWidget()
        self.tabs.addTab(self.books_tab, Constants.BOOKS_TAB)
        tab_h_box = QHBoxLayout()

        # Set up the books table
        self.books_table = QTableWidget()
        self.books_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.books_table.setColumnCount(9)
        self.books_table.setHorizontalHeaderLabels(["ID книги", "Название книги", "Авторы", "Год Издания", "Место издания", "Фондовый номер", "УДК", "ББК", "Количество экземпляров"])
        tab_h_box.addWidget(self.books_table)

        self.books_tab.setLayout(tab_h_box)

    def add_readers_tab(self):
        self.readers_tab = QWidget()
        self.tabs.addTab(self.readers_tab, Constants.READERS_TAB)
        tab_h_box = QHBoxLayout()
        
        # Set up the readers table
        self.readers_table = QTableWidget()
        self.readers_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.readers_table.setColumnCount(8)
        self.readers_table.setHorizontalHeaderLabels(["Номер читательского билета", "Фамилия", "Имя", "Отчество", "Номер паспорта", "Адрес", "Номер телефона", "Штраф"])
        tab_h_box.addWidget(self.readers_table)
        self.readers_table.resizeColumnsToContents()

        self.readers_tab.setLayout(tab_h_box)

    def add_issues_tab(self):
        self.issues_tab = QWidget()
        self.tabs.addTab(self.issues_tab, Constants.ISSUES_TAB)
        tab_h_box = QHBoxLayout()

        # Set up the issues table
        self.issues_table = QTableWidget()
        self.issues_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.issues_table.setColumnCount(4)
        self.issues_table.setHorizontalHeaderLabels(["ID книги", "Номер читательского билета", "Дата выдачи", "Срок выдачи"])
        tab_h_box.addWidget(self.issues_table)
        self.issues_table.resizeColumnsToContents()

        self.issues_tab.setLayout(tab_h_box)
