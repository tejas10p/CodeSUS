import sys
import os
import glob
import pathlib
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
import file_handler as fh   
import report_displayer as rd    

class Done(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: black')
        self.setWindowTitle('CodeSus')
        label = qtw.QLabel('Report Generated!',self)
        label.setStyleSheet('color: lime')
        label.setFont(qtg.QFont('HP Simplified',35))
        self.setCentralWidget(label)

class MainFrontEnd(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.waiting_window = None
        self.font_choice = 'HP Simplified'
        self.setStyleSheet('background-color: black')
        self.setWindowTitle('CodeSus')
        self.setGeometry(0,0,1200,800)
        main_window = qtw.QWidget()
        main_layout = qtw.QVBoxLayout(main_window)

        title = qtw.QLabel('CODESUS',self)
        title.setStyleSheet('color: lime')
        title.setFont(qtg.QFont(self.font_choice,50))
        title.setAlignment(qtc.Qt.AlignCenter)
        tabs = qtw.QTabWidget()
        main_tab = qtw.QWidget()
        about_us = qtw.QWidget()
        report_tab = qtw.QWidget()
        tabs.addTab(main_tab,'Main')
        tabs.addTab(report_tab,'Reports')
        tabs.addTab(about_us,'About Us')
        custom_tab_stylesheet = '''
                QTabBar::tab {
                background-color: black;
                color : lime;
                font-size : 15pt;
                height : 40px;
                width : 390px;
                border : 1px solid gray;
                }
                QTabBar::tab:selected {
                background-color: lime;
                color : black;
                }
                '''
        tabs.setStyleSheet(custom_tab_stylesheet)
        custom_layout = self.generate_main_page()
        custom_about_us = self.generate_about_us()
        custom_report_page = self.generate_report_page()
        main_layout.addWidget(title)
        main_layout.addWidget(tabs)
        main_tab.setLayout(custom_layout)
        about_us.setLayout(custom_about_us)
        report_tab.setLayout(custom_report_page)
        self.setCentralWidget(main_window)
        

    def generate_main_page(self):
        main_layout = qtw.QVBoxLayout()
        input_tab = qtw.QHBoxLayout()
        report_tab = qtw.QHBoxLayout()
        submit_layer = qtw.QHBoxLayout()
        
        folder_label = qtw.QLabel('Input Folder',self)
        folder_label.setStyleSheet('color: lime')
        folder_label.setFont(qtg.QFont(self.font_choice,20))

        report_label = qtw.QLabel('Report Name',self)
        report_label.setStyleSheet('color: lime')
        report_label.setFont(qtg.QFont(self.font_choice,20))

        select_button = qtw.QPushButton('Select Directory',self)
        select_button.setFont(qtg.QFont(self.font_choice,12))
        select_button.setStyleSheet('background-color: white')
        select_button.clicked.connect(self.select_dir)

        self.selected_directory = qtw.QLineEdit()
        self.selected_directory.setFont(qtg.QFont(self.font_choice,12))
        self.selected_directory.setStyleSheet('background-color: white')
        self.selected_directory.setReadOnly(True)

        self.report_name = qtw.QLineEdit()
        self.report_name.setFont(qtg.QFont(self.font_choice,12))
        self.report_name.setStyleSheet('background-color: white')

        submit_button = qtw.QPushButton('Submit',self)
        submit_button.setFont(qtg.QFont(self.font_choice,12))
        submit_button.setStyleSheet('background-color: white')
        submit_button.clicked.connect(self.send_data)

        input_tab.addWidget(folder_label)
        input_tab.addWidget(self.selected_directory)
        input_tab.addWidget(select_button)

        report_tab.addWidget(report_label)
        report_tab.addWidget(self.report_name)

        submit_layer.addStretch(1)
        submit_layer.addWidget(submit_button)
        submit_layer.addStretch(1)
        
        main_layout.addLayout(input_tab)
        main_layout.addLayout(report_tab)
        main_layout.addLayout(submit_layer)

        return main_layout

    def generate_about_us(self):
        main_layout = qtw.QVBoxLayout()
        tejas_label = qtw.QLabel('Tejas Pandey',self)
        tejas_label.setStyleSheet('color: lime')
        tejas_label.setFont(qtg.QFont(self.font_choice,20))
        
        varun_label = qtw.QLabel('Varun Singh',self)
        varun_label.setStyleSheet('color: lime')
        varun_label.setFont(qtg.QFont(self.font_choice,20))
        
        vivaan_label = qtw.QLabel('Vivaan Mishra',self)
        vivaan_label.setStyleSheet('color: lime')
        vivaan_label.setFont(qtg.QFont(self.font_choice,20))
        
        main_layout.addWidget(tejas_label)
        main_layout.addWidget(varun_label)
        main_layout.addWidget(vivaan_label)
        
        return main_layout

    def generate_report_page(self):
        main_layout = qtw.QVBoxLayout()
        button_layout = qtw.QHBoxLayout()
        self.report_table = qtw.QListWidget()
        self.report_table.setStyleSheet('color: lime')
        self.report_table.setFont(qtg.QFont(self.font_choice,20))
        self.location = str(pathlib.Path(__file__).parent.absolute())
        report_location = self.location + '\\' + "Reports" + '\\' + "*.txt"
        report_list = glob.glob(report_location)
        view_button = qtw.QPushButton('View Report',self)
        view_button.setFont(qtg.QFont(self.font_choice,12))
        view_button.setStyleSheet('background-color: white')
        view_button.clicked.connect(self.show_report)
        delete_button = qtw.QPushButton('Delete Report',self)
        delete_button.setFont(qtg.QFont(self.font_choice,12))
        delete_button.setStyleSheet('background-color: white')
        delete_button.clicked.connect(self.delete_report)
        button_layout.addWidget(view_button)
        button_layout.addWidget(delete_button)
        for i in report_list:
            name = qtw.QListWidgetItem(((str)(os.path.basename(i)))[:-4])
            self.report_table.addItem(name)
        main_layout.addWidget(self.report_table)
        main_layout.addLayout(button_layout)
        return main_layout

    def delete_report(self):
        selected_widget = self.report_table.currentItem()
        selected_name = selected_widget.text()
        report_file = self.location + '\\' + "Reports" + '\\' + selected_name + ".txt"
        self.report_table.takeItem(self.report_table.row(selected_widget))
        if(os.path.exists(report_file)):
            os.remove(report_file)

    def show_report(self):
        selected_name = self.report_table.currentItem().text()
        report_file = self.location + '\\' + "Reports" + '\\' + selected_name + ".txt"
        self.table = rd.Report_Table(report_file)
        self.table.show()

    def select_dir(self):
        self.folder = str(qtw.QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.show_folder()
        
    def show_folder(self):
        self.selected_directory.setText(self.folder)

    def send_data(self):
        report_arg = str(self.report_name.text())
        fh.file_bridge(self.folder,report_arg)
        add_to_reports = qtw.QListWidgetItem(report_arg)
        self.report_table.addItem(add_to_reports)
        self.show_done_window()
    
    def show_done_window(self):
        self.done_window = Done()
        self.done_window.show()
        self.timer = qtc.QTimer(self)
        self.timer.setInterval(2000)
        self.timer.timeout.connect(self.done_window.hide)
        self.timer.start()
        
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainFrontEnd()
    window.show()
    sys.exit(app.exec_())
