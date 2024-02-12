import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self,titulo):
        super().__init__()
        self.setWindowTitle(titulo)

app = QApplication(sys.argv)

window = MainWindow("App")
window.show()

app.exec()
