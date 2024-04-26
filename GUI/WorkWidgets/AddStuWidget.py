from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent


class AddStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("add_stu_widget")

        layout = QtWidgets.QGridLayout()

        header_label = LabelComponent(19, "Add Student")
        content_label_name = LabelComponent(16, "Name: ")
        content_label_subject = LabelComponent(16, "Subject: ")
        content_label_score = LabelComponent(16, "Score: ")
        self.content_label_response = LabelComponent(16, "", "color:red;")

        self.editor_label_name = LineEditComponent("Name")
        self.editor_label_subject = LineEditComponent("Subject")
        self.editor_label_score = LineEditComponent()
        self.editor_label_score.setValidator(QtGui.QIntValidator())
        self.editor_label_name.mousePressEvent = self.editor_label_name.clear_editor_content
        self.editor_label_subject.mousePressEvent = self.editor_label_subject.clear_editor_content
        self.editor_label_subject.disable()
        self.editor_label_score.disable()

        self.button_query = ButtonComponent("Query")
        self.button_add = ButtonComponent("Add")
        self.button_send = ButtonComponent("Send")
        self.button_query.clicked.connect(self.query)
        self.button_add.clicked.connect(self.add)
        self.button_send.clicked.connect(self.send)        

        layout.addWidget(header_label, 0, 0, 1, 2)
        layout.addWidget(self.content_label_response, 0, 4, 5, 1)
        layout.addWidget(content_label_name, 1, 0, 1, 1)
        layout.addWidget(content_label_subject, 2, 0, 1, 1)
        layout.addWidget(content_label_score, 3, 0, 1, 1)
        layout.addWidget(self.editor_label_name, 1, 1, 1, 1)
        layout.addWidget(self.editor_label_subject, 2, 1, 1, 1)
        layout.addWidget(self.editor_label_score, 3, 1, 1, 1)
        layout.addWidget(self.button_query, 1, 2, 1, 1)
        layout.addWidget(self.button_add, 3, 2, 1, 1)
        layout.addWidget(self.button_send, 6, 3, 1, 2)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 3)
        layout.setColumnStretch(3, 1)
        layout.setColumnStretch(4, 3)

        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 2)
        layout.setRowStretch(2, 2)
        layout.setRowStretch(3, 2)
        layout.setRowStretch(4, 2)
        layout.setRowStretch(5, 2)
        layout.setRowStretch(6, 2)

        self.setLayout(layout)

    def query(self):
        if self.editor_label_name.text() == "" or self.editor_label_name.text() == "Name":
            self.content_label_response.setText("Please input the data.")
        else:
            name = self.editor_label_name.text()
            self.editor_label_subject.enable()
            self.editor_label_score.enable()
            self.content_label_response.setText("Your name is: "+str(name))
            print(f"name: {name}")

    def add(self):
        if self.editor_label_subject.text() == "" or self.editor_label_subject.text() == "Subject":
            self.content_label_response.setText("Please input the data.")
        else:
            add_dict={self.editor_label_subject.text():self.editor_label_score.text()}
            self.content_label_response.setText("Your subject and score is: "+str(add_dict))
            print("Your subject and score is {}".format(add_dict))

    def send(self):
        if self.editor_label_name.text() == "" or self.editor_label_subject.text() == "" or self.editor_label_score.text() == "":
            self.content_label_response.setText("Please input the data.")
        else:
            response={'name': self.editor_label_name.text(), 'scores': {self.editor_label_subject.text():self.editor_label_score.text()}}
            print("Student info is {}".format(response))
            self.content_label_response.setText("Student info: "+str(response))
            self.editor_label_name.setText("Name")
            self.editor_label_subject.setText("Subject")
            self.editor_label_score.setText("")
            self.editor_label_subject.disable()
            self.editor_label_score.disable()
    