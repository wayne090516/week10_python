from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent


class AddStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("add_stu_widget")

        layout = QtWidgets.QGridLayout()

        header_label = LabelComponent(20, "Add Student")
        content_label_name = LabelComponent(16, "Name: ")
        self.editor_label_name = LineEditComponent("Name")
        self.editor_label_name.mousePressEvent = self.editor_label_name.clear_editor_content
        self.editor_label_name.textChanged.connect(self.name_change)
        self.button_query = ButtonComponent("Query")
        self.button_query.clicked.connect(self.querypush)
        self.button_query.disable()

        layout.addWidget(header_label, 0, 0, 1, 2)
        layout.addWidget(content_label_name, 1, 0, 1, 1)
        layout.addWidget(self.editor_label_name, 1, 1, 1, 1)
        layout.addWidget(self.button_query, 1, 2, 1, 1)

        content_label_subject = LabelComponent(16, "Subject: ")
        self.editor_label_subject = LineEditComponent("Subject")
        self.editor_label_subject.mousePressEvent = self.editor_label_subject.clear_editor_content
        self.editor_label_subject.disable()

        layout.addWidget(content_label_subject, 2, 0, 1, 1)
        layout.addWidget(self.editor_label_subject, 2, 1, 1, 1)

        content_label_score = LabelComponent(16, "Score: ")
        self.editor_label_score = LineEditComponent()
        self.editor_label_score.mousePressEvent = self.editor_label_score.clear_editor_content
        self.editor_label_score.disable()
        self.editor_label_score.setValidator(QtGui.QIntValidator())
        self.editor_label_score.textChanged.connect(self.score_change)
        self.button_add = ButtonComponent("Add")
        self.button_add.clicked.connect(self.add)
        self.button_add.disable()
        
        layout.addWidget(content_label_score, 3, 0, 1, 1)
        layout.addWidget(self.editor_label_score, 3, 1, 1, 1)
        layout.addWidget(self.button_add, 3, 2, 1, 1)

        self.content_label_respon = LabelComponent(16, "", "color:red;")
        button_send = ButtonComponent("Send")
        button_send.clicked.connect(self.send)

        layout.addWidget(self.content_label_respon, 0, 4, 5, 1)
        layout.addWidget(button_send, 6, 4, 1, 1)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 6)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)
        layout.setColumnStretch(4, 4)

        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 2)
        layout.setRowStretch(2, 2)
        layout.setRowStretch(3, 2)
        layout.setRowStretch(4, 2)
        layout.setRowStretch(5, 2)
        layout.setRowStretch(6, 2)
        self.setLayout(layout)


        
    def querypush(self):
        print("Name :" +self.editor_label_name.text())
        self.editor_label_subject.enable()
        self.editor_label_score.enable()

    def name_change(self):
        if self.editor_label_name.text() !="":
            self.button_query.enable()
    
    def score_change(self):
        if self.editor_label_score.text() !="":
            self.button_add.enable()

    def add(self):
        if (self.editor_label_name.text() ==""or self.editor_label_subject.text() =="" or self.editor_label_score.text() ==""):
            self.content_label_respon.setText("Please enter the score data")
        else:
            self.adddict={self.editor_label_subject.text():self.editor_label_score.text()}
            print(str(self.adddict))

    def send(self):
        if (self.editor_label_name.text() ==""or self.editor_label_subject.text() =="" or self.editor_label_score.text() ==""):
            self.content_label_respon.setText("Please enter the score data")
        else:
            text={'name': self.editor_label_name.text(), 'scores': {self.editor_label_subject.text():self.editor_label_score.text()}}
            print(text)
            self.content_label_respon.setText("The information"+str(text))
            self.editor_label_name.setText("Name")
            self.editor_label_subject.setText("Subject")
            self.editor_label_score.setText("")
            self.editor_label_subject.disable()
            self.editor_label_score.disable()
            self.button_query.disable()
            self.button_add.disable()