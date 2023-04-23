# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets

PATH = "../resources/photos/"
photos_path = {
    "page_new": PATH + "new.png",
    "page_home": PATH + "home.png",
    "page_forward": PATH + "forward.ico",
    "page_back": PATH + "back.ico",
    "page_refresh": PATH + "refresh.ico",
    "page_stop": PATH + "stop.ico",
    "page_go": PATH + "go.png"
}


class UiMainWindow:
    """

    """

    def __init__(self, main_window):
        """

        :param main_window:
        """
        self.main_window = main_window
        self.main_window.setObject("MainWindow")
        self.main_window.resize(1600, 900)
        '''设置 ui'''
        self.center_widget = QtWidgets.QWidget(self.main_window)
        self.vertical_layout = QtWidgets.QVBoxLayout(self.center_widget)
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout2 = QtWidgets.QHBoxLayout()
        self.page_new = QtWidgets.QPushButton(self.center_widget)
        self.page_home = QtWidgets.QPushButton(self.center_widget)
        self.page_forward = QtWidgets.QPushButton(self.center_widget)
        self.page_back = QtWidgets.QPushButton(self.center_widget)
        self.page_refresh = QtWidgets.QPushButton(self.center_widget)
        self.page_stop = QtWidgets.QPushButton(self.center_widget)
        self.page_go = QtWidgets.QPushButton(self.center_widget)
        self.table_widget = QtWidgets.QTabWidget(self.center_widget)
        '''icon'''
        self.icon_new = QtGui.QIcon()
        self.icon_home = QtGui.QIcon()
        self.icon_forward = QtGui.QIcon()
        self.icon_back = QtGui.QIcon()
        self.icon_refresh = QtGui.QIcon()
        self.icon_stop = QtGui.QIcon()
        self.icon_go = QtGui.QIcon()
        '''lineEdit'''
        self.line_edit = QtWidgets.QLineEdit(self.center_widget)
        '''progressBar'''
        self.progress_bar = QtWidgets.QProgressBar(self.center_widget)
        '''size_policy'''
        self.size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        '''status_bar'''
        self.status_bar = QtWidgets.QStatusBar(self.main_window)

    def set_ui(self):
        """
        设置 ui
        :return:
        """
        '''设置 ui 的具体属性'''
        self.center_widget.setObjectName("centerWidget")
        self.vertical_layout.setObjectName("verticalLayout")
        self.horizontal_layout.setObjectName("horizontalLayout")
        self.horizontal_layout2.setObjectName("horizontalLayout2")
        '''icon'''
        self.icon_new.addPixmap(QtGui.QPixmap(photos_path["page_new"]))
        self.page_new.setIcon(self.icon_new)
        self.page_new.setObjectName("pageNew")
        self.horizontal_layout.addWidget(self.page_new)
        self.icon_home.addPixmap(QtGui.QPixmap(photos_path["page_home"]))
        self.page_home.setIcon(self.page_home)
        self.page_home.setObjectName("pageHome")
        self.horizontal_layout.addWidget(self.page_home)

    def translate_ui_text(self, main_window):
        """
        设置 UI 内容
        :param main_window: 空白主窗口
        :return:
        """
