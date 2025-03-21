# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt5ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(612, 589)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 0, 561, 309))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.main_ui = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.main_ui.setContentsMargins(0, 0, 0, 0)
        self.main_ui.setSpacing(10)
        self.main_ui.setObjectName("main_ui")
        self.name_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(72)
        self.name_label.setFont(font)
        self.name_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.main_ui.addWidget(self.name_label)
        self.pick_name_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(22)
        self.pick_name_button.setFont(font)
        self.pick_name_button.setStyleSheet("QPushButton {\n"
"    padding: 20px;\n"
"}\n"
"")
        self.pick_name_button.setObjectName("pick_name_button")
        self.main_ui.addWidget(self.pick_name_button)
        self.reset_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.reset_button.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.reset_button.setFont(font)
        self.reset_button.setStyleSheet("QPushButton {\n"
"    padding: 10px;\n"
"}\n"
"")
        self.reset_button.setObjectName("reset_button")
        self.main_ui.addWidget(self.reset_button)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 310, 561, 171))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.config_ui = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.config_ui.setContentsMargins(0, 0, 0, 0)
        self.config_ui.setObjectName("config_ui")
        self.config_ui_1 = QtWidgets.QHBoxLayout()
        self.config_ui_1.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.config_ui_1.setContentsMargins(50, -1, -1, -1)
        self.config_ui_1.setSpacing(7)
        self.config_ui_1.setObjectName("config_ui_1")
        self.n_pick_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.n_pick_checkbox.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.n_pick_checkbox.setFont(font)
        self.n_pick_checkbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.n_pick_checkbox.setObjectName("n_pick_checkbox")
        self.config_ui_1.addWidget(self.n_pick_checkbox)
        self.g_names_pick_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.g_names_pick_checkbox.setFont(font)
        self.g_names_pick_checkbox.setObjectName("g_names_pick_checkbox")
        self.config_ui_1.addWidget(self.g_names_pick_checkbox)
        self.b_names_pick_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.b_names_pick_checkbox.setFont(font)
        self.b_names_pick_checkbox.setObjectName("b_names_pick_checkbox")
        self.config_ui_1.addWidget(self.b_names_pick_checkbox)
        self.config_ui.addLayout(self.config_ui_1)
        self.config_ui_2 = QtWidgets.QHBoxLayout()
        self.config_ui_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.config_ui_2.setContentsMargins(50, -1, -1, -1)
        self.config_ui_2.setSpacing(7)
        self.config_ui_2.setObjectName("config_ui_2")
        self.pick_again_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.pick_again_checkbox.setFont(font)
        self.pick_again_checkbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pick_again_checkbox.setObjectName("pick_again_checkbox")
        self.config_ui_2.addWidget(self.pick_again_checkbox)
        self.pick_time_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.pick_time_checkbox.setFont(font)
        self.pick_time_checkbox.setObjectName("pick_time_checkbox")
        self.config_ui_2.addWidget(self.pick_time_checkbox)
        self.pick_read_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.pick_read_checkbox.setFont(font)
        self.pick_read_checkbox.setObjectName("pick_read_checkbox")
        self.config_ui_2.addWidget(self.pick_read_checkbox)
        self.config_ui.addLayout(self.config_ui_2)
        self.config_ui_3 = QtWidgets.QHBoxLayout()
        self.config_ui_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.config_ui_3.setContentsMargins(50, -1, -1, -1)
        self.config_ui_3.setSpacing(7)
        self.config_ui_3.setObjectName("config_ui_3")
        self.pick_animation_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.pick_animation_checkbox.setFont(font)
        self.pick_animation_checkbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pick_animation_checkbox.setObjectName("pick_animation_checkbox")
        self.config_ui_3.addWidget(self.pick_animation_checkbox)
        self.is_save_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.is_save_checkbox.setFont(font)
        self.is_save_checkbox.setObjectName("is_save_checkbox")
        self.config_ui_3.addWidget(self.is_save_checkbox)
        self.checkBox_12 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_12.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.checkBox_12.setFont(font)
        self.checkBox_12.setObjectName("checkBox_12")
        self.config_ui_3.addWidget(self.checkBox_12)
        self.config_ui.addLayout(self.config_ui_3)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 480, 561, 55))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.timer_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        self.timer_label.setFont(font)
        self.timer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.timer_label.setObjectName("timer_label")
        self.verticalLayout.addWidget(self.timer_label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 612, 26))
        self.menubar.setObjectName("menubar")
        self.menu_about = QtWidgets.QMenu(self.menubar)
        self.menu_about.setObjectName("menu_about")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.update_action = QtWidgets.QAction(MainWindow)
        self.update_action.setObjectName("update_action")
        self.about_action = QtWidgets.QAction(MainWindow)
        self.about_action.setObjectName("about_action")
        self.github_action = QtWidgets.QAction(MainWindow)
        self.github_action.setObjectName("github_action")
        self.exit_action = QtWidgets.QAction(MainWindow)
        self.exit_action.setObjectName("exit_action")
        self.menu_about.addAction(self.about_action)
        self.menu_about.addAction(self.exit_action)
        self.menu_about.addSeparator()
        self.menu_about.addAction(self.update_action)
        self.menu_about.addAction(self.github_action)
        self.menubar.addAction(self.menu_about.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name_label.setText(_translate("MainWindow", "请抽取"))
        self.pick_name_button.setText(_translate("MainWindow", ">>> 抽取 <<<"))
        self.reset_button.setText(_translate("MainWindow", "重置名单"))
        self.n_pick_checkbox.setText(_translate("MainWindow", "均衡模式"))
        self.g_names_pick_checkbox.setText(_translate("MainWindow", "只抽女生"))
        self.b_names_pick_checkbox.setText(_translate("MainWindow", "只抽男生"))
        self.pick_again_checkbox.setText(_translate("MainWindow", "允许重复抽取"))
        self.pick_time_checkbox.setText(_translate("MainWindow", "计时器"))
        self.pick_read_checkbox.setText(_translate("MainWindow", "开启播报(测试)"))
        self.pick_animation_checkbox.setText(_translate("MainWindow", "开启动画"))
        self.is_save_checkbox.setText(_translate("MainWindow", "退出保存"))
        self.checkBox_12.setText(_translate("MainWindow", "开发中..."))
        self.timer_label.setText(_translate("MainWindow", "0.0s"))
        self.menu_about.setTitle(_translate("MainWindow", "程序"))
        self.update_action.setText(_translate("MainWindow", "检查更新"))
        self.about_action.setText(_translate("MainWindow", "程序简介"))
        self.github_action.setText(_translate("MainWindow", "打开 Github 仓库"))
        self.exit_action.setText(_translate("MainWindow", "退出程序"))
