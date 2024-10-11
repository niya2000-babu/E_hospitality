from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from.models import doctorsregister,shedule,eprescripotion
from Adminapp.models import Login,adddptr,assigndoctor
from patientapp.models import appointment,patientregister
from django.utils import timezone

from django.http import JsonResponse



def doctor(request):
    context={}
    template=loader.get_template("doctors.html")
    return HttpResponse(template.render(context,request))
def viewpatientrec(request):

    uname=request.session["uname"]
    doc_id=request.session["doc_id"]
    current_date = timezone.now().date()
    # p=patientregister.objects.raw("SELECT p. * FROM patientapp_patientregister p JOIN patientapp_appointment a ON p.Username = a.Email")
    # p=patientregister.objects.raw("SELECT p. *, d. * FROM patientapp_patientregister p JOIN Adminapp_assigndoctor d ON p.Username = d.Email")
    # p=patientregister.objects.raw("SELECT p. *, a. *, d. * FROM patientapp_patientregister p JOIN Adminapp_assigndoctor a ON p.Username = a.Email JOIN  medoffapp_doctorsregister d  ON a.Doctor = d.id")
    p = patientregister.objects.raw("SELECT    p. *, a. *, d. *, ap. * FROM patientapp_patientregister p JOIN Adminapp_assigndoctor a ON p.Username = a.Email JOIN medoffapp_doctorsregister d ON a.Doctor = d.id JOIN  patientapp_appointment ap ON ap.Email = a.Email where a.Doctor = %s and ap.Date >= %s",[doc_id,current_date])
    context = {'key':p }
    template=loader.get_template("viewpatientrecord.html")
    return HttpResponse(template.render(context,request))


def doctorreg(request):
    if request.method == 'POST':
        d = doctorsregister()
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        hname = request.POST.get("hname")
        street = request.POST.get("street")
        city = request.POST.get("city")
        state = request.POST.get("state")
        pin = request.POST.get("pin")
        country = request.POST.get("country")
        spcial = request.POST.get("ddlspecial")
        uname = request.POST.get("uname")
        pwd = request.POST.get("pwd")
        photo = request.FILES["photo"]
        qual = request.FILES["qual"]
        exp = request.FILES["exp"]
        d.Name = name
        d.Email = email
        d.Contact = phone
        d.Address = hname
        d.street = street
        d.city = city
        d.state = state
        d.pin = pin
        d.country = country
        d.Specialization=spcial
        d.photo = photo
        d.qual = qual
        d.exp = exp
        d.uname = uname
        d.pwd = pwd
        d.status = 'pending'
        l = Login()
        l.Uname = uname
        l.Pwd = pwd
        l.Utype = 'Doctor'
        l.save()
        d.save()
        return HttpResponse("<script>alert('Inserted Successfully');window.location='/doctorreg'</script>")
    else:
        b = adddptr.objects.all()
        context={'dptdwn':b}
        template=loader.get_template("doctoresregistration.html")
        return HttpResponse(template.render(context,request))

    # else:
    #     b = Bank.objects.all()
    #     template = loader.get_template("AddAccount.html")
    #     context = {'bank': b}
    #     return HttpResponse(template.render(context, request))
def viewdoctor(request):
    m =doctorsregister.objects.filter(status='pending')
    # n=payment.objects.all()
    # context = {'key':m,'amt':n}
    context = {'key': m}
    template = loader.get_template("doctorprofile.html")
    return HttpResponse(template.render(context, request))





def pschedule(request):
    if request.method == 'POST':
        d = shedule()
        name = request.POST.get("name")
        age = request.POST.get("age")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        time = request.POST.get("timepicker")

        d.Name = name
        d.Age = age
        d.Contact = contact
        d.Email = email
        d.Gender = gender
        d.Time = time

        d.save()
        return HttpResponse("<script>alert('scheduled Successfully...');window.location='/doctor'</script>")
    else:
        context = {}
        template = loader.get_template("appointmentsheduling.html")
        return HttpResponse(template.render(context, request))

def prescription(request):
    if request.method == 'POST':
        d = eprescripotion()
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        medicines = request.POST.get("medicines")
        test = request.POST.get("test")
        bill = request.POST.get("bill")


        d.Name = name
        d.Age = age
        d.Gender = gender
        d.Medicines = medicines
        d.Gender = gender
        d.Test = test
        d.bill = bill


        d.save()
        return HttpResponse("<script>alert('prescription send Successfully');window.location='/doctor'</script>")
    else:
        context={}
        template=loader.get_template("e_priscriptions.html")
        return HttpResponse(template.render(context,request))
