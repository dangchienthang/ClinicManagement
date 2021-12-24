from django.urls import path
from clinic.views import *


urlpatterns = [
    path('', homepage, name='homepage'),
    path('about/', aboutpage, name='aboutpage'),
    path('login/', loginpage, name='loginpage'),
    path('createaccount/', createaccountpage, name='createaccountpage'),
    path('admin_login/', login_admin, name='login_admin'),
    path('adminhome/', AdminHome, name='adminhome'),
    path('adminlogout/', logout_admin, name='adminlogout'),
    path('adminadddoctor/', admin_add_doctor, name='adminaddDoctor'),
    path('adminviewDdoctor/', admin_view_doctor, name='adminviewDoctor'),
    path('adminDeleteDoctor<int:pid><str:email>', admin_delete_doctor, name='admin_delete_doctor'),
    path('adminaddNurse/', admin_add_nurse, name='adminaddReceptionist'),
    path('adminviewNurse/', admin_view_nurse, name='adminviewReceptionist'),
    path('adminDeleteNurse<int:pid>,<str:email>', admin_delete_receptionist, name='admin_delete_receptionist'),
    path('adminviewAppointment/', admin_view_appointment, name='adminviewAppointment'),
    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),
    path('makeappointments/', make_appointments, name='makeappointments'),
    path('viewappointments/', viewappointments, name='viewappointments'),
    path('PatientDeleteAppointment<int:pid>', patient_delete_appointment, name='patient_delete_appointment'),
    path('logout/', Logout, name='logout'),
]
