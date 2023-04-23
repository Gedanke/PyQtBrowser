# 基于 PyQt5 的浏览器

该项目有以下功能：

* 浏览网页、音乐、玩 flash 游戏、看视频
* 基本浏览器操作：新建页面、主页、前进、后退、刷新、停止、开始
* 网页载入进度显示
* url 地址栏点击后自动全选
* 输入 url 后自定添加网址后缀
* 鼠标移动到 url 上状态栏会显示当前链接

---

## 简单的介绍

Qt WebEngine 提供了渲染动态 Web 内容区域的功能

Qt WebEngine 中的功能分为以下几个模块：

* `QtWebEngineCore`：提供 `QtWebEngine` 和 `QtWebEngineWidgets` 共享的公共 API
* `QtWebEngine`：提供用于在 QML 应用程序中呈现 Web 内容的 QML 类型
* `QtWebEngineWidgets`：提供用于在基于 QWidget 的应用程序中呈现 Web 内容的 C++ 类

这里主要可能会用到第 1、3 两个类，其中第 2 个类不再我讨论范围

其中 `QtWebEngineCore` 类包含了如下几个子类：

* `QWebEngineCookieStore.FilterRequest`：此结构与 `QWebEngineCookieStore.setCookieFilter()` 一起使用，并且是 `filterCallback` 操作的类型
* `QWebEngineCookieStore`：访问 Chromium 的 cookie 
* `QWebEngineHttpRequest`：保留与 `WebEngine` 一起发送的请求 
* `QWebEngineQuotaRequest`：允许接受或拒绝比文件系统API中应用程序当前分配更大的持久存储的请求 
* `QWebEngineRegisterProtocolHandlerRequest`：允许接受或拒绝来自 `registerProtocolHandler` API 的请求 
* `QWebEngineUrlRequestInfo`：有关 URL 请求的信息 
* `QWebEngineUrlRequestInterceptor`：URL 拦截的抽象基类 
* `QWebEngineUrlRequestJob`：表示自定义 URL 请求 
* `QWebEngineUrlSchemeHandler`：用于处理自定义 URL 方案的基类

`QtWebEngineWidgets` 类包含了如下几个子类：

* `QWebEngineCertificateError`：有关证书错误的信息
* `QWebEngineContextMenuData`：用于使用操作填充或扩展上下文菜单的上下文数据
* `QWebEngineDownloadItem`：有关下载的信息
* `QWebEngineFullScreenRequest`：允许接受或拒绝进入和退出全屏模式的请求
* `QWebEngineHistory`：表示 Web 引擎页面的历史记录
* `QWebEngineHistoryItem`：表示 Web 引擎页面历史记录中的一个项目
* `QWebEnginePage`：用于查看和编辑 Web 文档的对象
* `QWebEngineProfile`：多个页面共享的 Web 引擎配置文件
* `QWebEngineScript`：封装 JavaScript 程序
* `QWebEngineScriptCollection`：表示用户脚本的集合 
* `QWebEngineSettings`：用于存储 `QWebEnginePage` 使用的设置的对象 
* `QWebEngineView`：用于查看和编辑 Web 文档的小组件

通过这些类我们构建一个“谷歌心、自己功能”的浏览器基本上就没有问题了

---

## 核心代码

浏览器：

* NewWebView
  * `createWindows()`
* WebView
  * `initUi()`：一些基础设置 
  * `getModel()`：网站链接补全模型 
  * `newTab()`：新标签页
  * `getUr()`：网站 url 
  * `closeTab()`：关闭标签
  * `tabChange()`：标签切换
  * `closeEvent()`：关闭事件 
  * `eventFilter()`：事件过滤器
  * `webTitle()`：网站标题 
  * `webIcon()`：网站图标
  * `webProgress()`：网站加载进度
  * `webHistory()`：网站浏览历史 
  * `showUrl()`：显示 url
  * `lineEditTextChanged()`：地址栏变换
  * `pageNewClicked()`：打开新标签页 
  * `pageForwardClicked()`：前选 
  * `pageBackClicked()`：后退 
  * `pageRefreshClicked()`：刷新 
  * `pageStopClicked()`：停止
  * `pageGoClicked()`：开始 
  * `pageHomeClicked()`：主页

我们要能够打开网页需要重载 `QWebEngineView` 的 `createWindow()` 函数；在实现的类中大约有 20 多个函数

---

##  

本项目参考了[链接](https://zhuanlan.zhihu.com/p/49439814)


---
