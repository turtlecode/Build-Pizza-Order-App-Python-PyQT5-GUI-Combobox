import PyQt5.QtWidgets as PyWidget
import PyQt5.QtGui as PyGui


class MainWindow(PyWidget.QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(PyWidget.QVBoxLayout())

        my_label = PyWidget.QLabel("Pick Something From The List Below", self)

        my_label.setFont(PyGui.QFont('Helvetica', 24))
        self.layout().addWidget(my_label)

        my_combo = PyWidget.QComboBox(self,
                                 editable=True,
                                 insertPolicy=PyWidget.QComboBox.InsertAtBottom)

        my_combo.addItem("Neapolitan Pizza")
        my_combo.addItem("Chicago Pizza")
        my_combo.insertItems(2,["California Pizza","Detroit Pizza"])

        self.layout().addWidget(my_combo)

        my_button = PyWidget.QPushButton("Press Me!",
                                    clicked=lambda: press_it())
        self.layout().addWidget(my_button)
        self.show()

        def press_it():
            my_label.setText(f'You Picked {my_combo.currentText()}!')


app = PyWidget.QApplication([])
mw = MainWindow()
app.exec_()