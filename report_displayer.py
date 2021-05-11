import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

class Report_Table(qtw.QMainWindow):
    def __init__(self,file_location):
        super().__init__()
        self.setGeometry(0,0,400,500)
        self.setWindowTitle('Report')
        report = open((str)(file_location),'r')
        report_lines = report.readlines()
        entries = len(report_lines)
        report_table = qtw.QTableWidget()
        report_table.verticalHeader().setDefaultSectionSize(50)
        report_table.horizontalHeader().setDefaultSectionSize(120)
        report_table.setRowCount(entries + 1)
        report_table.setColumnCount(3)
        report_table.setItem(0,0,qtw.QTableWidgetItem('First Student'))
        report_table.setItem(0,1,qtw.QTableWidgetItem('Second Student'))
        report_table.setItem(0,2,qtw.QTableWidgetItem('Percentage Similarity'))
        for i in range(entries):
            cur = report_lines[i].split('\t')
            report_table.setItem(i + 1,0,qtw.QTableWidgetItem(cur[0]))
            report_table.setItem(i + 1,1,qtw.QTableWidgetItem(cur[1]))
            report_table.setItem(i + 1,2,qtw.QTableWidgetItem(cur[2]))
        self.setCentralWidget(report_table)