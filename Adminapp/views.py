from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from medoffapp.models import doctorsregister
from patientapp.models import patientregister,appointment

from .models import adddptr,assigndoctor
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse



def adminhome(request):
    context={}
    template=loader.get_template("adminpage.html")
    return HttpResponse(template.render(context,request))
def adddepartment(request):
    if request.method == "POST":
        s=adddptr()
        dptr=request.POST.get("dptr")
        s.Department=dptr
        s.save()
        return HttpResponse("<script>alert('Department added successfully');window.location='/adddptr';</script>")
    else:
        context = {}
        template = loader.get_template("adddepartment.html")
        return HttpResponse(template.render(context, request))
def viewdoctorlist(request):
    alldoc=doctorsregister.objects.all()
    context = {'key': alldoc}
    template = loader.get_template("viewdoctors.html")
    return HttpResponse(template.render(context, request))
def doctordtls(request,id):
    id=doctorsregister.objects.get(id=id)
    context = {'key': id}
    template = loader.get_template("doctorprofile.html")
    return HttpResponse(template.render(context, request))

def approvedoc(request,id):
    r=doctorsregister.objects.get(id=id)

    email=r.Email
    r.status='approve'
    r.save()
    subject = 'You got an email from ehospital'
    message = 'Your request accepted successfully!!!!Now you can access your account'
    email_from = settings.EMAIL_HOST_USER
    mailid = email
    recipient_list = [mailid, ]
    send_mail(subject, message, email_from, recipient_list)

    return HttpResponse("<script>alert('Approved successfully');window.location='/viewdoctorlist';</script>")
def rejectdoc(request,id):
    r=doctorsregister.objects.get(id=id)
    request.session["email"]=r.Email
    r.status='reject'
    r.save()
    subject = 'You got an email from ehospital'
    message = 'Your request has declined!!!!Check your request...'
    email_from = settings.EMAIL_HOST_USER
    mailid = request.session["email"]
    recipient_list = [mailid, ]
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse("<script>alert('Rejected successfully');window.location='/viewdoctorlist';</script>")

def viewpatientslist(request):
    allpat=patientregister.objects.filter(status='pending')

    context = {'key': allpat}
    template = loader.get_template("viewpatients.html")
    return HttpResponse(template.render(context, request))
def approvepatient(request,id):
    r=patientregister.objects.get(id=id)

    email=r.Username
    r.status='approved'
    r.save()
    subject = 'You got an email from ehospital'
    message = 'Your request accepted successfully!!!!Now you can access your account'
    email_from = settings.EMAIL_HOST_USER
    mailid = email
    recipient_list = [mailid, ]
    send_mail(subject, message, email_from, recipient_list)

    return HttpResponse("<script>alert('Approved successfully');window.location='/viewpatientslist';</script>")
def viewapprovedpatientslist(request):
    allpat=patientregister.objects.filter(status='approved')

    context = {'key': allpat}
    template = loader.get_template("viewapprovedpatients.html")
    return HttpResponse(template.render(context, request))
def viewappointment(request):
    aponmnts=appointment.objects.all()
    for i in aponmnts:
        request.session["email"]= i.Email
    context = {'key': aponmnts}
    template = loader.get_template("viewappointments.html")
    return HttpResponse(template.render(context, request))
def appointmentsdtls(request,id):
    id=appointment.objects.get(id=id)
    context = {'key': id}
    template = loader.get_template("vieweachappointments.html")
    return HttpResponse(template.render(context, request))
def approveappointments(request,id):
    r=appointment.objects.get(id=id)
    email=r.Email
    r.status='approved'
    r.save()
    subject = 'You got an email from ehospital'
    message = 'Your request accepted successfully!!!!Now you can access your account'
    email_from = settings.EMAIL_HOST_USER
    mailid = email
    recipient_list = [mailid, ]
    send_mail(subject, message, email_from, recipient_list)

    return HttpResponse("<script>alert('Approved successfully');window.location='/viewappointment';</script>")




def get_doctors1(request):
    aponmnts=adddptr.objects.all()
    #aponmnts=doctorsregister.objects.all()
    #context = {'key': aponmnts}
    # if request.method == 'POST':
    #     doctors = doctorsregister.objects.filter(Specialization=specialization).values('Name')
    #     return JsonResponse(list(doctors), safe=False)
    # else:
    email = request.session["email"]
    r1 = appointment.objects.raw("select * from patientapp_appointment where Email=%s", [email])
    context = {'keyy': r1,'key': aponmnts}
    template = loader.get_template("assigndoctor.html")
    return HttpResponse(template.render(context, request))

def get_doctors(request, specialization):
    if request.method == 'GET':
        doctors = doctorsregister.objects.filter(Specialization=specialization).values('id','Name')
        return JsonResponse(list(doctors), safe=False)

#original code
# def get_doctors(request, specialization):
#     if request.method == 'POST':
#         doctors = doctorsregister.objects.filter(Specialization=specialization).values('Name')
#         return JsonResponse(list(doctors), safe=False)
#     else:
#         email = request.session["email"]
#         r1 = appointment.objects.raw("select * from patientapp_appointment where Email=%s", [email])
#         context = {'keyy': r1}
#         template = loader.get_template("assigndoctor.html")
#         return HttpResponse(template.render(context, request))
#
#     return HttpResponse(template.render(context,request))

def assignduty(request):
    if request.method == 'POST':
        r = assigndoctor()
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        symptoms = request.POST.get("symptoms")
        department = request.POST.get("ddldepartment")
        doctors = request.POST.get("ddldoctors")

        r.Name = name
        r.Contact = contact
        r.Email = email
        r.Symptoms = symptoms
        r.Department = department
        r.Doctor = doctors
        r.save()
        return HttpResponse("<script>alert('assigned   Successfully');window.location='/viewdoctorlist'</script>")
    else:

        template=loader.get_template("assigndoctor.html")
        context = {}
        return HttpResponse(template.render(context,request))