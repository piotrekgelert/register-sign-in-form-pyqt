import os
import pathlib
import sys

import mysql.connector as mc
import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg
import PyQt6.QtWidgets as qtw
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget
from UI.register_login_ui import Ui_lw_main


class Main(qtw.QMainWindow, Ui_lw_main):
    one_sygnal = qtc.pyqtSignal()
    q = ''
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_icons()

        self.stackedWidget.setCurrentWidget(self.pg_welcome)
        self.pb_main_login.clicked.connect(self.login_page)
        self.pb_main_sign_in.clicked.connect(self.signin_page)
        self.pb_main_forgot_pass.clicked.connect(self.forgot_page)
        
        self.pb_register_sign_up.clicked.connect(self.process_sign_in)
        self.pb_login_login.clicked.connect(self.process_log_in)
    
    def setup_icons(self):
        root = r''.format(pathlib.Path(__file__).parent.absolute().parent)
        main_path = os.path.join(root, 'App_icons')
        
        self.setWindowIcon(
            qtg.QIcon('{}\\{}'.format(main_path, 'admin_thumb.png'))
        )
        set_icon = self._icon_set(main_path)
        set_pixmap = self._pixmap_set(main_path)
        
        set_icon(self.pb_main_login, 'existing_user_white_thumb.png')
        set_icon(self.pb_main_sign_in, 'new_user_white_thumb.png')
        set_pixmap(self.lb_main_logo, 'logo_white_thumb.png')

        set_pixmap(self.lb_login_email_icon, 'mail_white_thumb.png')
        set_pixmap(self.lb_login_password_icon, 'key_white_thumb.png')
        set_icon(self.pb_login_login, 'success_white_thumb.png')
        set_icon(self.pb_login_cancel, 'cross_white_thumb.png')
        set_pixmap(self.lb_login_message_icon, 'exclamation_mark_white_thumb.png')

        set_pixmap(self.lb_register_fname_icon, 'user_white_thumb.png')
        set_pixmap(self.lb_register_lname_icon, 'user_white_thumb.png')
        set_pixmap(self.lb_register_email_icon, 'mail_white_thumb.png')
        set_pixmap(self.lb_register_password_icon, 'key_white_thumb.png')
        set_pixmap(self.lb_register_question_icon, 'Q_white_thumb.png')
        set_pixmap(self.lb_register_answer_icon, 'A_white_thumb.png')
        set_icon(self.pb_register_sign_up, 'success_white_thumb.png')
        set_icon(self.pb_register_cancel, 'cross_white_thumb.png')
        set_pixmap(self.lb_register_message_icon, 'exclamation_mark_white_thumb.png')
        
        set_pixmap(self.lb_reset_email_icon, 'mail_white_thumb.png')
        set_pixmap(self.lb_reset_question_icon, 'Q_white_thumb.png')
        set_pixmap(self.lb_reset_answer_icon, 'A_white_thumb.png')
        set_pixmap(self.lb_reset_new_pass_icon, 'key_white_thumb.png')
        set_pixmap(self.lb_reset_repeat_pass_icon, 'key_white_thumb.png')
        set_icon(self.pb_reset_login, 'success_white_thumb.png')
        set_icon(self.pb_reset_cancel, 'cross_white_thumb.png')
        set_pixmap(self.lb_reset_message_icon, 'exclamation_mark_white_thumb.png')


        # self.pb_main_login.setIcon(
        
        #     qtg.QIcon('{}\\{}'.format(main_path, 'existing_user_white_thumb.png'))
        # )
        # self.pb_main_sign_in.setIcon(
        #     qtg.QIcon('{}\\{}'.format(main_path, 'new_user_white_thumb.png'))
        # )
        # self.lb_logo.setPixmap(
        #     qtg.QPixmap('{}\\{}'.format(main_path, 'logo_white_thumb.png'))
        # )
        # 
        #     

    def _icon_set(self, path_main):
        def f(pb, button_name):
            return pb.setIcon(
                qtg.QIcon('{}\\{}'.format(path_main, button_name))
            )
        return f
    
    def _pixmap_set(self, path_main):
        def f(lb, label_name):
            return lb.setPixmap(
                qtg.QPixmap('{}\\{}'.format(path_main, label_name))
            )
        return f
    
    def login_page(self):
        self.stackedWidget.setCurrentWidget(self.pg_login)

    def signin_page(self):
        self.stackedWidget.setCurrentWidget(self.pg_sign_in)

    def forgot_page(self):
        self.stackedWidget.setCurrentWidget(self.pg_forgot)
    
    @qtc.pyqtSlot()
    def process_sign_in(self):
        try:
            db = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='people'
            )
            cursor = db.cursor()
            fname = self.le_register_fname.text()
            lname = self.le_register_lname.text()
            email = self.le_register_email.text()
            password = self.le_register_password.text()
            dob_date = '{}/{}/{}'.format(
                self.sb_register_dob_day.text(),
                self.sb_register_dob_month.text(),
                self.sb_register_dob_year.text()
            )
            question = self.le_register_question.text()
            answer = self.le_register_answer.text()
            if all(len(x) > 0 for x in (fname, lname, email, password, dob_date, question, answer)):
                query = 'INSERT INTO users (fname, lname, email, password, dob_date, question, answer) VALUES (%s, %s, %s, %s, %s, %s, %s)'
                value = (fname, lname, email, password, question, answer)
                cursor.execute(query, value)
                db.commit()
                self.lb_register_message.setText('Creating account succesfull')
                self.le_register_fname.clear()
                self.le_register_lname.clear()
                self.le_register_email.clear()
                self.le_register_password.clear()
                self.le_register_question.clear()
                self.le_register_answer.clear()
                self.one_sygnal.emit()
            else:
                self.lb_register_message.setText('All fields are mandatory')
        except mc.Error as e:
            print(e)
            self.lb_register_message.setText('Creating account failed')
        
    @qtc.pyqtSlot()
    def process_log_in(self):
        try:
            db = mc.connect(
                host = 'localhost',
                user = 'root',
                password = '',
                database = 'people'
            )
            cursor = db.cursor()
            email = self.le_login_username.text()
            password = self.le_login_password.text()
            query = "SELECT email, password, question from users WHERE email like  '" + email + "'and password like '" + password + "'"
            cursor.execute(query)
            user_data = cursor.fetchone()
            if user_data is None:
                print(user_data)
                self.lb_login_message.setText('Incorrect email or password')
            else:
                self.one_sygnal.emit()
                self.lb_login_message.setText('You are log in successfully')
        except mc.Error as e:
            print(e.msg)
    
    def process_forgot(self):
        try:
            db = mc.connect(
                host = 'localhost',
                user = 'root',
                password = '',
                database = 'people'
            )
            cursor_check = db.cursor()
            fname, lname = self.lb_reset_name.text().split(' ')
            dob_date = '{}/{}/{}'.format(
                self.sb_reset_dob_day.text(),
                self.sb_reset_dob_day.text(),
                self.sb_reset_dob_day.text()
            )
            answer = self.le_reset_answer.text()
            
            q = 'SELECT users (fname, lname, dob_date, answer) VALUES (%s, %s, %s, %s)'
            v = (fname, lname, dob_date, answer)
            cursor_check.execute(q, v)
            check_data = cursor_check.fetchone()
            if check_data is None:
                self.lb_reset_message.setText('Repeat process, somewhere is mistake')
            else:
                new_pass = self.le_reset_new_pass.text()
                repeat_new_pass = self.le_reset_repeat_pass.text()
                if new_pass == repeat_new_pass:
                    cursor_change = db.cursor()
                    cursor_change.execute(
                        "UPDATE users SET password='%s' WHERE dob_date=%s", 
                        (new_pass, dob_date))
                    db.commit()
                    self.one_sygnal.emit()
                    self.lb_login_message.setText('You are log in successfully')

                
            # query = "SELECT dob_date, answer from users WHERE email like  '" +  dob_date + "' and answer like '" + answer +"'"
        except mc.Error as e:
            print(e.msg)
            

'''
in database add column  -> dob_date
'''


    



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())