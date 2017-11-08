from IB_PyQt_GUI import Ui_MainWindow
import About_IB_PyQt, Connect_To_IB, About_Qt
from PyQt5.QtWidgets import QMainWindow, QDialog

class Connect_To_IB_Window(QDialog,Connect_To_IB.Ui_Form):
	def __init__(self):
		super(Connect_To_IB_Window,self).__init__()
		self.setupUi(self)
		self.show()

class About_IB_PyQt_Window(QDialog,About_IB_PyQt.Ui_Dialog):
	def __init__(self):
		super(About_IB_PyQt_Window, self).__init__()
		self.setupUi(self)
		self.show()

class About_Qt_Window(QDialog,About_Qt.Ui_Form):
	def __init__(self):
		super(About_Qt_Window, self).__init__()
		self.setupUi(self)
		self.show()

class Main_Window(QMainWindow,Ui_MainWindow):
	def __init__(self):
		super(Main_Window,self).__init__()
		self.setupUi(self)
		self.home()
		self.show()
		
	def Open_Connect_To_IB_Window(self):
		self.Connect_To_IB_Window = Connect_To_IB_Window()

	def Open_About_IB_PyQt_Window(self):
		self.About_IB_PyQt_Window = About_IB_PyQt_Window()

	def Open_About_Qt_Window(self):
		self.About_IB_PyQt_Window = About_Qt_Window()
		
	def home(self):
		self.actionConnect.triggered.connect(self.Open_Connect_To_IB_Window)
		self.actionAbout.triggered.connect(self.Open_About_IB_PyQt_Window)
		self.actionAbout_QT.triggered.connect(self.Open_About_Qt_Window)