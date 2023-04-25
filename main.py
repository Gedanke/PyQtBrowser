# -*- coding: utf-8 -*-


from browser import *
import sys


def test_browser_ui():
    """

    :return:
    """
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


def test_browser():
    """

    :return:
    """
    app = QApplication(sys.argv)
    wv = WebView()
    wv.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    """"""
    test_browser()
    # test_browser_ui()
