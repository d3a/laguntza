import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self,titulo):
        super().__init__()
        self.setWindowTitle(titulo)

        layout_h = QHBoxLayout()
        layout_h.addWidget(QWidget())
        layout_h.addWidget(QWidget())

        layout_t = QHBoxLayout()
        layout_h.addWidget(QWidget())
        layout_h.addWidget(QWidget())

        layout_g = QGridLayout()
        layout_g.addWidget(QWidget(), 0, 0)
        layout_g.addWidget(QWidget(), 1, 0)
        layout_g.addWidget(QWidget(), 1, 1)
        layout_g.addWidget(QWidget(), 2, 1)
        
        layout_v = QVBoxLayout()
        layout_v.addWidget(QWidget())
        layout_v.addLayout(layout_h)
        layout_v.addLayout(layout_g)

app = QApplication(sys.argv)

window = MainWindow("App")
window.show()

app.exec()
