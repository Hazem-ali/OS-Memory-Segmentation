# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'holes_data.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import process
import errordialog


class Ui_HolesForm(object):

    # here we pass data needed when this class is instantiated
    # This is the constructor of the class
    def __init__(self, memory_size, no_of_holes):
        self.memory_size = memory_size
        self.no_of_holes = no_of_holes

    def Open_Error_Window(self, message):
        self.window = QtWidgets.QDialog()
        self.ui = errordialog.Ui_Dialog(message)
        self.ui.setupUi(self.window)
        self.window.show()

    def openProcessWindow(self):

        # Organizing variables
        all_holes_tuples = []
        for hole in self.AllTextBoxes:
            try:
                base = int(hole["Base"].text())
                size = int(hole["Size"].text())
                all_holes_tuples.append((base, size))
                if(base < 0 or size < 0):
                    self.Open_Error_Window("Please Write Positive Numbers")
                    return
            except:
                # Invalid Numbers Situation
                self.Open_Error_Window("Please Write Valid Numbers")
                return

        hole_test = sorted(all_holes_tuples, key=lambda x: x[0], reverse=True)
        for item in hole_test:
            test_base, test_size = item
            if test_base + test_size >= self.memory_size:
                self.Open_Error_Window("Hole Cannot Exceed Memory Size")
                return

        # if integer parsing has no errors
        self.window = QtWidgets.QWidget()
        self.ProcessUI = process.Ui_Processes(
            self.memory_size, all_holes_tuples)
        self.ProcessUI.setupUi(self.window)
        # Plotting the window
        self.window.show()
        self.ProcessUI.drawer.draw(self.ProcessUI.Drawing_List)

    def setupUi(self, HolesForm):
        HolesForm.setObjectName("HolesForm")
        HolesForm.resize(558, 452)
        self.StartButton = QtWidgets.QPushButton(
            HolesForm, clicked=lambda: self.openProcessWindow())
        self.StartButton.setGeometry(QtCore.QRect(170, 390, 221, 41))
        self.StartButton.setObjectName("StartButton")
        self.scrollArea = QtWidgets.QScrollArea(HolesForm)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setGeometry(QtCore.QRect(0, 10, 741, 381))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 739, 379))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LabelGroup = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.LabelGroup.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.LabelGroup.sizePolicy().hasHeightForWidth())
        self.LabelGroup.setSizePolicy(sizePolicy)
        self.LabelGroup.setMinimumSize(QtCore.QSize(0, 50))
        self.LabelGroup.setTitle("")
        self.LabelGroup.setObjectName("LabelGroup")
        self.HoleLabel = QtWidgets.QLabel(self.LabelGroup)
        self.HoleLabel.setGeometry(QtCore.QRect(10, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HoleLabel.setFont(font)
        self.HoleLabel.setObjectName("HoleLabel")
        self.HoleSizeLabel = QtWidgets.QLabel(self.LabelGroup)
        self.HoleSizeLabel.setGeometry(QtCore.QRect(200, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HoleSizeLabel.setFont(font)
        self.HoleSizeLabel.setObjectName("HoleSizeLabel")
        self.BaseAddressLabel = QtWidgets.QLabel(self.LabelGroup)
        self.BaseAddressLabel.setGeometry(QtCore.QRect(70, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BaseAddressLabel.setFont(font)
        self.BaseAddressLabel.setObjectName("BaseAddressLabel")
        self.verticalLayout.addWidget(self.LabelGroup)

        self.AllTextBoxes = []  # each element here is a list that contain all entries for a hole
        for i in range(self.no_of_holes):  # Here we add number of holes
            HoleTextBoxes = {}

            self.HoleGroup = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
            sizePolicy = QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(
                self.HoleGroup.sizePolicy().hasHeightForWidth())

            self.HoleGroup.setSizePolicy(sizePolicy)
            self.HoleGroup.setMinimumSize(QtCore.QSize(0, 50))
            self.HoleGroup.setTitle("")
            self.HoleGroup.setObjectName("HoleGroup")

            self.H1 = QtWidgets.QLabel(self.HoleGroup)
            self.H1.setGeometry(QtCore.QRect(-10, 0, 61, 31))
            self.H1.setFrameShadow(QtWidgets.QFrame.Raised)
            self.H1.setAlignment(QtCore.Qt.AlignCenter)
            self.H1.setObjectName("H"+str(i+1))

            self.BaseAddressInput = QtWidgets.QLineEdit(self.HoleGroup)
            self.BaseAddressInput.setGeometry(QtCore.QRect(70, 10, 113, 20))
            self.BaseAddressInput.setObjectName("BaseAddressInput")

            self.HoleSizeInput = QtWidgets.QLineEdit(self.HoleGroup)
            self.HoleSizeInput.setGeometry(QtCore.QRect(200, 10, 113, 20))
            self.HoleSizeInput.setObjectName("HoleSizeInput")

            self.verticalLayout.addWidget(self.HoleGroup)
            self.scrollArea.setWidget(self.scrollAreaWidgetContents)

            self.retranslateUi(HolesForm, "H"+str(i+1))
            QtCore.QMetaObject.connectSlotsByName(HolesForm)

            # Adding Spins into the Dict for each hole
            HoleTextBoxes["Base"] = self.BaseAddressInput
            HoleTextBoxes["Size"] = self.HoleSizeInput
            # Adding This Dict to the big list that contains all spins
            self.AllTextBoxes.append(HoleTextBoxes)
            ##############################################

    def retranslateUi(self, HolesForm, HoleName):
        _translate = QtCore.QCoreApplication.translate
        HolesForm.setWindowTitle(_translate("HolesForm", "Form"))
        self.StartButton.setText(_translate("HolesForm", "Start "))
        self.HoleLabel.setText(_translate("HolesForm", "Hole"))
        self.HoleSizeLabel.setText(_translate("HolesForm", "Size"))
        self.BaseAddressLabel.setText(_translate("HolesForm", "Base Address"))
        self.H1.setText(_translate("HolesForm", HoleName))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     HolesForm = QtWidgets.QWidget()
#     ui = Ui_HolesForm(5000,2)
#     ui.setupUi(HolesForm)
#     HolesForm.show()
#     sys.exit(app.exec_())
