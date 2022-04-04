import sys

from PIL.ImageDraw import ImageDraw
from PIL.ImageQt import ImageQt, QPixmap
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QGraphicsColorizeEffect, \
    QColorDialog, QLabel, QDialog, QWidget, QVBoxLayout, QHBoxLayout
from ui_palette import Ui_MainWindow
from ui_add_tab_dialog import Ui_AddTabDialog
from ui_palette_tab import Ui_PaletteTab
from PIL import Image


def pixmap_grid_to_label(cols, rows, label: QLabel):
    size = label.size()
    image_x, image_y = size.width(), size.height()
    image = Image.new('RGB', (image_x, image_y), color="white")
    draw = ImageDraw(image)
    y_start = 0
    y_end = image.height
    y_step_size = int(image.width / rows)
    for x in range(0, image.width, y_step_size):
        line = ((x, y_start), (x, y_end))
        draw.line(line, fill=128)
    line = ((image.width - 1, y_start), (image.width - 1, y_end))
    draw.line(line, fill=128)
    x_start = 0
    x_end = image.width
    x_step_size = int(image.height / cols)
    for y in range(0, image.height, x_step_size):
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill=128)
    line = ((x_start, image.height - 1), (x_end, image.height - 1))
    draw.line(line, fill=128)

    image2 = image.convert("RGBA")
    data = image2.tobytes("raw", "BGRA")
    qim = QtGui.QImage(data, image.width, image.height, QtGui.QImage.Format_ARGB32)
    pix = QtGui.QPixmap.fromImage(qim)
    label.setPixmap(pix)


class PaletteTab(QWidget, Ui_PaletteTab):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print(self.layout().sizeHint())
        self.resize_picture()
        self.lineEdit_height.textChanged.connect(self.resize_picture)
        self.lineEdit_width.textChanged.connect(self.resize_picture)
        self.pushButton.clicked.connect(self.add_color_action)

    def func(self, a0):
        print(a0)

    def resize_picture(self):
        try:
            width = int(self.lineEdit_width.text())
            height = int(self.lineEdit_height.text())
            if width == 0 or height == 0:
                raise ValueError
        except ValueError:
            return
        self.label_picture.resize(width, height)

    def add_color_action(self):
        color = QColorDialog.getColor()
        label = self.label_picture
        label.setGeometry(100, 100, 200, 60)
        label.setText(str(color))
        graphic = QGraphicsColorizeEffect(self)
        graphic.setColor(color)
        label.setGraphicsEffect(graphic)


class PaletteEditor(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.push_button_add_color.clicked.connect(self.add_color_action)
        self.action_add_palette.triggered.connect(self.open_add_tab_dialog)

    def open_add_tab_dialog(self):
        add_tab_dialog = AddTabDialog(self)
        add_tab_dialog.exec()

    def add_tab(self, cols: int, rows: int):
        palette_tab = PaletteTab()
        pixmap_grid_to_label(cols, rows, palette_tab.label_picture)
        self.tabWidget.addTab(palette_tab, "new_tab")


class AddTabDialog(QDialog, Ui_AddTabDialog):
    def __init__(self, palette_editor):
        super().__init__()
        self.setupUi(self)
        self.palette_editor = palette_editor
        self.cols = self.rows = None
        self.label_presize.resize(250, 250)
        self.draw_grid()
        self.lineEditCountColumns.textChanged.connect(self.draw_grid)
        self.lineEditCountRows.textChanged.connect(self.draw_grid)
        self.pushButton_ok.clicked.connect(self.ok_action)
        self.pushButton_cancel.clicked.connect(self.cancel_action)

    def draw_grid(self):
        try:
            cols = int(self.lineEditCountColumns.text())
            rows = int(self.lineEditCountRows.text())
            if cols == 0 or rows == 0:
                raise ValueError
        except ValueError:
            return

        self.cols = cols
        self.rows = rows

        pixmap_grid_to_label(cols, rows, self.label_presize)

    def ok_action(self):
        self.palette_editor.add_tab(self.rows, self.cols)
        self.close()

    def cancel_action(self):
        self.close()


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PaletteEditor()
    ex.show()
    sys.exit(app.exec())