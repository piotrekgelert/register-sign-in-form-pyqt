# register-sign-in-form-pyqt
Full login system with login, sign up, create new password forms made with 
pyqt6 and phpAdmin in Python 3.87

## ui examples
<p align="middle">
  <img src="https://github.com/piotrekgelert/register-sign-in-form-pyqt/blob/main/images/login.png" width="30%"/>
  <img src="https://github.com/piotrekgelert/register-sign-in-form-pyqt/blob/main/images/register.png" width="30%"/>
  <img src="https://github.com/piotrekgelert/register-sign-in-form-pyqt/blob/main/images/forgot_pass.png" width="30%"/>
</p>

### notes
- [x] uses XAMP and phpMyAdmin
- [x] password is encrypted with Hash
- [x] to change password first name and DOB is needed, next answer the question
- [x] email is treated as an ID

### used packages:
To create this register\sign in form I used libraries and apps:
- [pyqt6](https://pypi.org/project/PyQt6/)
- [pyqt5-tools](https://pypi.org/project/pyqt5-tools/)
- [mysql_connector](https://pypi.org/project/mysql-connector-python/)
- [pyqt_designer](https://build-system.fman.io/qt-designer-download)
- [xampp](https://www.apachefriends.org/download.html)



### running the project
App can be opened from `App_main/main.py` file only to see it,
or from `App_logged_in/main_logged_in.py` if you want to operate it, remember
to start phpMyAdmin first and add:
- database: 'people'
- table: 'users'
- columns: 'fname', 'lname', 'email', 'password', 'dob_date', 'question', 'answer'

### icons created by:
- [Ivan Repin](https://www.flaticon.com/authors/ivan-repin)
- [Rutmer Zijlstra](https://www.flaticon.com/authors/rutmer-zijlstra)
- [smashingstocks](https://www.flaticon.com/authors/smashingstocks)
- [Creative Stall Premium](https://www.flaticon.com/authors/creative-stall-premium)
- [Nsu Rabo Elijah](https://www.flaticon.com/authors/nsu-rabo-elijah)
- [Roundicons](https://www.flaticon.com/authors/roundicons)

### licence
This project is licensed under the [MIT] License - see [Licence.md](LICENSE) file for details.