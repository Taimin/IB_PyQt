from GUI.Main_Window import Main_Window
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Main_Window()
	sys.exit(app.exec_())