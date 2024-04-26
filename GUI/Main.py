from WorkWidgets.MainWidget import MainWidget
from PyQt6.QtWidgets import QApplication
import sys

app = QApplication([])
main_window = MainWidget()

main_window.setFixedSize(650, 350)
main_window.show()
# main_window.showFullScreen()

sys.exit(app.exec())
