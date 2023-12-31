# Form implementation generated from reading ui file 'd:\Python_PORTFOLIO\9_Register_sign_in_form_pyqt6\App_main\UI\register_login.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_lw_main(object):
    def setupUi(self, lw_main):
        lw_main.setObjectName("lw_main")
        lw_main.setEnabled(True)
        lw_main.resize(664, 456)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        lw_main.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main/admin_thumb.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        lw_main.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=lw_main)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(150, 20, 501, 421))
        self.stackedWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pg_welcome = QtWidgets.QWidget()
        self.pg_welcome.setObjectName("pg_welcome")
        self.lb_main_logo = QtWidgets.QLabel(parent=self.pg_welcome)
        self.lb_main_logo.setGeometry(QtCore.QRect(170, 70, 131, 151))
        self.lb_main_logo.setText("")
        self.lb_main_logo.setPixmap(QtGui.QPixmap(":/buttons/logo_white_thumb.png"))
        self.lb_main_logo.setObjectName("lb_main_logo")
        self.lb_welcome = QtWidgets.QLabel(parent=self.pg_welcome)
        self.lb_welcome.setGeometry(QtCore.QRect(180, 240, 121, 21))
        self.lb_welcome.setObjectName("lb_welcome")
        self.stackedWidget.addWidget(self.pg_welcome)
        self.pg_login = QtWidgets.QWidget()
        self.pg_login.setObjectName("pg_login")
        self.gb_login_frane = QtWidgets.QGroupBox(parent=self.pg_login)
        self.gb_login_frane.setGeometry(QtCore.QRect(10, 0, 481, 421))
        self.gb_login_frane.setTitle("")
        self.gb_login_frane.setObjectName("gb_login_frane")
        self.gb_login = QtWidgets.QGroupBox(parent=self.gb_login_frane)
        self.gb_login.setGeometry(QtCore.QRect(10, 10, 461, 121))
        self.gb_login.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gb_login.setFlat(True)
        self.gb_login.setObjectName("gb_login")
        self.layoutWidget = QtWidgets.QWidget(parent=self.gb_login)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 451, 34))
        self.layoutWidget.setObjectName("layoutWidget")
        self.hl_login_username = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.hl_login_username.setContentsMargins(0, 0, 0, 0)
        self.hl_login_username.setObjectName("hl_login_username")
        self.lb_login_email_icon = QtWidgets.QLabel(parent=self.layoutWidget)
        self.lb_login_email_icon.setText("")
        self.lb_login_email_icon.setPixmap(QtGui.QPixmap(":/buttons/mail_white_thumb.png"))
        self.lb_login_email_icon.setObjectName("lb_login_email_icon")
        self.hl_login_username.addWidget(self.lb_login_email_icon)
        self.lb_login_email = QtWidgets.QLabel(parent=self.layoutWidget)
        self.lb_login_email.setObjectName("lb_login_email")
        self.hl_login_username.addWidget(self.lb_login_email)
        self.le_login_username = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.le_login_username.setObjectName("le_login_username")
        self.hl_login_username.addWidget(self.le_login_username)
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.gb_login)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 70, 451, 34))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.hl_login_password = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.hl_login_password.setContentsMargins(0, 0, 0, 0)
        self.hl_login_password.setObjectName("hl_login_password")
        self.lb_login_password_icon = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.lb_login_password_icon.setText("")
        self.lb_login_password_icon.setPixmap(QtGui.QPixmap(":/buttons/key_white_thumb.png"))
        self.lb_login_password_icon.setObjectName("lb_login_password_icon")
        self.hl_login_password.addWidget(self.lb_login_password_icon)
        self.lb_login_password = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.lb_login_password.setObjectName("lb_login_password")
        self.hl_login_password.addWidget(self.lb_login_password)
        self.le_login_password = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.le_login_password.setObjectName("le_login_password")
        self.hl_login_password.addWidget(self.le_login_password)
        self.layoutWidget2 = QtWidgets.QWidget(parent=self.gb_login_frane)
        self.layoutWidget2.setGeometry(QtCore.QRect(270, 330, 201, 42))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.hl_login_buttons = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.hl_login_buttons.setContentsMargins(0, 0, 0, 0)
        self.hl_login_buttons.setObjectName("hl_login_buttons")
        self.pb_login_login = QtWidgets.QPushButton(parent=self.layoutWidget2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/buttons/success_white_thumb.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_login_login.setIcon(icon1)
        self.pb_login_login.setIconSize(QtCore.QSize(32, 32))
        self.pb_login_login.setObjectName("pb_login_login")
        self.hl_login_buttons.addWidget(self.pb_login_login)
        self.pb_login_cancel = QtWidgets.QPushButton(parent=self.layoutWidget2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/buttons/cross_white_thumb.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_login_cancel.setIcon(icon2)
        self.pb_login_cancel.setIconSize(QtCore.QSize(32, 32))
        self.pb_login_cancel.setObjectName("pb_login_cancel")
        self.hl_login_buttons.addWidget(self.pb_login_cancel)
        self.layoutWidget3 = QtWidgets.QWidget(parent=self.gb_login_frane)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 380, 461, 34))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lb_login_message_icon = QtWidgets.QLabel(parent=self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_login_message_icon.sizePolicy().hasHeightForWidth())
        self.lb_login_message_icon.setSizePolicy(sizePolicy)
        self.lb_login_message_icon.setText("")
        self.lb_login_message_icon.setPixmap(QtGui.QPixmap(":/buttons/exclamation_mark_white_thumb.png"))
        self.lb_login_message_icon.setObjectName("lb_login_message_icon")
        self.horizontalLayout_3.addWidget(self.lb_login_message_icon)
        self.lb_login_message = QtWidgets.QLabel(parent=self.layoutWidget3)
        self.lb_login_message.setObjectName("lb_login_message")
        self.horizontalLayout_3.addWidget(self.lb_login_message)
        self.stackedWidget.addWidget(self.pg_login)
        self.pg_sign_in = QtWidgets.QWidget()
        self.pg_sign_in.setObjectName("pg_sign_in")
        self.gb_container_register = QtWidgets.QGroupBox(parent=self.pg_sign_in)
        self.gb_container_register.setGeometry(QtCore.QRect(10, 0, 481, 421))
        self.gb_container_register.setTitle("")
        self.gb_container_register.setFlat(False)
        self.gb_container_register.setCheckable(False)
        self.gb_container_register.setObjectName("gb_container_register")
        self.gb_register = QtWidgets.QGroupBox(parent=self.gb_container_register)
        self.gb_register.setGeometry(QtCore.QRect(10, 10, 461, 181))
        self.gb_register.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gb_register.setFlat(True)
        self.gb_register.setObjectName("gb_register")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.gb_register)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hl_register_fname = QtWidgets.QHBoxLayout()
        self.hl_register_fname.setObjectName("hl_register_fname")
        self.lb_register_fname_icon = QtWidgets.QLabel(parent=self.gb_register)
        self.lb_register_fname_icon.setText("")
        self.lb_register_fname_icon.setPixmap(QtGui.QPixmap(":/buttons/user_white_thumb.png"))
        self.lb_register_fname_icon.setObjectName("lb_register_fname_icon")
        self.hl_register_fname.addWidget(self.lb_register_fname_icon)
        self.lb_register_fname = QtWidgets.QLabel(parent=self.gb_register)
        self.lb_register_fname.setObjectName("lb_register_fname")
        self.hl_register_fname.addWidget(self.lb_register_fname)
        self.le_register_fname = QtWidgets.QLineEdit(parent=self.gb_register)
        self.le_register_fname.setObjectName("le_register_fname")
        self.hl_register_fname.addWidget(self.le_register_fname)
        self.verticalLayout.addLayout(self.hl_register_fname)
        self.hl_register_lname = QtWidgets.QHBoxLayout()
        self.hl_register_lname.setObjectName("hl_register_lname")
        self.lb_register_lname_icon = QtWidgets.QLabel(parent=self.gb_register)
        self.lb_register_lname_icon.setText("")
        self.lb_register_lname_icon.setPixmap(QtGui.QPixmap(":/buttons/user_white_thumb.png"))
        self.lb_register_lname_icon.setObjectName("lb_register_lname_icon")
        self.hl_register_lname.addWidget(self.lb_register_lname_icon)
        self.lb_register_lname = QtWidgets.QLabel(parent=self.gb_register)
        self.lb_register_lname.setObjectName("lb_register_lname")
        self.hl_register_lname.addWidget(self.lb_register_lname)
        self.le_register_lname = QtWidgets.QLineEdit(parent=self.gb_register)
        self.le_register_lname.setObjectName("le_register_lname")
        self.hl_register_lname.addWidget(self.le_register_lname)
        self.verticalLayout.addLayout(self.hl_register_lname)
        self.hl_register_email = QtWidgets.QHBoxLayout()
        self.hl_register_email.setObjectName("hl_register_email")
        self.lb_register_email_icon = QtWidgets.QLabel(parent=self.gb_register)
        self.lb_register_email_icon.setText("")
        self.lb_register_email_icon.setPixmap(QtGui.QPixmap(":/buttons/mail_white_thumb.png"))
        self.lb_register_email_icon.setObjectName("lb_register_email_icon")
        self.hl_register_email.addWidget(self.lb_register_email_icon)
        self.lb_register_email = QtWidgets.QLabel(parent=self.gb_register)
        self.lb_register_email.setObjectName("lb_register_email")
        self.hl_register_email.addWidget(self.lb_register_email)
        self.le_register_email = QtWidgets.QLineEdit(parent=self.gb_register)
        self.le_register_email.setObjectName("le_register_email")
        self.hl_register_email.addWidget(self.le_register_email)
        self.verticalLayout.addLayout(self.hl_register_email)
        self.hl_register_password = QtWidgets.QHBoxLayout()
        self.hl_register_password.setObjectName("hl_register_password")
        self.lb_register_password_icon = QtWidgets.QLabel(parent=self.gb_register)
        self.lb_register_password_icon.setText("")
        self.lb_register_password_icon.setPixmap(QtGui.QPixmap(":/buttons/key_white_thumb.png"))
        self.lb_register_password_icon.setObjectName("lb_register_password_icon")
        self.hl_register_password.addWidget(self.lb_register_password_icon)
        self.lb_register_password = QtWidgets.QLabel(parent=self.gb_register)
        self.lb_register_password.setObjectName("lb_register_password")
        self.hl_register_password.addWidget(self.lb_register_password)
        self.le_register_password = QtWidgets.QLineEdit(parent=self.gb_register)
        self.le_register_password.setObjectName("le_register_password")
        self.hl_register_password.addWidget(self.le_register_password)
        self.verticalLayout.addLayout(self.hl_register_password)
        self.gb_register_question = QtWidgets.QGroupBox(parent=self.gb_container_register)
        self.gb_register_question.setGeometry(QtCore.QRect(10, 200, 461, 111))
        self.gb_register_question.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gb_register_question.setFlat(True)
        self.gb_register_question.setObjectName("gb_register_question")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gb_register_question)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.hl_register_question = QtWidgets.QHBoxLayout()
        self.hl_register_question.setObjectName("hl_register_question")
        self.lb_register_question_icon = QtWidgets.QLabel(parent=self.gb_register_question)
        self.lb_register_question_icon.setText("")
        self.lb_register_question_icon.setPixmap(QtGui.QPixmap(":/buttons/Q_white_thumb.png"))
        self.lb_register_question_icon.setObjectName("lb_register_question_icon")
        self.hl_register_question.addWidget(self.lb_register_question_icon)
        self.lb_register_question = QtWidgets.QLabel(parent=self.gb_register_question)
        self.lb_register_question.setObjectName("lb_register_question")
        self.hl_register_question.addWidget(self.lb_register_question)
        self.le_register_question = QtWidgets.QLineEdit(parent=self.gb_register_question)
        self.le_register_question.setObjectName("le_register_question")
        self.hl_register_question.addWidget(self.le_register_question)
        self.verticalLayout_2.addLayout(self.hl_register_question)
        self.hl_register_answer = QtWidgets.QHBoxLayout()
        self.hl_register_answer.setObjectName("hl_register_answer")
        self.lb_register_answer_icon = QtWidgets.QLabel(parent=self.gb_register_question)
        self.lb_register_answer_icon.setText("")
        self.lb_register_answer_icon.setPixmap(QtGui.QPixmap(":/buttons/A_white_thumb.png"))
        self.lb_register_answer_icon.setObjectName("lb_register_answer_icon")
        self.hl_register_answer.addWidget(self.lb_register_answer_icon)
        self.lb_register_answer = QtWidgets.QLabel(parent=self.gb_register_question)
        self.lb_register_answer.setObjectName("lb_register_answer")
        self.hl_register_answer.addWidget(self.lb_register_answer)
        self.le_register_answer = QtWidgets.QLineEdit(parent=self.gb_register_question)
        self.le_register_answer.setObjectName("le_register_answer")
        self.hl_register_answer.addWidget(self.le_register_answer)
        self.verticalLayout_2.addLayout(self.hl_register_answer)
        self.layoutWidget4 = QtWidgets.QWidget(parent=self.gb_container_register)
        self.layoutWidget4.setGeometry(QtCore.QRect(270, 330, 201, 42))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.hl_register_buttons = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.hl_register_buttons.setContentsMargins(0, 0, 0, 0)
        self.hl_register_buttons.setObjectName("hl_register_buttons")
        self.pb_register_sign_up = QtWidgets.QPushButton(parent=self.layoutWidget4)
        self.pb_register_sign_up.setIcon(icon1)
        self.pb_register_sign_up.setIconSize(QtCore.QSize(32, 32))
        self.pb_register_sign_up.setObjectName("pb_register_sign_up")
        self.hl_register_buttons.addWidget(self.pb_register_sign_up)
        self.pb_register_cancel = QtWidgets.QPushButton(parent=self.layoutWidget4)
        self.pb_register_cancel.setIcon(icon2)
        self.pb_register_cancel.setIconSize(QtCore.QSize(32, 32))
        self.pb_register_cancel.setObjectName("pb_register_cancel")
        self.hl_register_buttons.addWidget(self.pb_register_cancel)
        self.layoutWidget5 = QtWidgets.QWidget(parent=self.gb_container_register)
        self.layoutWidget5.setGeometry(QtCore.QRect(10, 380, 461, 34))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lb_register_message_icon = QtWidgets.QLabel(parent=self.layoutWidget5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_register_message_icon.sizePolicy().hasHeightForWidth())
        self.lb_register_message_icon.setSizePolicy(sizePolicy)
        self.lb_register_message_icon.setText("")
        self.lb_register_message_icon.setPixmap(QtGui.QPixmap(":/buttons/exclamation_mark_white_thumb.png"))
        self.lb_register_message_icon.setObjectName("lb_register_message_icon")
        self.horizontalLayout_4.addWidget(self.lb_register_message_icon)
        self.lb_register_message = QtWidgets.QLabel(parent=self.layoutWidget5)
        self.lb_register_message.setObjectName("lb_register_message")
        self.horizontalLayout_4.addWidget(self.lb_register_message)
        self.stackedWidget.addWidget(self.pg_sign_in)
        self.pg_forgot = QtWidgets.QWidget()
        self.pg_forgot.setObjectName("pg_forgot")
        self.gb_reset_password = QtWidgets.QGroupBox(parent=self.pg_forgot)
        self.gb_reset_password.setGeometry(QtCore.QRect(10, 0, 481, 421))
        self.gb_reset_password.setTitle("")
        self.gb_reset_password.setObjectName("gb_reset_password")
        self.gb_forgot_password = QtWidgets.QGroupBox(parent=self.gb_reset_password)
        self.gb_forgot_password.setGeometry(QtCore.QRect(10, 10, 461, 271))
        self.gb_forgot_password.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gb_forgot_password.setFlat(True)
        self.gb_forgot_password.setObjectName("gb_forgot_password")
        self.layoutWidget6 = QtWidgets.QWidget(parent=self.gb_forgot_password)
        self.layoutWidget6.setGeometry(QtCore.QRect(10, 30, 451, 34))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.hl_reset_email = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.hl_reset_email.setContentsMargins(0, 0, 0, 0)
        self.hl_reset_email.setObjectName("hl_reset_email")
        self.lb_reset_email_icon = QtWidgets.QLabel(parent=self.layoutWidget6)
        self.lb_reset_email_icon.setText("")
        self.lb_reset_email_icon.setPixmap(QtGui.QPixmap(":/buttons/user_white_thumb.png"))
        self.lb_reset_email_icon.setObjectName("lb_reset_email_icon")
        self.hl_reset_email.addWidget(self.lb_reset_email_icon)
        self.lb_reset_email = QtWidgets.QLabel(parent=self.layoutWidget6)
        self.lb_reset_email.setObjectName("lb_reset_email")
        self.hl_reset_email.addWidget(self.lb_reset_email)
        self.le_reset_email = QtWidgets.QLineEdit(parent=self.layoutWidget6)
        self.le_reset_email.setObjectName("le_reset_email")
        self.hl_reset_email.addWidget(self.le_reset_email)
        self.layoutWidget7 = QtWidgets.QWidget(parent=self.gb_forgot_password)
        self.layoutWidget7.setGeometry(QtCore.QRect(10, 130, 451, 34))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.hl_reset_answer = QtWidgets.QHBoxLayout(self.layoutWidget7)
        self.hl_reset_answer.setContentsMargins(0, 0, 0, 0)
        self.hl_reset_answer.setObjectName("hl_reset_answer")
        self.lb_reset_answer_icon = QtWidgets.QLabel(parent=self.layoutWidget7)
        self.lb_reset_answer_icon.setText("")
        self.lb_reset_answer_icon.setPixmap(QtGui.QPixmap(":/buttons/A_white_thumb.png"))
        self.lb_reset_answer_icon.setObjectName("lb_reset_answer_icon")
        self.hl_reset_answer.addWidget(self.lb_reset_answer_icon)
        self.le_reset_answer = QtWidgets.QLineEdit(parent=self.layoutWidget7)
        self.le_reset_answer.setObjectName("le_reset_answer")
        self.hl_reset_answer.addWidget(self.le_reset_answer)
        self.layoutWidget8 = QtWidgets.QWidget(parent=self.gb_forgot_password)
        self.layoutWidget8.setGeometry(QtCore.QRect(10, 180, 451, 34))
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.hl_reset_new_pass = QtWidgets.QHBoxLayout(self.layoutWidget8)
        self.hl_reset_new_pass.setContentsMargins(0, 0, 0, 0)
        self.hl_reset_new_pass.setObjectName("hl_reset_new_pass")
        self.lb_reset_new_pass_icon = QtWidgets.QLabel(parent=self.layoutWidget8)
        self.lb_reset_new_pass_icon.setText("")
        self.lb_reset_new_pass_icon.setPixmap(QtGui.QPixmap(":/buttons/key_white_thumb.png"))
        self.lb_reset_new_pass_icon.setObjectName("lb_reset_new_pass_icon")
        self.hl_reset_new_pass.addWidget(self.lb_reset_new_pass_icon)
        self.lb_reset_new_pass = QtWidgets.QLabel(parent=self.layoutWidget8)
        self.lb_reset_new_pass.setObjectName("lb_reset_new_pass")
        self.hl_reset_new_pass.addWidget(self.lb_reset_new_pass)
        self.le_reset_new_pass = QtWidgets.QLineEdit(parent=self.layoutWidget8)
        self.le_reset_new_pass.setObjectName("le_reset_new_pass")
        self.hl_reset_new_pass.addWidget(self.le_reset_new_pass)
        self.layoutWidget9 = QtWidgets.QWidget(parent=self.gb_forgot_password)
        self.layoutWidget9.setGeometry(QtCore.QRect(10, 220, 451, 34))
        self.layoutWidget9.setObjectName("layoutWidget9")
        self.hl_reset_repeat_pass = QtWidgets.QHBoxLayout(self.layoutWidget9)
        self.hl_reset_repeat_pass.setContentsMargins(0, 0, 0, 0)
        self.hl_reset_repeat_pass.setObjectName("hl_reset_repeat_pass")
        self.lb_reset_repeat_pass_icon = QtWidgets.QLabel(parent=self.layoutWidget9)
        self.lb_reset_repeat_pass_icon.setText("")
        self.lb_reset_repeat_pass_icon.setPixmap(QtGui.QPixmap(":/buttons/key_white_thumb.png"))
        self.lb_reset_repeat_pass_icon.setObjectName("lb_reset_repeat_pass_icon")
        self.hl_reset_repeat_pass.addWidget(self.lb_reset_repeat_pass_icon)
        self.lb_reset_repeat_pass = QtWidgets.QLabel(parent=self.layoutWidget9)
        self.lb_reset_repeat_pass.setObjectName("lb_reset_repeat_pass")
        self.hl_reset_repeat_pass.addWidget(self.lb_reset_repeat_pass)
        self.le_reset_repeat_pass = QtWidgets.QLineEdit(parent=self.layoutWidget9)
        self.le_reset_repeat_pass.setObjectName("le_reset_repeat_pass")
        self.hl_reset_repeat_pass.addWidget(self.le_reset_repeat_pass)
        self.layoutWidget10 = QtWidgets.QWidget(parent=self.gb_forgot_password)
        self.layoutWidget10.setGeometry(QtCore.QRect(10, 90, 451, 34))
        self.layoutWidget10.setObjectName("layoutWidget10")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget10)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lb_reset_question_icon = QtWidgets.QLabel(parent=self.layoutWidget10)
        self.lb_reset_question_icon.setText("")
        self.lb_reset_question_icon.setPixmap(QtGui.QPixmap(":/buttons/Q_white_thumb.png"))
        self.lb_reset_question_icon.setObjectName("lb_reset_question_icon")
        self.horizontalLayout_2.addWidget(self.lb_reset_question_icon)
        self.lb_reset_question = QtWidgets.QLabel(parent=self.layoutWidget10)
        self.lb_reset_question.setObjectName("lb_reset_question")
        self.horizontalLayout_2.addWidget(self.lb_reset_question)
        self.layoutWidget11 = QtWidgets.QWidget(parent=self.gb_reset_password)
        self.layoutWidget11.setGeometry(QtCore.QRect(270, 330, 201, 42))
        self.layoutWidget11.setObjectName("layoutWidget11")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget11)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_reset_login = QtWidgets.QPushButton(parent=self.layoutWidget11)
        self.pb_reset_login.setIcon(icon1)
        self.pb_reset_login.setIconSize(QtCore.QSize(32, 32))
        self.pb_reset_login.setObjectName("pb_reset_login")
        self.horizontalLayout.addWidget(self.pb_reset_login)
        self.pb_reset_cancel = QtWidgets.QPushButton(parent=self.layoutWidget11)
        self.pb_reset_cancel.setIcon(icon2)
        self.pb_reset_cancel.setIconSize(QtCore.QSize(32, 32))
        self.pb_reset_cancel.setObjectName("pb_reset_cancel")
        self.horizontalLayout.addWidget(self.pb_reset_cancel)
        self.layoutWidget12 = QtWidgets.QWidget(parent=self.gb_reset_password)
        self.layoutWidget12.setGeometry(QtCore.QRect(10, 380, 461, 34))
        self.layoutWidget12.setObjectName("layoutWidget12")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget12)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lb_reset_message_icon = QtWidgets.QLabel(parent=self.layoutWidget12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_reset_message_icon.sizePolicy().hasHeightForWidth())
        self.lb_reset_message_icon.setSizePolicy(sizePolicy)
        self.lb_reset_message_icon.setText("")
        self.lb_reset_message_icon.setPixmap(QtGui.QPixmap(":/buttons/exclamation_mark_white_thumb.png"))
        self.lb_reset_message_icon.setObjectName("lb_reset_message_icon")
        self.horizontalLayout_5.addWidget(self.lb_reset_message_icon)
        self.lb_reset_message = QtWidgets.QLabel(parent=self.layoutWidget12)
        self.lb_reset_message.setObjectName("lb_reset_message")
        self.horizontalLayout_5.addWidget(self.lb_reset_message)
        self.stackedWidget.addWidget(self.pg_forgot)
        self.pg_inside = QtWidgets.QWidget()
        self.pg_inside.setObjectName("pg_inside")
        self.label = QtWidgets.QLabel(parent=self.pg_inside)
        self.label.setGeometry(QtCore.QRect(230, 180, 81, 21))
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.pg_inside)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 20, 121, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.pb_main_login = QtWidgets.QPushButton(parent=self.frame)
        self.pb_main_login.setGeometry(QtCore.QRect(10, 20, 101, 41))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/buttons/existing_user_white_thumb.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_main_login.setIcon(icon3)
        self.pb_main_login.setIconSize(QtCore.QSize(32, 32))
        self.pb_main_login.setObjectName("pb_main_login")
        self.pb_main_forgot_pass = QtWidgets.QPushButton(parent=self.frame)
        self.pb_main_forgot_pass.setGeometry(QtCore.QRect(0, 310, 121, 81))
        self.pb_main_forgot_pass.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.pb_main_forgot_pass.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.pb_main_forgot_pass.setAutoFillBackground(False)
        self.pb_main_forgot_pass.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.pb_main_forgot_pass.setFlat(True)
        self.pb_main_forgot_pass.setObjectName("pb_main_forgot_pass")
        self.pb_main_sign_in = QtWidgets.QPushButton(parent=self.frame)
        self.pb_main_sign_in.setGeometry(QtCore.QRect(10, 70, 101, 41))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/buttons/new_user_white_thumb.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_main_sign_in.setIcon(icon4)
        self.pb_main_sign_in.setIconSize(QtCore.QSize(32, 32))
        self.pb_main_sign_in.setAutoDefault(False)
        self.pb_main_sign_in.setDefault(False)
        self.pb_main_sign_in.setFlat(False)
        self.pb_main_sign_in.setObjectName("pb_main_sign_in")
        lw_main.setCentralWidget(self.centralwidget)

        self.retranslateUi(lw_main)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(lw_main)

    def retranslateUi(self, lw_main):
        _translate = QtCore.QCoreApplication.translate
        lw_main.setWindowTitle(_translate("lw_main", "Register_Login"))
        self.lb_welcome.setText(_translate("lw_main", "->WELCOME <-"))
        self.gb_login.setTitle(_translate("lw_main", "Log in"))
        self.lb_login_email.setText(_translate("lw_main", "Email:"))
        self.lb_login_password.setText(_translate("lw_main", "Password:"))
        self.pb_login_login.setText(_translate("lw_main", "Login"))
        self.pb_login_cancel.setText(_translate("lw_main", "Cancel"))
        self.lb_login_message.setText(_translate("lw_main", "Message"))
        self.gb_register.setTitle(_translate("lw_main", "Register"))
        self.lb_register_fname.setText(_translate("lw_main", "First name:"))
        self.lb_register_lname.setText(_translate("lw_main", "Last name:"))
        self.lb_register_email.setText(_translate("lw_main", "Email:"))
        self.lb_register_password.setText(_translate("lw_main", "Password:"))
        self.gb_register_question.setTitle(_translate("lw_main", "Add question and answer in case of forgotten password"))
        self.lb_register_question.setText(_translate("lw_main", "Question:"))
        self.lb_register_answer.setText(_translate("lw_main", "Answer:"))
        self.pb_register_sign_up.setText(_translate("lw_main", "Sign in"))
        self.pb_register_cancel.setText(_translate("lw_main", "Cancel"))
        self.lb_register_message.setText(_translate("lw_main", "Message"))
        self.gb_forgot_password.setTitle(_translate("lw_main", "Reset password"))
        self.lb_reset_email.setText(_translate("lw_main", "Email:"))
        self.lb_reset_new_pass.setText(_translate("lw_main", "New password:"))
        self.lb_reset_repeat_pass.setText(_translate("lw_main", "Repeat new password:"))
        self.lb_reset_question.setText(_translate("lw_main", "question ??????????????????????????????????????"))
        self.pb_reset_login.setText(_translate("lw_main", "Login"))
        self.pb_reset_cancel.setText(_translate("lw_main", "Cancel"))
        self.lb_reset_message.setText(_translate("lw_main", "Message"))
        self.label.setText(_translate("lw_main", "You are in"))
        self.pb_main_login.setText(_translate("lw_main", "log  in"))
        self.pb_main_forgot_pass.setText(_translate("lw_main", "Forgot\n"
"your\n"
"password?"))
        self.pb_main_sign_in.setText(_translate("lw_main", "sign in"))
