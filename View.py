import Constants
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QMenu, qApp, QAction, QTabWidget, QTableWidget, QAbstractItemView, QTableView
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('icons/library.ico'))
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
        self._update_tables_action = QAction(QIcon(r"icons/update.ico"), "Обновить таблицу", self)
        _file_menu.addAction(self._update_tables_action)

        # issuing submenu
        self._issuing_action = QAction(QIcon(r"icons/issue.ico"), "Выдать книгу", self)
        _file_menu.addAction(self._issuing_action)

        # issuing submenu
        self._accepting_action = QAction(QIcon(r"icons/accept.ico"), "Принять книгу", self)
        _file_menu.addAction(self._accepting_action)

        # adding submenu
        _adding_menu = QMenu("Добавить", self)
        self._add_book_action = QAction(QIcon(r"icons/add.ico"), "Книгу", self)
        self._add_reader_action = QAction(QIcon(r"icons/add.ico"), "Читателя", self)
        _adding_menu.addActions([self._add_book_action, self._add_reader_action])
        _file_menu.addMenu(_adding_menu)
        
        # deleting submenu
        _deliting_menu = QMenu("Удалить", self)
        self._delete_book_action = QAction(QIcon(r"icons/delete.ico"),"Книгу", self)
        self._delete_reader_action = QAction(QIcon(r"icons/delete.ico"),"Читателя", self)
        _deliting_menu.addActions([self._delete_book_action, self._delete_reader_action])
        _file_menu.addMenu(_deliting_menu)
        
        # exit button
        self.exit_action = QAction(QIcon(r"icons/exit.ico"), "Выход", self)
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
        self.books_table = QTableView()
        '''self.books_table.setColumnCount(9)
        self.books_table.setHorizontalHeaderLabels(["ID книги", "Название книги", "Авторы", "Год Издания", "Место издания", "Фондовый номер", "УДК", "ББК", "Количество экземпляров"])
        '''
        tab_h_box.addWidget(self.books_table)
        self.books_tab.setLayout(tab_h_box)

        self.model = QSqlTableModel(self)
        self.model.setTable("Books")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.setHeaderData(0, Qt.Horizontal, "Код книги")
        self.model.setHeaderData(1, Qt.Horizontal, "Название книги")
        self.model.setHeaderData(2, Qt.Horizontal, "Авторы")
        self.model.setHeaderData(3, Qt.Horizontal, "Год Издания")
        self.model.setHeaderData(4, Qt.Horizontal, "Место издания")
        self.model.setHeaderData(5, Qt.Horizontal, "Фондовый номер")
        self.model.setHeaderData(6, Qt.Horizontal, "УДК")
        self.model.setHeaderData(7, Qt.Horizontal, "ББК")
        self.model.setHeaderData(8, Qt.Horizontal, "Количество экземпляров")
        self.model.select()
        # Set up the view

        self.view = QTableView()
        self.books_table.setModel(self.model)
        self.books_table.resizeColumnsToContents()

    def add_readers_tab(self):
        self.readers_tab = QWidget()
        self.tabs.addTab(self.readers_tab, Constants.READERS_TAB)
        tab_h_box = QHBoxLayout()
        
        # Set up the readers table
        self.readers_table = QTableView()
        '''
        self.readers_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.readers_table.setColumnCount(8)
        self.readers_table.setHorizontalHeaderLabels(["Номер читательского билета", "Фамилия", "Имя", "Отчество", "Номер паспорта", "Адрес", "Номер телефона", "Штраф"])
        '''
        tab_h_box.addWidget(self.readers_table)
        self.readers_tab.setLayout(tab_h_box)

        self.model = QSqlTableModel(self)
        self.model.setTable("Readers")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.setHeaderData(0, Qt.Horizontal, "Номер читательского билета")
        self.model.setHeaderData(1, Qt.Horizontal, "Фамилия")
        self.model.setHeaderData(2, Qt.Horizontal, "Имя")
        self.model.setHeaderData(3, Qt.Horizontal, "Отчество")
        self.model.setHeaderData(4, Qt.Horizontal, "Номер паспорта")
        self.model.setHeaderData(5, Qt.Horizontal, "Адрес")
        self.model.setHeaderData(6, Qt.Horizontal, "Номер телефона")
        self.model.setHeaderData(7, Qt.Horizontal, "Штраф")
        self.model.select()

        self.view = QTableView()
        self.readers_table.setModel(self.model)
        self.readers_table.resizeColumnsToContents()

    def add_issues_tab(self):
        self.issues_tab = QWidget()
        self.tabs.addTab(self.issues_tab, Constants.ISSUES_TAB)
        tab_h_box = QHBoxLayout()

        # Set up the issues table
        self.issues_table = QTableView()
        '''
        self.issues_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.issues_table.setColumnCount(4)
        self.issues_table.setHorizontalHeaderLabels(["ID книги", "Номер читательского билета", "Дата выдачи", "Срок выдачи"])
        '''
        tab_h_box.addWidget(self.issues_table)
        self.issues_tab.setLayout(tab_h_box)

        self.model = QSqlTableModel(self)
        self.model.setTable("Issues")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.setHeaderData(0, Qt.Horizontal, "Код выдачи")
        self.model.setHeaderData(1, Qt.Horizontal, "Код книги")
        self.model.setHeaderData(2, Qt.Horizontal, "Номер читательского билета")
        self.model.setHeaderData(3, Qt.Horizontal, "Дата выдачи")
        self.model.setHeaderData(3, Qt.Horizontal, "Срок выдачи")
        self.model.select()

        self.view = QTableView()
        self.issues_table.setModel(self.model)
        self.issues_table.resizeColumnsToContents()

        
