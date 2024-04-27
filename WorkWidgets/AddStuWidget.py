from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import *

class AddStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("add_stu_widget")
        
        layout = QtWidgets.QGridLayout()
        
        header_label = LabelComponent(20, "Add Student")
        
        name_label = LabelComponent(16, "Name: ")
        self.name_label = LineEditComponent("Name")
        self.name_label.mousePressEvent = lambda event, le=self.name_label: le.clear()

        query_button = ButtonComponent("Query")
        query_button.clicked.connect(self.query_name) 
        self.result_label = LabelComponent(16, "")

        subject_label = LabelComponent(16, "Subject: ")
        self.subject_label = LineEditComponent("Subject")
        self.subject_label.mousePressEvent = lambda event, le=self.subject_label: le.clear()
        self.subject_label.setReadOnly(True)
        self.subject_label.mousePressEvent = self.subject_label_click_handler
        
        score_label = LabelComponent(16, "Score: ")
        self.score_label = NumberLineEditComponent("", 3, 100, 16)
        
        add_button = ButtonComponent("Add")
        add_button.clicked.connect(self.confirm_action)

        send_button = ButtonComponent("Send")
        send_button.clicked.connect(self.send_action)

        layout.addWidget(header_label, 0, 0, 1, 3) 
        layout.addWidget(name_label, 1, 0, 1, 1)
        layout.addWidget(self.name_label, 1, 1, 1, 2)
        layout.addWidget(query_button, 1, 3, 1, 1)
        
        layout.addWidget(subject_label, 2, 0, 1, 1)
        layout.addWidget(self.subject_label, 2, 1, 1, 2)
        
        layout.addWidget(score_label, 3, 0, 1, 1)
        layout.addWidget(self.score_label, 3, 1, 1, 2)
        layout.addWidget(add_button, 3, 3, 1, 1)
        layout.addWidget(send_button, 5, 5, 1, 2)

        layout.addWidget(self.result_label, 1, 5, 5, 3) 

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 3)
        layout.setColumnStretch(2, 3)
        layout.setColumnStretch(3, 1)
        layout.setColumnStretch(4, 1)
        layout.setColumnStretch(5, 3)
        layout.setColumnStretch(6, 3)
        layout.setColumnStretch(7, 3)
        
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 2)
        layout.setRowStretch(2, 2)
        layout.setRowStretch(3, 2)
        layout.setRowStretch(4, 5)
        layout.setRowStretch(5, 2)
        
        self.setLayout(layout)

    def subject_label_click_handler(self, event):
        event.ignore()

    def confirm_action(self):
        if not self.name_label.text().strip() or not self.subject_label.text().strip() or not self.score_label.text().strip():
            self.result_label.setText(f"Name, Subject, and Score cannot be empty.")
        else:
            self.result_label.setText(f"Name: {self.name_label.text()},\nSubject: {self.subject_label.text()},\nScore: {self.score_label.text()}")
    
    def send_action(self):
        if not self.name_label.text().strip() or not self.subject_label.text().strip() or not self.score_label.text().strip():
            self.result_label.setText(f"Name, Subject, and Score cannot be empty.")
        else:
            show="{"+f"'name': '{self.name_label.text()}', "+"'score': {"+f"'{self.subject_label.text()}': '{self.score_label.text()}'"+"}}"
            print(show)

    def query_name(self):
        if not self.name_label.text().strip():
            self.result_label.setText("Name cannot be empty.")
        else:
            name = self.name_label.text()
            self.result_label.setText(f"{name} does not exist")
            self.subject_label.setReadOnly(False)
            self.subject_label.mousePressEvent = lambda event: self.subject_label.clear()

    def clear_editor_content(self, event):
        sender = self.sender()
        if isinstance(sender, LineEditComponent):
            sender.clear()
