from GUI.IB_PyQt_GUI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Main_Window(QMainWindow):
	def __init__(self):
		super(Main_Window,self).__init__()
		Ui = Ui_MainWindow()
		Ui.setupUi(self)
		self.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Main_Window()
	sys.exit(app.exec_())