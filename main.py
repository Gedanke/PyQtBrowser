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


def test_js_broswer():
    """

    :return:
    """
    app = QApplication(sys.argv)
    b = Browser()
    b.load('http://www.flyscoot.com/')
    sys.exit(app.exec_())


if __name__ == "__main__":
    """"""
    test_browser()
    # test_browser_ui()
    # from selenium import webdriver
    # import time
    #
    # wd = webdriver.Chrome()
    # wd.get("https://www.crunchbase.com/app/search/companies/")  # 打开百度浏览器
    # time.sleep(60)
    # wd.quit()  # 关闭浏览器
