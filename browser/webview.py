# -*- coding: utf-8 -*-


from PyQt5.QtCore import pyqtSlot, QUrl, QEvent, Qt, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication, QTabWidget, QMessageBox, QWidget, QVBoxLayout, QCompleter
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from .ui import UiMainWindow

'''
https://bot.sannysoft.com/
https://www.crunchbase.com/app/search/companies/
https://www.imperva.com/products/advanced-bot-protection-management/?redirect=Distil
'''


class NewWebView(QWebEngineView):
    def __init__(self, tabWidget):
        super().__init__()
        self.tabWidget = tabWidget

    def createWindow(self, WebWindowType):
        new_webview = NewWebView(self.tabWidget)
        self.tabWidget.newTab(new_webview)
        return new_webview


class WebView(QMainWindow, UiMainWindow):
    """

    """

    def __init__(self, parent=None):
        """

        :param parent:
        """
        super(WebView, self).__init__(parent)
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        """

        :return:
        """
        self.progressBar.hide()
        self.showMaximized()
        # self.tabWidget.setTabShape(QTabWidget.Triangular)
        # self.tabWidget.setDocumentMode(True)
        # self.tabWidget.setMovable(True)
        # self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.closeTab)
        self.tabWidget.currentChanged.connect(self.tabChange)
        self.view = NewWebView(self)
        self.view.load(QUrl("https://www.xuexi.cn/"))
        self.newTab(self.view)
        self.lineEdit.installEventFilter(self)
        self.lineEdit.setMouseTracking(True)
        settings = QWebEngineSettings.defaultSettings()
        settings.setAttribute(QWebEngineSettings.WebAttribute.PluginsEnabled, True)
        # settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.getModel()

    def getModel(self):
        """

        :return:
        """
        self.m_model = QStandardItemModel(0, 1, self)
        m_completer = QCompleter(self.m_model, self)
        self.lineEdit.setCompleter(m_completer)
        m_completer.activated[str].connect(self.onUrlChoosed)

    def newTab(self, view):
        """

        :param view:
        :return:
        """
        self.pb_forward.setEnabled(False)
        self.pb_back.setEnabled(False)
        view.titleChanged.connect(self.webTitle)
        view.iconChanged.connect(self.webIcon)
        view.loadProgress.connect(self.webProgress)
        view.loadFinished.connect(self.webProgressEnd)
        view.urlChanged.connect(self.webHistory)
        view.page().linkHovered.connect(self.showUrl)
        currentUrl = self.getUrl(view)

        self.lineEdit.setText(currentUrl)
        self.tabWidget.addTab(view, "新标签页")
        self.tabWidget.setCurrentWidget(view)

    def getUrl(self, webview):
        """

        :param webview:
        :return:
        """
        url = webview.url().toString()
        return url

    def closeTab(self, index):
        """

        :param index:
        :return:
        """
        if self.tabWidget.count() > 1:
            self.tabWidget.widget(index).deleteLater()
            self.tabWidget.removeTab(index)
        elif self.tabWidget.count() == 1:
            self.tabWidget.removeTab(0)
            self.on_pb_new_clicked()

    def tabChange(self, index):
        """

        :param index:
        :return:
        """
        currentView = self.tabWidget.widget(index)
        if currentView:
            currentViewUrl = self.getUrl(currentView)
            self.lineEdit.setText(currentViewUrl)

    def closeEvent(self, event):
        """

        :param event:
        :return:
        """
        tabNum = self.tabWidget.count()
        closeInfo = "你打开了{}个标签页，现在确认关闭？".format(tabNum)
        if tabNum > 1:
            r = QMessageBox.question(self, "关闭浏览器", closeInfo, QMessageBox.Ok | QMessageBox.Cancel,
                                     QMessageBox.Cancel)
            if r == QMessageBox.Ok:
                event.accept()
            elif r == QMessageBox.Cancel:
                event.ignore()
        else:
            event.accept()

    def eventFilter(self, object, event):
        """

        :param object:
        :param event:
        :return:
        """
        if object == self.lineEdit:
            if event.type() == QEvent.MouseButtonRelease:
                self.lineEdit.selectAll()
            elif event.type() == QEvent.KeyPress:
                if event.key() == Qt.Key_Return:
                    self.on_pb_go_clicked()
        return QObject.eventFilter(self, object, event)

    def webTitle(self, title):
        """

        :param title:
        :return:
        """
        index = self.tabWidget.currentIndex()
        if len(title) > 16:
            title = title[0:17]
        self.tabWidget.setTabText(index, title)

    def webIcon(self, icon):
        """

        :param icon:
        :return:
        """
        index = self.tabWidget.currentIndex()
        self.tabWidget.setTabIcon(index, icon)

    def webProgress(self, progress):
        """

        :param progress:
        :return:
        """
        self.progressBar.show()
        self.progressBar.setValue(progress)

    def webProgressEnd(self, isFinished):
        """

        :param isFinished:
        :return:
        """
        if isFinished:
            self.progressBar.setValue(100)
            self.progressBar.hide()
            self.progressBar.setValue(0)

    def webHistory(self, url):
        """

        :param url:
        :return:
        """
        self.lineEdit.setText(url.toString())
        index = self.tabWidget.currentIndex()
        currentView = self.tabWidget.currentWidget()
        history = currentView.history()
        if history.count() > 1:
            if history.currentItemIndex() == history.count() - 1:
                self.pb_back.setEnabled(True)
                self.pb_forward.setEnabled(False)
            elif history.currentItemIndex() == 0:
                self.pb_back.setEnabled(False)
                self.pb_forward.setEnabled(True)
            else:
                self.pb_back.setEnabled(True)
                self.pb_forward.setEnabled(True)

    def showUrl(self, url):
        """

        :param url:
        :return:
        """
        self.statusBar.showMessage(url)

    def onUrlChoosed(self, url):
        """

        :param url:
        :return:
        """
        self.lineEdit.setText(url)

    @pyqtSlot(str)
    def on_lineEdit_textChanged(self, text):
        """

        :param text:
        :return:
        """

        urlGroup = text.split(".")

        if len(urlGroup) == 3 and urlGroup[-1]:
            return
        elif len(urlGroup) == 3 and not (urlGroup[-1]):
            wwwList = ["com", "cn", "net", "org", "gov", "cc"]
            self.m_model.removeRows(0, self.m_model.rowCount())
            for i in range(0, len(wwwList)):
                self.m_model.insertRow(0)
                self.m_model.setData(self.m_model.index(0, 0), text + wwwList[i])

    @pyqtSlot()
    def on_pb_new_clicked(self):
        """

        :return:
        """
        newView = NewWebView(self)
        self.newTab(newView)
        newView.load(QUrl(""))

    @pyqtSlot()
    def on_pb_forward_clicked(self):
        """

        :return:
        """
        self.tabWidget.currentWidget().forward()

    @pyqtSlot()
    def on_pb_back_clicked(self):
        """

        :return:
        """
        self.tabWidget.currentWidget().back()

    @pyqtSlot()
    def on_pb_refresh_clicked(self):
        """

        :return:
        """
        self.tabWidget.currentWidget().reload()

    @pyqtSlot()
    def on_pb_stop_clicked(self):
        """

        :return:
        """
        self.tabWidget.currentWidget().stop()

    @pyqtSlot()
    def on_pb_go_clicked(self):
        """

        :return:
        """
        url = self.lineEdit.text()
        if url[0:7] == "http://" or url[0:8] == "https://":
            qurl = QUrl(url)
        else:
            qurl = QUrl("http://" + url)
        self.tabWidget.currentWidget().load(qurl)

    @pyqtSlot()
    def on_pb_home_clicked(self):
        """

        :return:
        """
        homeurl = QUrl("https://www.sogou.com/")
        if self.tabWidget.currentWidget().title() == "about:blank":
            self.tabWidget.currentWidget().load(homeurl)
        else:
            newView = NewWebView(self)
            self.newTab(newView)
            newView.load(homeurl)

    def __del__(self):
        self.view.deleteLater()
