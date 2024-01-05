# register-sign-in-form-pyqt
Full login system with login, sign up, create new password forms made with 
pyqt6 in Python 3.87

## ui examples
<p align="middle">
  <img src="" width="300"/>
  <img src="" width="300"/>
  <img src="" width="300"/>
</p>

### notes
- [x] uses XAMP and phpMyAdmin
- [x] password is encrypted with Hash
- [x] to change password first name and DOB is needed, next answer the question
- [x] email is treated as an ID

### icons created by:
- [Ivan Repin](https://www.flaticon.com/authors/ivan-repin)
- [Rutmer Zijlstra](https://www.flaticon.com/authors/rutmer-zijlstra)
- [smashingstocks](https://www.flaticon.com/authors/smashingstocks)
- [Creative Stall Premium](https://www.flaticon.com/authors/creative-stall-premium)
- [Nsu Rabo Elijah](https://www.flaticon.com/authors/nsu-rabo-elijah)
- [Roundicons](https://www.flaticon.com/authors/roundicons)

### used packages:
[PyQt6 6.6.1](https://www.riverbankcomputing.com/software/pyqt/)


### running the project
App can be opened from `App_main/main.py` file only to see it,
or from `App_logged_in/main_logged_in.py` if you want to operate it, remember
to start phpMyAdmin first and add:
- database: 'people'
- table: 'users'
- columns: 'fname', 'lname', 'email', 'password', 'dob_date', 'question', 'answer'


### licence
This project is licensed under the [MIT] License - see [Licence.md](LICENSE) file for details.