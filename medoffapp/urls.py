from django.urls import path
import medoffapp.views
urlpatterns = [
    path('doctor/',medoffapp.views.doctor,name="doctor"),
    path('doctorreg/', medoffapp.views.doctorreg, name="doctorreg"),
    path('viewpatientrec/', medoffapp.views.viewpatientrec, name="viewpatientrec"),

    # path('appointmentsheduling/', medoffapp.views.appointmentsheduling, name="appointmentsheduling"),
    # path('next-page/', medoffapp.views.next_page_view, name='next_page_view'),
    path('pschedule-page/', medoffapp.views.pschedule, name='pschedule'),
    path('prescription/', medoffapp.views.prescription, name='prescription'),


]