from PyQt4 import QtGui
import sys
from main_window import *

class FromEvernoteToTimeSaver(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("From Evernote to Time Saver")
        self.ui.pushButton.setFocus()
        
    def convert(self):
        text_to_convert = self.ui.textEdit.toPlainText()
        o_working_hours = ProduceWorkingHours(text_to_convert)
        nbr_days_worked = o_working_hours.nbrDaysWorked()
        list_days_worked = o_working_hours.listHoursWorked()
        
        #result = text_to_convert.split("\n")
        #week_working_hours = []
        #for row in result:
            #nbr_hours = self.retrieveNbrHoursWorkThatDay(row)
            #week_working_hours.append(nbr_hours)
        #print week_working_hours
        
        #nbr_days_worked = len(week_working_hours)
        #for day_index in range(nbr_days_worked, 0, -1):
            #pass
            
    #def retrieveNbrHoursWorkedThatDay(self, row):
        #sep_date_hours = row.split(":")
        #if len(sep_date_hours) == 1:
            #return -1
        
        #hours_part = sep_date_hours[1:].join(":")
        #full_day = hours_part.split("->")
        #if len(full_day) == 1: #ex: 8h
            #hours = full_day[0].split("h") # remove hours ('h') symbol
            #return str(hours[0]).strip()
        
        #start_day_at = full_day[0]
        #second_part_of_day = full_day[1].split("-")
        
        #return -1


class ProduceWorkingHours(object):
    
    input_string = ''
    nbr_days_worked = -1
    list_day_worked = []
    
    def __init__(self, string_hours):
        self.input_string = string_hours
                
        self.splitByDay()
        
    def splitByDay(self):
        
        # if no argument passed
        _input_string = self.input_string
        if _input_string.strip() == "":
            return
        
        list_day_worked = _input_string.split("\n")

        # get real number of days worked (remove empty lines)
        index_nbr_day = 0
        for day in list_day_worked:
            if day.strip() != "":
                index_nbr_day += 1
        self.nbr_days_worked = index_nbr_day
        
        

    
    def nbrDaysWorked(self):
        return self.nbr_days_worked
        
    def listHoursWorked(self):
        return []


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = FromEvernoteToTimeSaver()
    myapp.show()
    
    exit_code = app.exec_()
    sys.exit(exit_code)