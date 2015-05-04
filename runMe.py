from PyQt4 import QtGui
import sys
import re
from main_window import *


class FromEvernoteToTimeSaver(QtGui.QMainWindow):

    list_day_ui = []


    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("From Evernote to Time Saver")
        self.ui.pushButton.setFocus()

        self.list_day_ui = [self.ui.label_monday,
                            self.ui.label_tuesday,
                            self.ui.label_wednesday,
                            self.ui.label_thursday,
                            self.ui.label_friday,
                            self.ui.label_saturday,
                            self.ui.label_sunday]
        
    def convert(self):
        text_to_convert = self.ui.textEdit.toPlainText()
        o_working_hours = ProduceWorkingHours(text_to_convert)
        nbr_days_worked = o_working_hours.nbrDaysWorked()
        list_hours_worked = o_working_hours.listHoursWorked()
        revert_list_hours_worked = self.revertList(list_hours_worked)
        
        self.populateLabels(revert_list_hours_worked)

    def populateLabels(self, list_hours_worked):
        for idx, hours_worked in enumerate(list_hours_worked):
            label_ui = self.list_day_ui[idx].setText("%.1f"%(float(hours_worked)))

    def revertList(self, list_hours_worked):
        return list_hours_worked[::-1]
        
class ProduceWorkingHours(object):
    
    input_string = ''
    nbr_days_worked = -1
    list_day_worked = []
    list_hours_worked = []
    
    def __init__(self, string_hours):
        self.input_string = ''
        self.nbr_days_worked = -1
        self.list_day_worked = []
        self.list_hours_worked = []

        self.input_string = string_hours
                
        self.splitByDay()
        
    def splitByDay(self):
        
        # if no argument passed
        _input_string = str(self.input_string)
        if _input_string.strip() == "":
            return
        
        _list_day_worked = _input_string.split("\n")

        # get real number of days worked (remove empty lines)
        index_nbr_day = 0
        for day in _list_day_worked:
            if day.strip() != "":
                index_nbr_day += 1
                self.list_day_worked.append(day)
        self.nbr_days_worked = index_nbr_day
        
        self.getListHoursWorked()
        
    def getListHoursWorked(self):
        _list_day_worked = self.list_day_worked
        for _day in _list_day_worked:
            set_date_from_second_part = _day.split(":")
            
            if len(set_date_from_second_part) == 1:
                self.nbr_days_worked -= 1
                continue
            
            if len(set_date_from_second_part) == 2:
                hours_worked = self.calculateNumberOfHoursStraigthHours(set_date_from_second_part[1])
                self.list_hours_worked.append(hours_worked)
                continue
            
            second_part = ":".join(set_date_from_second_part[1:])
            [start_day, end_day, minus_hours, plus_hours] = self.isolateStringParts(second_part)
            hours_worked = self.calculateNumberOfHoursWorked([start_day, end_day, minus_hours, plus_hours])
            self.list_hours_worked.append(hours_worked)
    
    def isolateStringParts(self, second_part):
        second_part = second_part.replace(" ", "")
        regular_expression = r"(\d+):(\d+)->(\d+):(\d+)(-\d?.?\d+)?h?(\+\d?.?\d?)?h?"
        result_re = re.match(regular_expression, second_part)
        
        start_hour = int(result_re.group(1))
        start_minute = float(result_re.group(2))/60.
        start_hour_mn = float(start_hour) + start_minute

        end_hour = int(result_re.group(3))
        end_minute = float(result_re.group(4))/60.
        end_hour_mn = float(end_hour) + end_minute
        
        minus_hour_str = result_re.group(5)
        minus_hour = 0
        if minus_hour_str:
            split_by_neg_sign = minus_hour_str.split("-")
            split_by_h = split_by_neg_sign[1].split("h")
            minus_hour = float(split_by_h[0])
        
        plus_hour_str = result_re.group(6)
        plus_hour = 0
        if plus_hour_str: 
            split_by_plus_sign= plus_hour_str.split("+")
            split_by_h = split_by_plus_sign[1].split("h")
            plus_hour = float(split_by_h[0])

        return [start_hour_mn, end_hour_mn, minus_hour, plus_hour]

    def calculateNumberOfHoursStraigthHours(self, second_part):
        remove_h = second_part.split("h")
        return remove_h[0].strip()
    
    def calculateNumberOfHoursWorked(self, start_end_minus_plus_list):
        start_hour_mn = start_end_minus_plus_list[0]
        end_hour_mn = 12+start_end_minus_plus_list[1]
        minus_hour = start_end_minus_plus_list[2]
        plus_hour = start_end_minus_plus_list[3]

        total_hours = end_hour_mn - start_hour_mn - minus_hour + plus_hour
        return str(total_hours)
    
    def nbrDaysWorked(self):
        return self.nbr_days_worked
        
    def listHoursWorked(self):
        return self.list_hours_worked


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = FromEvernoteToTimeSaver()
    myapp.show()
    
    exit_code = app.exec_()
    sys.exit(exit_code)