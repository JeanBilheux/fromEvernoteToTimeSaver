from PyQt4 import QtGui

class FromEvernoteToTimeSaver(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setWindowTitle("From Evernote to Time Saver")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = FromEvernoteToTimeSaver()
    myapp.show()
    
    exit_code = app.exec_()
    sys.exit(exit_code)