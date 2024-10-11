from django.urls import path
import Adminapp.views

urlpatterns = [
    path('adminhome/',Adminapp.views.adminhome,name="adminhome"),
    path('adddptr/', Adminapp.views.adddepartment, name="adddptr"),
    path('viewdoctorlist/', Adminapp.views.viewdoctorlist, name="viewdoctorlist"),
    path('doctordtls/<id>', Adminapp.views.doctordtls, name="doctordtls"),
    path('approvedoc/<id>', Adminapp.views.approvedoc, name="approvedoc"),
    path('rejectdoc/<id>', Adminapp.views.rejectdoc, name="rejectdoc"),
    path('viewpatientslist/', Adminapp.views.viewpatientslist, name="viewpatientslist"),
    path('approvepatient/<id>', Adminapp.views.approvepatient, name="approvepatient"),
    path('viewapprovedpatientslist/', Adminapp.views.viewapprovedpatientslist, name="viewapprovedpatientslist"),
    path('viewappointment', Adminapp.views.viewappointment, name="viewappointment"),
    path('appointmentsdtls/<id>', Adminapp.views.appointmentsdtls, name="appointmentsdtls"),
    path('approveappointments/<id>', Adminapp.views.approveappointments, name="approveappointments"),
    path('get-doctors1/', Adminapp.views.get_doctors1, name='get_doctors1'),
    # path('get_doctors/<str:specialization>/',Adminapp.views.get_doctors, name='get_doctors'),
    path('get_doctors/<str:specialization>/', Adminapp.views.get_doctors, name='get_doctors'),
    path('assignduty', Adminapp.views.assignduty, name="assignduty"),

]