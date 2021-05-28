# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'process.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Processes(object):
    
    # Here we pass data needed when this class is instantiated
    # This is the constructor of the class
    def __init__(self, memory_size, all_holes_tuples):
        self.memory_size = memory_size
        self.all_holes_tuples = all_holes_tuples
        
        # Here we must open the drawing window
        
    def Chosen_Algorithm(self):
        if self.FirstFitButton.isChecked():
            return self.FirstFitButton.text()
        if self.BestFitButton.isChecked():
            return self.BestFitButton.text()
        if self.WorstFitButton.isChecked():
            return self.WorstFitButton.text()
        
    def setupUi(self, Processes):
        Processes.setObjectName("Processes")
        Processes.resize(513, 473)
        self.label = QtWidgets.QLabel(Processes)
        self.label.setGeometry(QtCore.QRect(40, 50, 201, 21))
        self.label.setObjectName("label")
        self.radioGroup = QtWidgets.QGroupBox(Processes)
        self.radioGroup.setGeometry(QtCore.QRect(40, 70, 231, 51))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioGroup.setFont(font)
        self.radioGroup.setTitle("")
        self.radioGroup.setObjectName("radioGroup")
        self.WorstFitButton = QtWidgets.QRadioButton(self.radioGroup)
        self.WorstFitButton.setGeometry(QtCore.QRect(150, 20, 82, 17))
        self.WorstFitButton.setObjectName("WorstFitButton")
        self.FirstFitButton = QtWidgets.QRadioButton(self.radioGroup)
        self.FirstFitButton.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.FirstFitButton.setChecked(True)
        self.FirstFitButton.setObjectName("FirstFitButton")
        self.BestFitButton = QtWidgets.QRadioButton(self.radioGroup)
        self.BestFitButton.setGeometry(QtCore.QRect(80, 20, 82, 17))
        self.BestFitButton.setChecked(False)
        self.BestFitButton.setObjectName("BestFitButton")
        self.SegmentTextBox = QtWidgets.QPlainTextEdit(Processes)
        self.SegmentTextBox.setGeometry(QtCore.QRect(40, 200, 281, 161))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.SegmentTextBox.setFont(font)
        self.SegmentTextBox.setStatusTip("")
        self.SegmentTextBox.setPlainText("")
        self.SegmentTextBox.setObjectName("SegmentTextBox")
        self.label_2 = QtWidgets.QLabel(Processes)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 301, 51))
        self.label_2.setObjectName("label_2")
        self.AllocateButton = QtWidgets.QPushButton(Processes)
        self.AllocateButton.setGeometry(QtCore.QRect(40, 410, 91, 31))
        self.AllocateButton.setObjectName("AllocateButton")
        self.DeallocateButton = QtWidgets.QPushButton(Processes)
        self.DeallocateButton.setGeometry(QtCore.QRect(390, 410, 91, 31))
        self.DeallocateButton.setObjectName("DeallocateButton")
        self.allProcessesMenu = QtWidgets.QComboBox(Processes)
        self.allProcessesMenu.setGeometry(QtCore.QRect(390, 380, 91, 22))
        self.allProcessesMenu.setObjectName("allProcessesMenu")
        self.ProcessLabel = QtWidgets.QLabel(Processes)
        self.ProcessLabel.setGeometry(QtCore.QRect(190, 20, 211, 21))
        self.ProcessLabel.setObjectName("ProcessLabel")

        self.retranslateUi(Processes)
        QtCore.QMetaObject.connectSlotsByName(Processes)

    def retranslateUi(self, Processes):
        _translate = QtCore.QCoreApplication.translate
        Processes.setWindowTitle(_translate("Processes", "Form"))
        self.label.setText(_translate("Processes", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Allocation Algorithm </span></p></body></html>"))
        self.WorstFitButton.setText(_translate("Processes", "Worst Fit"))
        self.FirstFitButton.setText(_translate("Processes", "First Fit"))
        self.BestFitButton.setText(_translate("Processes", "Best Fit"))
        self.label_2.setText(_translate("Processes", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Type process segment this way: </span><span style=\" font-size:10pt; font-weight:600; color:#5d0000;\">Name:Size</span></p><p><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">Note: Separate segments by enter</span></p></body></html>"))
        self.AllocateButton.setText(_translate("Processes", "Allocate"))
        self.DeallocateButton.setText(_translate("Processes", "Deallocate"))
        self.ProcessLabel.setText(_translate("Processes", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Process Name: P1 </span></p></body></html>"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Processes = QtWidgets.QWidget()
#     ui = Ui_Processes()
#     ui.setupUi(Processes)
#     Processes.show()
#     sys.exit(app.exec_())