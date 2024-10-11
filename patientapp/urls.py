from django.urls import path
import patientapp.views
urlpatterns = [
    path('',patientapp.views.indexx,name="index"),
    path('departments',patientapp.views.departments,name="departments"),
    path('patienthome/', patientapp.views.patienthome, name="patienthome"),
    path('patientreg/', patientapp.views.patientreg, name="patientreg"),
    path('patientlog/', patientapp.views.patientlog, name="patientlog"),
    path('appointment/', patientapp.views.patientappointment, name="appointment"),
    path('medicaltips/', patientapp.views.medicaltips, name="medicaltips"),
    path('bill/', patientapp.views.bill, name="bill"),
    path('addaccount/', patientapp.views.addaccount, name="addaccount"),
    #path('bill/', patientapp.views.bill, name="bill"),
    path('medicalhistory/', patientapp.views.medicalhistory, name="medicalhistory"),


]