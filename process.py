# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'process.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import plotter
import errordialog


class Ui_Processes(object):

    # Here we pass data needed when this class is instantiated
    # This is the constructor of the class
    def __init__(self, memory_size, holes_with_size):
        self.memory_size = memory_size
        self.holes_with_size = holes_with_size
        self.drawer = plotter.Drawer_Window(self.memory_size)

        # Declaring Memory Elements
        # Each element in Drawing_List will be (y0, y1, details) where details is dict with name & color
        self.old_processes = {}
        self.Allocated_Processes_Dict = {}
        self.Drawing_List = []
        self.current_process_name = 1

        self.Initialize_Memory()
        self.PrepareDrawing()  # Modifies Drawing List

        # Make function that appends to Drawing_List then Draw it

        # Here we must open the drawing window

    def Chosen_Algorithm(self):
        if self.FirstFitButton.isChecked():
            return self.FirstFitButton.text()
        if self.BestFitButton.isChecked():
            return self.BestFitButton.text()
        if self.WorstFitButton.isChecked():
            return self.WorstFitButton.text()

    def Open_Error_Window(self, message):
        self.window = QtWidgets.QDialog()
        self.ui = errordialog.Ui_Dialog(message)
        self.ui.setupUi(self.window)
        self.window.show()

    def Initialize_Memory(self):
        # This function makes old processes positions and puts them into old_processes dict
        holes_start_end = self.sizeTo_STARTEND(self.holes_with_size)
        holes_start_end.sort(key=lambda x: x[0])  # Sort array from start
        counter = 0
        for i in range(len(holes_start_end)):
            start, end = holes_start_end[i]
            Old_Name = "Old_P" + str(counter)
            if i == 0:
                if start == 0:
                    continue
                else:
                    self.old_processes[Old_Name] = (0, start - 1)
                    counter += 1

            elif i == len(holes_start_end) - 1:
                if end == self.memory_size - 1:
                    continue
                else:
                    self.old_processes[Old_Name] = (
                        end + 1, self.memory_size - 1)

            else:
                self.old_processes[Old_Name] = (
                    end + 1, holes_start_end[i + 1][0] - 1)
                counter += 1
        print("old processes:", self.old_processes)
        return

    def PrepareDrawing(self):
        # This function makes all data ready for drawing
        self.Drawing_List = []
        # details = {}

        # Working with holes

        # details["color"] = self.drawer.HoleColor
        # details["name"] = "Hole"
        holes_start_end = self.sizeTo_STARTEND(self.holes_with_size)
        for start, end in holes_start_end:
            self.Drawing_List.append(
                (start, end, {"name": "Hole", "color": self.drawer.HoleColor}))
        # print("details in holes:", details)

        # Working with Old_Processes
        # {Old_P1: (start,end)}
        # details["color"] = self.drawer.OldProcessColor

        for name, value in self.old_processes.items():
            start, end = value
            # details["name"] = str(name)
            self.Drawing_List.append(
                (start, end, {"name": name, "color": self.drawer.OldProcessColor}))
        # print("details in old:", details)

        # Working with Processes

        # details["color"] = self.drawer.ProcessColor

        for process in self.Allocated_Processes_Dict.keys():

            # {​​​'class': (900, 1499), 'code': (300, 699), 'seg': (0, 199)}​​​
            # name of process
            # detalis={​​​ "p1"}​​​
            for segment_name, segments_tuple in self.Allocated_Processes_Dict[process].items():
                # now add a new hole
                start, end = segments_tuple
                name = str(process + ": " + segment_name)
                self.Drawing_List.append(
                    (start, end, {"name": name, "color": self.drawer.ProcessColor}))
        # print("details in process:", details)
        return

    def add_old_processes(self):
        for name in self.old_processes.keys():
            self.update_menu(name)
        return
        
        

    def Deallocate(self):
        # Deallocate Algorithm and drawing

        # Removing item from menu
        # self.allProcessesMenu.removeItem(deallocated_item_index)
        return

    def Allocate(self):
        # Retrieve Data From TextBox
        process_entry = self.SegmentTextBox.toPlainText().split('\n')
        process_name = "P" + str(self.current_process_name)
        process_data = {}
        print(process_entry)
        for segment in process_entry:
            name, size = segment.split(':')
            process_data[name] = int(size)
            print(name, size)

        algorithm = self.Chosen_Algorithm()

        if algorithm == "First Fit":
            if (self.first_fit(process_name, process_data)):

                self.current_process_name += 1
                self.update_menu(process_name)
                self.updateTitle("P" + str(self.current_process_name))
                self.PrepareDrawing()  # Modifies Drawing List
                self.drawer.delete_window()
                self.drawer.draw(self.Drawing_List)

            else:
                self.Open_Error_Window("There's No Free Space")

        elif algorithm == "Best Fit":
            if (self.best_fit(process_name, process_data)):
                self.PrepareDrawing()  # Modifies Drawing List
                self.drawer.draw(self.Drawing_List)
            else:
                self.Open_Error_Window("There's No Free Space")

        elif algorithm == "Worst Fit":
            if (self.worst_fit(process_name, process_data)):
                self.PrepareDrawing()  # Modifies Drawing List
                self.drawer.draw(self.Drawing_List)
            else:
                self.Open_Error_Window("There's No Free Space")

        """
        Code:400
        Mem:200
        
        """
        # allocate Algorithm and drawing

        # Retrieve everything to draw
        # Modifying tuples to add color to them

        # self.graph.delete_window()
        # Draw Here

        # Adding item from menu
        # self.allProcessesMenu.setItemText(i+1, _translate("MainWindow", processes_array[i].name))

        return

    # DANGER!!! Process Allocation Functions
    # Credits to Hazem Ashraf
    ############################################
    def sizeTo_STARTEND(self, Base_Size_List):
        # make the array of start and end
        result = []

        for base, size in Base_Size_List:
            end = base+size-1
            result.append((base, end))
        return result

    def startTo_SIZE(self, Start_End_List):
        # Convert List into (base,size)
        result = []

        for start, end in Start_End_List:
            size = end - start + 1
            result.append((start, size))
        return result

    def first_fit(self, process_name, process_data):

        # this for check
        safe_holes_sizes = self.holes_with_size[:]

        one_process_dict = {}
        temp_dict = {}

        # normal memory sort
        self.holes_with_size.sort(key=lambda x: x[0])

        print("holes sort smallest base  : ", self.holes_with_size)
        print("the procces : ", process_data)

        for segments_name, segments_size in process_data.items():
            # compare segments_size with holes
            for hole_index in range(len(self.holes_with_size)):
                # get size of hole
                # (100,299)
                start = self.holes_with_size[hole_index][0]
                size_of_el_hole_ele_3leha_eldor = self.holes_with_size[hole_index][1]
                end = start + size_of_el_hole_ele_3leha_eldor-1

                if segments_size <= size_of_el_hole_ele_3leha_eldor:

                    taken_space_by_segment_tuple = (
                        start, start + segments_size - 1)
                    # sotre in list that contains the process allocated in memory
                    # needed in the allocation
                    " ya norm "
                    # code  : ( 0 , 299)
                    temp_dict.update(
                        {f'{segments_name}': taken_space_by_segment_tuple})
                    modified_hole = (
                        taken_space_by_segment_tuple[1]+1, size_of_el_hole_ele_3leha_eldor-segments_size)
                    # the update pb
                    self.holes_with_size[hole_index] = modified_hole
                    break
                # finished for loop for allocate a segment in temp_allocate[]
            print("updated array in loop : ", self.holes_with_size)

        if len(process_data.keys()) > len(temp_dict.keys()):

            # holes_with_size=safe_holes_sizes
            for i in range(len(safe_holes_sizes)):
                self.holes_with_size[i] = safe_holes_sizes[i]
            print("not safe ya negm")
            return False

        # finished for loop for allocate a process
        # store the procces and its locations
        # {'p1' : 'code':(500,900} , 'seg' : (1000,1010}
        one_process_dict = {process_name: temp_dict}
        print("process with tuples : ", one_process_dict)
        # { 'p1' : {'code':(500,900) , seg' : (1000,1010)} ,'p2' : {'code':(500,900) , 'seg' : (1000,1010)} }

        self.Allocated_Processes_Dict.update(one_process_dict)
        print("the dict : ", self.Allocated_Processes_Dict)
        return True

    def best_fit(self, process_name, process_data):
        # this for check
        safe_holes_sizes = self.holes_with_size[:]

        one_process_dict = {}
        temp_dict = {}
        # holes sorted from small to big size
        self.holes_with_size.sort(key=lambda x: x[1])
        print("holes sort : ", self.holes_with_size)
        # should sort the segments big to small
        sorte = sorted(process_data.items(), key=lambda x: x[1], reverse=True)
        sorted_process = dict(sorte)
        print("the procces sort : ", sorted_process)

        for segments_name, segments_size in sorted_process.items():
            # compare segments_size with holes
            for hole_index in range(len(self.holes_with_size)):
                # get size of hole
                start = self.holes_with_size[hole_index][0]
                size = self.holes_with_size[hole_index][1]
                end = start + size - 1

                if segments_size <= size:
                    taken_space_by_segment_tuple = (
                        start, start + segments_size - 1)
                    # sotre in list that contains the process allocated in memory
                    # needed in de allocation
                    temp_dict.update(
                        {f'{segments_name}': taken_space_by_segment_tuple})
                    modified_hole = (
                        taken_space_by_segment_tuple[1]+1, size-segments_size)
                    # the update pb
                    self.holes_with_size[hole_index] = modified_hole
                    break
            # finished for loop for allocate a segment in temp_allocate[]

        if len(process_data.keys()) > len(temp_dict.keys()):
            # holes_with_size=safe_holes_sizes
            for i in range(len(safe_holes_sizes)):
                self.holes_with_size[i] = safe_holes_sizes[i]
            print("not safe ya negm")
            return False

        # finished for loop for allocate a process
        # store the procces and its locations
        # {'p1' : 'code':(500,900} , 'seg' : (1000,1010}
        one_process_dict = {process_name: temp_dict}
        print("process with tuples : ", one_process_dict)
        # { 'p1' : {'code':(500,900) , seg' : (1000,1010)} ,'p2' : {'code':(500,900) , 'seg' : (1000,1010)} }
        self.Allocated_Processes_Dict.update(one_process_dict)
        print("the dict : ", self.Allocated_Processes_Dict)
        return True

    def worst_fit(self, process_name, process_data):
        # this for check
        safe_holes_sizes = self.holes_with_size[:]

        one_process_dict = {}
        temp_dict = {}
        self.holes_with_size.sort(key=lambda x: x[1], reverse=True)
        print("holes sort with size : ", self.holes_with_size)
        # should sort the segments small to big
        sorte = sorted(process_data.items(), key=lambda x: x[1])
        sorted_process = dict(sorte)

        print("the procces sort : ", sorted_process)
        print("################################")
        for segments_name, segments_size in sorted_process.items():
            # compare segments_size with holes
            for hole_index in range(len(self.holes_with_size)):
                # pb here
                # we take the same tuple every time
                # must update th sizes
                # get size of hole
                start = self.holes_with_size[hole_index][0]
                size = self.holes_with_size[hole_index][1]
                end = start + size - 1

                if segments_size <= size:
                    taken_space_by_segment_tuple = (
                        start, start + segments_size - 1)
                    # sotre in list that contains the process allocated in memory
                    # needed in de allocation
                    temp_dict.update(
                        {f'{segments_name}': taken_space_by_segment_tuple})
                    modified_hole = (
                        taken_space_by_segment_tuple[1]+1, size-segments_size)
                    # the update pb
                    self.holes_with_size[hole_index] = modified_hole
                    break

            # finished for loop for allocate a segment in temp_allocate[]

        # the check
        # no of segments in old procces vs new
        if len(process_data.keys()) > len(temp_dict.keys()):

            # holes_with_size=safe_holes_sizes
            for i in range(len(safe_holes_sizes)):
                self.holes_with_size[i] = safe_holes_sizes[i]
            print("not safe ya negm")
            return False

        # finished for loop for allocate a process
        # store the procces and its locations
        # {'p1' : 'code':(500,900} , 'seg' : (1000,1010}
        one_process_dict = {process_name: temp_dict}
        print("process with tuples : ", one_process_dict)
        # { 'p1' : {'code':(500,900) , seg' : (1000,1010)} ,'p2' : {'code':(500,900) , 'seg' : (1000,1010)} }
        self.Allocated_Processes_Dict.update(one_process_dict)
        print("the dict : ", self.Allocated_Processes_Dict)
        return True

    def deallocate(self, procces_to_delete, array_holes, Allocated_Processes_Dict):

        awhole_new_holes_list = []
        # get Name
        # search on old Memory
        # if procces_to_delete in self.Allocated_Processes_Dict:
        #{'code':(500,900) , 'seg' : (1000,1010)}
        contents = self.Allocated_Processes_Dict[procces_to_delete]
        for segments_name, segments_tuple in contents.items():
            # now add a new hole
            array_holes.append(segments_tuple)
        print(array_holes)
        # add the holees ended
        # delete that process from dict
        del self.Allocated_Processes_Dict[procces_to_delete]
        # merge memory
        # sort holes
        array_holes.sort(key=lambda x: x[0])
        print(array_holes)
        awhole_new_holes_list = array_holes[:]
        awhole_new_holes_list.clear()
        #
        x = 0
        for hole_index in range(len(array_holes)):
            # print(hole_index)
            if (hole_index == len(array_holes)-1):
                # print("if")
                # break
                continue
            else:
                if x:
                    x -= 1
                    continue
                print(array_holes[hole_index][1], array_holes[hole_index+1][0])
                if (array_holes[hole_index][1] - array_holes[hole_index+1][0]) == -1:
                    # new hole = (strat1 , end 2)
                    awhole_new_hole = (
                        array_holes[hole_index][0], array_holes[hole_index+1][1])
                    awhole_new_holes_list.append(awhole_new_hole)
                    print("whole in if ", awhole_new_holes_list)
                    x += 1
                else:
                    # normal hole
                    awhole_new_holes_list.append(array_holes[hole_index])
                    print("whole in else ", awhole_new_holes_list)
            # [(0,1500),(1501,2000),(2500,3000)]
        array_holes = awhole_new_holes_list[:]
        awhole_new_holes_list.clear()
        print("dict ", self.Allocated_Processes_Dict)
        print("array ", array_holes)
        return array_holes
    ############################################

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
        self.AllocateButton = QtWidgets.QPushButton(
            Processes, clicked=lambda: self.Allocate())
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
        self.add_old_processes()
        QtCore.QMetaObject.connectSlotsByName(Processes)

    def retranslateUi(self, Processes):
        _translate = QtCore.QCoreApplication.translate
        # for i in range(len(processes_array)):
        #     self.allProcessesMenu.setItemText(i+1, _translate("MainWindow", processes_array[i].name))
        # self.allProcessesMenu.findText()

        Processes.setWindowTitle(_translate("Processes", "Form"))
        self.label.setText(_translate(
            "Processes", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Allocation Algorithm </span></p></body></html>"))
        self.WorstFitButton.setText(_translate("Processes", "Worst Fit"))
        self.FirstFitButton.setText(_translate("Processes", "First Fit"))
        self.BestFitButton.setText(_translate("Processes", "Best Fit"))
        self.label_2.setText(_translate("Processes", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Type process segment this way: </span><span style=\" font-size:10pt; font-weight:600; color:#5d0000;\">Name:Size</span></p><p><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">Note: Separate segments by enter</span></p></body></html>"))
        self.AllocateButton.setText(_translate("Processes", "Allocate"))
        self.DeallocateButton.setText(_translate("Processes", "Deallocate"))
        self.ProcessLabel.setText(_translate(
            "Processes", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Process Name: P"+str(self.current_process_name)+" </span></p></body></html>"))

    def update_menu(self, name):
        # This function updates menu and process name in the window
        _translate = QtCore.QCoreApplication.translate
        self.allProcessesMenu.addItem(name, name)
        self.allProcessesMenu.setItemText(
            int(name.find("P")+1), _translate("MainWindow", name))

    def updateTitle(self, new_name):
        # This function updates menu and process name in the window
        _translate = QtCore.QCoreApplication.translate
        self.ProcessLabel.setText(_translate(
            "Processes", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Process Name: "+new_name+" </span></p></body></html>"))


if __name__ == "__main__":
    import sys
    holes = [(600, 500), (1200, 900), (2600, 1000)]
    app = QtWidgets.QApplication(sys.argv)
    Processes = QtWidgets.QWidget()
    ui = Ui_Processes(5800, holes)
    ui.setupUi(Processes)
    Processes.show()
    # Plotting the window
    ui.drawer.draw(ui.Drawing_List)
    sys.exit(app.exec_())
