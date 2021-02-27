
#import sys
import os
#import json
import cryptography
import time
import ctypes
import telnetlib
from PyQt5 import QtCore, QtGui, QtWidgets
from netmiko import ConnectHandler
import re
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Date, DateTime
from sqlalchemy.orm import sessionmaker
import datetime
from sqlalchemy import text
import webbrowser
import  easygui


Base = declarative_base()

class Ui_UserInfo(Base):
    __tablename__ = 'tbl_Users'
    Id = Column(Integer, primary_key=True)
    UserName = Column(String(250), nullable=False, default="admin")
    Password = Column(String(250), nullable=False, default="cisco")
    Target = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('C:\PlannerProject\pka'))
        MainWindow.resize(790, 602)
        MainWindow.setMinimumSize(QtCore.QSize(790, 602))
        MainWindow.setMaximumSize(QtCore.QSize(790, 602))
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 771, 171))
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 50, 81, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 110, 81, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 80, 81, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 140, 81, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(100, 20, 81, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(100, 80, 81, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setGeometry(QtCore.QRect(100, 50, 81, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_9.setGeometry(QtCore.QRect(100, 110, 81, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_10.setGeometry(QtCore.QRect(100, 140, 81, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_11.setGeometry(QtCore.QRect(210, 20, 81, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_12.setGeometry(QtCore.QRect(210, 80, 81, 23))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_13.setGeometry(QtCore.QRect(210, 140, 81, 23))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_14.setGeometry(QtCore.QRect(210, 50, 81, 23))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_15.setGeometry(QtCore.QRect(210, 110, 81, 23))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_16.setGeometry(QtCore.QRect(300, 140, 81, 23))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_17.setGeometry(QtCore.QRect(300, 20, 81, 23))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_18.setGeometry(QtCore.QRect(300, 50, 81, 23))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_19.setGeometry(QtCore.QRect(300, 80, 81, 23))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_20.setGeometry(QtCore.QRect(300, 110, 81, 23))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_21.setGeometry(QtCore.QRect(410, 50, 81, 23))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_22.setGeometry(QtCore.QRect(410, 20, 81, 23))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_23.setGeometry(QtCore.QRect(410, 140, 81, 23))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_24.setGeometry(QtCore.QRect(410, 80, 81, 23))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_25.setGeometry(QtCore.QRect(410, 110, 81, 23))
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_26.setGeometry(QtCore.QRect(500, 50, 81, 23))
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_27.setGeometry(QtCore.QRect(500, 20, 81, 23))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_28.setGeometry(QtCore.QRect(500, 140, 81, 23))
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_29.setGeometry(QtCore.QRect(500, 80, 81, 23))
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_30.setGeometry(QtCore.QRect(500, 110, 81, 23))
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_31.setGeometry(QtCore.QRect(590, 50, 81, 23))
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_32.setGeometry(QtCore.QRect(590, 20, 81, 23))
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_33 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_33.setGeometry(QtCore.QRect(590, 140, 81, 23))
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_34.setGeometry(QtCore.QRect(590, 80, 81, 23))
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_35.setGeometry(QtCore.QRect(590, 110, 81, 23))
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_36 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_36.setGeometry(QtCore.QRect(680, 50, 81, 23))
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_37 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_37.setGeometry(QtCore.QRect(680, 20, 81, 23))
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_38 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_38.setGeometry(QtCore.QRect(680, 140, 81, 23))
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_39 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_39.setGeometry(QtCore.QRect(680, 80, 81, 23))
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_40 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_40.setGeometry(QtCore.QRect(680, 110, 81, 23))
        self.pushButton_40.setObjectName("pushButton_40")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 180, 771, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 131, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Source IP Address")
        self.pushButton_41 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_41.setGeometry(QtCore.QRect(680, 10, 75, 23))
        self.pushButton_41.setObjectName("pushButton_41")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox_2)
        self.dateEdit.setGeometry(QtCore.QRect(580, 10, 81, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(10, 50, 121, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setToolTip("select button to run with default profile")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(440, 50, 51, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setToolTip("select checkbox and enter a file path to save output")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 10, 141, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("Destination IP Address")
        self.pushButton_42 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_42.setGeometry(QtCore.QRect(680, 40, 75, 23))
        self.pushButton_42.setObjectName("pushButton_42")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(500, 40, 161, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setPlaceholderText("Enter File Path")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(160, 40, 118, 23))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setGeometry(QtCore.QRect(310, 40, 121, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(310, 10, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(620, 530, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 261, 751, 261))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("color:  rgb(255, 255, 255); background-color: rgb(40, 40, 40); font: 12pt");
        #self.textBrowser.setStyleSheet("background-color: rgb(40, 40, 40)")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuConfigure = QtWidgets.QMenu(self.menubar)
        self.menuConfigure.setObjectName("menuConfigure")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionConfigure = QtWidgets.QAction(MainWindow)
        self.actionConfigure.setObjectName("actionConfigure")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionUser_Guide = QtWidgets.QAction(MainWindow)
        self.actionUser_Guide.setObjectName("actionUser_Guide")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionStart = QtWidgets.QAction(MainWindow)
        self.actionStart.setObjectName("actionStart")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionExit_3 = QtWidgets.QAction(MainWindow)
        self.actionExit_3.setObjectName("actionExit_3")
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionUser_Guide)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionUpdate)
        self.menuHelp.addAction(self.actionExit_3)
        self.menuConfigure.addAction(self.actionStart)
        self.menuConfigure.addAction(self.actionExit_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuConfigure.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.Cisco_ShowArp_Button)
        self.pushButton_2.clicked.connect(self.Cisco_IpAddress_Field)
        self.pushButton_3.clicked.connect(self.Cisco_ShowDHCPBinding_Button)
        self.pushButton_4.clicked.connect(self.Cisco_ShowDHCPConflicts_Button)
        self.pushButton_5.clicked.connect(self.Cisco_ShowInterfaces_Button)
        self.pushButton_6.clicked.connect(self.Cisco_ShowMacAddress_Button)
        self.pushButton_7.clicked.connect(self.Cisco_ShowDHCPPool_Button)
        self.pushButton_8.clicked.connect(self.Cisco_ShowRun_Button)
        self.pushButton_9.clicked.connect(self.Cisco_ShowIPRoute_Button)
        self.pushButton_10.clicked.connect(self.Cisco_ShowACL_Button)
        self.pushButton_11.clicked.connect(self.Cisco_ShowVLAN_Button)
        self.pushButton_12.clicked.connect(self.Cisco_ShowLogging_Button)
        self.pushButton_13.clicked.connect(self.Cisco_ShowInterfaceBrief_Button)
        self.pushButton_14.clicked.connect(self.Cisco_ShowOSPFDatabase_Button)
        self.pushButton_15.clicked.connect(self.Cisco_ShowVersion_Button)
        self.pushButton_16.clicked.connect(self.Cisco_ShowBGPSummary_Button)
        self.pushButton_17.clicked.connect(self.Cisco_ShowOSPFNeigbours_Button)
        self.pushButton_18.clicked.connect(self.Cisco_ShowSTP_Button)
        self.pushButton_19.clicked.connect(self.Cisco_ShowUptime_Button)
        self.pushButton_20.clicked.connect(self.Cisco_ShowIOS_Button)
        self.pushButton_21.clicked.connect(self.Cisco_ShowIPTraffic_Button)
        self.pushButton_22.clicked.connect(self.Cisco_ShowNAT_Button)
        self.pushButton_23.clicked.connect(self.Cisco_ShowTrunk_Button)
        self.pushButton_24.clicked.connect(self.Cisco_NTPStatus_Button)
        self.pushButton_25.clicked.connect(self.Cisco_ShowCryptoPolicy_Button)
        self.pushButton_26.clicked.connect(self.Cisco_ClassMap_Button)
        self.pushButton_27.clicked.connect(self.Cisco_ShowInterfaceBits_Button)
        self.pushButton_28.clicked.connect(self.Cisco_ShowClock_Button)
        self.pushButton_29.clicked.connect(self.Cisco_ShowCounterErrors_Button)
        self.pushButton_30.clicked.connect(self.Cisco_ShowVTPStatus_Button)
        self.pushButton_31.clicked.connect(self.Cisco_ShowIPProtocolsSummary_Button)
        self.pushButton_32.clicked.connect(self.Cisco_ClassMap_Button)
        self.pushButton_33.clicked.connect(self.Cisco_NATTranslation_Button)
        self.pushButton_34.clicked.connect(self.Cisco_DefaultGateway_Button)
        self.pushButton_35.clicked.connect(self.Cisco_FreePorts_Button)
        self.pushButton_36.clicked.connect(self.Cisco_ASAVPNSession_Button)
        self.pushButton_37.clicked.connect(self.Cisco_ASAShowIP_Button)
        self.pushButton_38.clicked.connect(self.Cisco_ASAVPNTunnel_Button)
        self.pushButton_39.clicked.connect(self.Cisco_ASAObjectGroup_Button)
        self.pushButton_40.clicked.connect(self.Cisco_ASAServicePolicy_Button)
        self.pushButton_41.clicked.connect(self.ExportFileUi)


        self.comboBox.addItem(self.Operating_System_Combo())
        self.comboBox_2.addItem(self.Device_Type_Combo())
        #self.pushButton_41.clicked.connect(self.ExportFileUi)
        self.buttonBox.accepted.connect(MainWindow.close)
        self.buttonBox.rejected.connect(MainWindow.close)
        self.reset()
        self.reset1()
        self.reset2()

        self.actionExit.triggered.connect(MainWindow.close)
        self.actionStart.triggered.connect(self.openWindow)
        self.actionUpdate.triggered.connect(self.WebBrowserGithub_Menu)
        self.actionUser_Guide.triggered.connect(self.WebBrowserUserGuide_Menu)
        self.actionExport.triggered.connect(self.ExportFileUi)
        #self.actionUser_Guide.triggered.connect('C:\PlannerProject\pka')

    def WebBrowserGithub_Menu(self):
        new = 1
        url = "https://github.com/DNnate/Dante-Toolbox";
        webbrowser.open(url,new=new)

    def WebBrowserUserGuide_Menu(self):
        new = 1
        url = "C:\PlannerProject\HelpGuide";
        webbrowser.open(url,new=new)

        # script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        # rel_path = "C:\PlannerProject\HelpGuide";
        # abs_file_path = os.path.join(script_dir, rel_path)
        # path = os.getcwd() + abs_file_path
        # fp = open(path, 'r+')

    def Operating_System_Combo(self):
        channels = ['Cisco', 'Netgear', 'Juniper']
        for channel in channels:
            self.comboBox.addItem(channel)

    def Device_Type_Combo(self):
        channels = ['Switch', 'Router']
        for channel in channels:
            self.comboBox_2.addItem(channel)


    def ExportFileUi(self):
        try:
            save_dest = easygui.filesavebox()
            #save_dest = QtGui.QFileDialog.getSaveFileName(self, 'Export')
            outfile = open(save_dest, 'w')
            result = self.textBrowser.toPlainText()
            outfile.write(result)
            outfile.close()
        except:
            pass

    def Cisco_ASAObjectGroup_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show run | include object')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ASAShowIP_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show ip address')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ASAServicePolicy_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show service-policy')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ASAVPNSession_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('sh vpn-sessiondb remote')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ASAVPNTunnel_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show run | include vpn')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ClassMap_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show class-map')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_DefaultGateway_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show ip route | include network')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_FreePorts_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show int | i proto|Last in')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_NATTranslation_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show xlate')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_PolicyMap_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show policy-map')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowACL_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show run | include access')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowArp_Button(self):
        try:
            x = self.lineEdit.text()
            y = self.lineEdit_2.text()
            #match = re.search(r"ba[r|z|d]", x.strip())
            #match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text( "SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str =  (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str =  (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show arp')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowBGPSummary_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show ip bgp summary')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowClock_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show clock')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowCounterErrors_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show interface | i line|escription|error')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowCryptoPolicy_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show crypto isakmp policy')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowDHCPBinding_Button(self):
        try:
            x = self.lineEdit.text()
            #match = re.search(r"ba[r|z|d]", x.strip())
            #match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text( "SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str =  (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str =  (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show ip dhcp binding')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowDHCPConflicts_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show ip dhcp conflict')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowDHCPPool_Button(self):
        try:
            x = self.lineEdit.text()
            #match = re.search(r"ba[r|z|d]", x.strip())
            #match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text( "SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str =  (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str =  (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show ip dhcp pool')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowIOS_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show version | include processor')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowInterfaces_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show interfaces')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowInterfaceBrief_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show ip interface brief')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowInterfaceBits_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show interface | i line|escription|bit')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowIPProtocolsSummary_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show ip protocols summary')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowIPRoute_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show ip route')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowIPTraffic_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show ip traffic')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowOSPFDatabase_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show ip ospf database')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowLogging_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show logging')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowMacAddress_Button(self):
        try:
            x = self.lineEdit.text()
            #match = re.search(r"ba[r|z|d]", x.strip())
            #match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text( "SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str =  (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str =  (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show mac-address-table')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowNAT_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show run | include nat')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowOSPFNeigbours_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show ip ospf neighbor')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_NTPStatus_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show ntp status')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowRun_Button(self):
        try:
            x = self.lineEdit.text()
            #match = re.search(r"ba[r|z|d]", x.strip())
            #match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text( "SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str =  (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str =  (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show run')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowSTP_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show spanning-tree')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowTrunk_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show interface trunk')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowUptime_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show version | include uptime')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowVLAN_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show vlan-switch brief')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowVersion_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show version')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_ShowVTPStatus_Button(self):
        try:
            x = self.lineEdit.text()
            # match = re.search(r"ba[r|z|d]", x.strip())
            # match = re.compile("^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$").match(x.strip())
            ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
            ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
            matchHost = re.compile(ValidHostnameRegex).match(x.strip())
            matchIp = re.compile(ValidIpAddressRegex).match(x.strip())
            if matchHost or matchIp:
                pass
            else:
                sys.exit(800)
        except:
            self.textBrowser.setText('Please Enter a Valid IP Address or Host Name')

        else:
            self.completed = 0
            for i in range(0, 100):
                self.progressBar.setValue(i + 30)
                time.sleep(1)
                engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
                conn = engine.connect()
                user = text("SELECT UserName FROM tbl_Users WHERE Id = 1")
                password = text("SELECT Password FROM tbl_Users WHERE Id = 1")
                User_Entry = conn.execute(user).fetchall()
                for u in User_Entry:
                    Dtu_Conver_Str = (str(u))
                    User_From_DB = (Dtu_Conver_Str[2:-3])
                Password_Entry = conn.execute(password).fetchall()
                for p in Password_Entry:
                    Dtp_Conver_Str = (str(p))
                    Password_From_DB = (Dtp_Conver_Str[2:-3])

                self.progressBar.setValue(i + 60)
                time.sleep(1)
                cisco = {
                    'device_type': 'cisco_ios',
                    'host': x,
                    'username': User_From_DB,
                    'password': Password_From_DB,
                }
                try:
                    self.progressBar.setValue(i + 80)
                    net_connect = ConnectHandler(**cisco)
                except (AuthenticationException):
                    self.textBrowser.setText('Incorrect Username or Password: ' + self.lineEdit.text())
                except (NetMikoTimeoutException):
                    self.textBrowser.setText('Timeout to Device: ' + self.lineEdit.text())
                except (EOFError):
                    self.textBrowser.setText('End of File while attempting device: ' + self.lineEdit.text())
                except (SSHException):
                    self.textBrowser.setText('SSH issue. Are you sure SSH is enabled: ' + self.lineEdit.text())
                except Exception as unknown_error:
                    self.textBrowser.setText('Some other Error: ' + unknown_error)
                else:
                    net_connect.send_command
                    output = net_connect.send_command('show VTP status')
                    self.textBrowser.setText(output)
                self.progressBar.setValue(100)
                break

    def Cisco_IpAddress_Field(self):
        self.completed = 0
        #HOST = self.lineEdit.text()
        HOST = "192.168.1.148"
        #DESTINATION = ""
        for i in range (0,100):

        #while self.completed < 100:
            #self.completed += 10
            #time.sleep(1)
            self.progressBar.setValue(i + 30)
            time.sleep(1)
            user = "admin"
            password = "cisco"
            tn = telnetlib.Telnet(HOST)
            tn.read_until(b"Username: ")
            tn.write(user.encode('ascii') + b"\n")
            if password:
                tn.read_until(b"Password: ")
                tn.write(password.encode('ascii') + b"\n")
            self.progressBar.setValue(i + 60)
            time.sleep(1)
            tn.write(b"enable\n")
            tn.write(b"cisco\n")
            # tn.write(b"show run\n")
            self.progressBar.setValue(i + 80)
            tn.write(b"show ip int brief\n")
            tn.write(b"exit\n")
            doc = tn.read_all().decode('ascii')
            self.textBrowser.setText(doc)
            self.progressBar.setValue(100)
            break

    def reset(self):
        engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
        Base.metadata.create_all(engine)
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()
        self.session.commit

    def reset1(self):
        engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
        conn = engine.connect()
        default = text(

             "INSERT INTO tbl_Users(id, UserName, Password)"
            "SELECT * FROM (SELECT 1, 'admin', 'cisco') WHERE NOT EXISTS (SELECT id, UserName FROM tbl_Users WHERE id = 1) LIMIT 1;"
         )
        conn.execute(default)

    def reset2(self):
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(1)
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_4.clear()
        self.radioButton.setAutoExclusive(True)
        self.radioButton.setChecked(False)
        self.textBrowser.setText('')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dante"))
        self.groupBox.setTitle(_translate("MainWindow", "ToolBox"))
        self.pushButton.setText(_translate("MainWindow", "ARP"))
        self.pushButton_2.setText(_translate("MainWindow", "PING"))
        self.pushButton_3.setText(_translate("MainWindow", "DHCP Bindings"))
        self.pushButton_4.setText(_translate("MainWindow", "DHCP Conflicts"))
        self.pushButton_5.setText(_translate("MainWindow", "Interfaces"))
        self.pushButton_6.setText(_translate("MainWindow", "MAC Address"))
        self.pushButton_7.setText(_translate("MainWindow", "Show DHCP"))
        self.pushButton_8.setText(_translate("MainWindow", "Show Run"))
        self.pushButton_9.setText(_translate("MainWindow", "Show Route"))
        self.pushButton_10.setText(_translate("MainWindow", "Show ACL"))
        self.pushButton_11.setText(_translate("MainWindow", "Show VLAN"))
        self.pushButton_12.setText(_translate("MainWindow", "Show Logging"))
        self.pushButton_13.setText(_translate("MainWindow", "Interface Brief"))
        self.pushButton_14.setText(_translate("MainWindow", "Show OSPF"))
        self.pushButton_15.setText(_translate("MainWindow", "Show Version"))
        self.pushButton_16.setText(_translate("MainWindow", "BGP Summary"))
        self.pushButton_17.setText(_translate("MainWindow", "OSPF neighbor"))
        self.pushButton_18.setText(_translate("MainWindow", "STP"))
        self.pushButton_19.setText(_translate("MainWindow", "Show Uptime"))
        self.pushButton_20.setText(_translate("MainWindow", "Show IOSv"))
        self.pushButton_21.setText(_translate("MainWindow", "IP Traffic"))
        self.pushButton_22.setText(_translate("MainWindow", "NAT"))
        self.pushButton_23.setText(_translate("MainWindow", "Show Trunk"))
        self.pushButton_24.setText(_translate("MainWindow", "NTP Status"))
        self.pushButton_25.setText(_translate("MainWindow", "Crypto Info"))
        self.pushButton_26.setText(_translate("MainWindow", "Class Map"))
        self.pushButton_27.setText(_translate("MainWindow", "Line bits/sec"))
        self.pushButton_28.setText(_translate("MainWindow", "Show Clock"))
        self.pushButton_29.setText(_translate("MainWindow", "Counter Errors"))
        self.pushButton_30.setText(_translate("MainWindow", "VTP Status"))
        self.pushButton_31.setText(_translate("MainWindow", "IP Protocols"))
        self.pushButton_32.setText(_translate("MainWindow", "Policy Map"))
        self.pushButton_33.setText(_translate("MainWindow", "xlate"))
        self.pushButton_34.setText(_translate("MainWindow", "Default Route"))
        self.pushButton_35.setText(_translate("MainWindow", "Free Port"))
        self.pushButton_36.setText(_translate("MainWindow", "VPN Session"))
        self.pushButton_37.setText(_translate("MainWindow", "FP/ASA IP"))
        self.pushButton_38.setText(_translate("MainWindow", "Ipsec Policy"))
        self.pushButton_39.setText(_translate("MainWindow", "Object Group"))
        self.pushButton_40.setText(_translate("MainWindow", "Service Policy"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Confugure"))
        self.pushButton_41.setText(_translate("MainWindow", "Export"))
        self.radioButton.setText(_translate("MainWindow", "Run as Administrator"))
        self.checkBox.setText(_translate("MainWindow", "Save"))
        self.pushButton_42.setText(_translate("MainWindow", "Import"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuConfigure.setTitle(_translate("MainWindow", "Configure"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionConfigure.setText(_translate("MainWindow", "Configure"))
        #self.actionConfigure.triggered.connect(self.close)
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionUser_Guide.setText(_translate("MainWindow", "User Guide"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionUpdate.setText(_translate("MainWindow", "github.com"))
        self.actionStart.setText(_translate("MainWindow", "Start"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))
        self.actionExit_3.setText(_translate("MainWindow", "Exit"))


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(179, 95)
        Dialog.setMinimumSize(QtCore.QSize(179, 95))
        Dialog.setMaximumSize(QtCore.QSize(179, 95))
        Dialog.setWindowIcon(QtGui.QIcon('C:\PlannerProject\pka'))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(70, 70, 91, 20))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(62, 10, 111, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 40, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 47, 13))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.accepted.connect(self.AddUserLoginItemUi)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def AddUserLoginItemUi(self):
        try:
            a = self.lineEdit.text()
            b = self.lineEdit_2.text()
            ismatch1 = re.compile("^[a-zA-Z0-9_.-]+$").match(a.strip())
            ismatch2 = re.compile("^[a-zA-Z0-9_.@#$%^&+=-]+$").match(b.strip())
            if ismatch1 and ismatch2:
                pass
            else:
                sys.exit(800)
        except:
            self.Mbox()

        else:
            engine = create_engine('sqlite:///DanteToolbox.db', echo=True)
            Base.metadata.create_all(engine)
            Base.metadata.bind = engine
            DBSession = sessionmaker(bind=engine)
            self.session = DBSession()
            PSWD = self.lineEdit_2.text()
            USNM = self.lineEdit.text()
            DateText = datetime.datetime.now()
            self.session.add(Ui_UserInfo())
            self.session.query(Ui_UserInfo).filter(Ui_UserInfo.Id == 1).update({'UserName': USNM, 'Password':PSWD})
            self.SetUserInfoConfirmationMBox()

    def Mbox(self):
        MB_OK = 0x0
        ICON_STOP = 0x10
        result = ctypes.windll.user32.MessageBoxW(0, "You Must Enter a Username and Password!", "Warning", MB_OK | ICON_STOP)

    def SetUserInfoConfirmationMBox(self):
        try:
            IDYES = 6
            IDNO = 7
            result = ctypes.windll.user32.MessageBoxW(0, "Are you sure you want to Save the User?", "Information",4)
            if result == IDYES:
                self.session.commit()
            else:
                self.session.rollback()
        except:
            pass

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_2.setText(_translate("Dialog", "Password"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
