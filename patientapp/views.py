from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from.models import patientregister,pay
from Adminapp.models import Login
from medoffapp.models import doctorsregister,shedule,eprescripotion
from patientapp.models import appointment


def indexx(request):
    context={}
    template=loader.get_template("index.html")
    return HttpResponse(template.render(context,request))

def patienthome(request):
    context={}
    template=loader.get_template("patienthomepg.html")
    return HttpResponse(template.render(context,request))

def patientreg(request):
    if request.method=='POST':
        r = patientregister()
        l = Login()
        name = request.POST.get("name")
        hname = request.POST.get("Address")
        gender = request.POST.get("gender")
        phone = request.POST.get("phone")
        age = request.POST.get("age")
        uname = request.POST.get("username")
        pwd = request.POST.get("password")
        #email = request.POST.get("email")

        r.Name = name
        r.Address = hname
        r.Gender = gender
        r.Contact = phone
        r.Age = age
        r.Username = uname
        r.Password = pwd
        r.status="pending"

        r.save()
        l.Uname = uname
        l.Pwd = pwd
        l.Utype = 'User'
        l.save()
        return HttpResponse("<script>alert('Inserted Successfully');window.location='/patientreg'</script>")
    else:
        context={}
        template=loader.get_template("patientreg.html")
        return HttpResponse(template.render(context,request))


# def patientlog(request):
#     context={}
#     template=loader.get_template("patientlog.html")
#     return HttpResponse(template.render(context,request))


def patientlog(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        request.session["uname"]=uname
        pwd=request.POST.get('password')
        if(Login.objects.filter(Uname=uname,Pwd=pwd)):
            li=Login.objects.filter(Uname=uname,Pwd=pwd)
            for i in li:
                if(i.Utype == "Admin"):
                    request.session["uname"] = uname
                    context = {}
                    template = loader.get_template("adminpage.html")
                    return HttpResponse(template.render(context, request))
                elif (i.Utype == "User"):
                    u = patientregister.objects.get(Username=uname)
                    if (u.status == "pending"):
                        return HttpResponse("<script>alert('NoT Approved by admin');window.location='/patientlog';</script>")
                    else:
                        request.session["uname"] = uname
                        context = {}
                        template = loader.get_template("patienthomepg.html")
                        return HttpResponse(template.render(context, request))

                elif(i.Utype == "Doctor"):
                    u=doctorsregister.objects.get(uname=uname)
                    if(u.status=="pending"):
                        return HttpResponse("<script>alert('NoT Approved by admin');window.location='/patientlog';</script>")
                    else:
                        request.session["doc_id"] = u.id
                        request.session["uname"]=uname

                        context = {}
                        template = loader.get_template("doctors.html")
                        return HttpResponse(template.render(context, request))
                # elif (i.utype == "lawyer"):
                #     u = lawyerreg.objects.get(uname=uname)
                #     if (u.status == "pending"):
                #         return HttpResponse("<script>alert('NoT Approved by admin');window.location='/login';</script>")
                #     else:
                #         request.session["uname"] = uname
                #         context = {}
                #         template = loader.get_template("lawerhome.html")
                #         return HttpResponse(template.render(context,request))
                # elif (i.utype == "officer"):
                #     request.session["uname"] = uname
                #
                #     context = {}
                #     template = loader.get_template("officerhome.html")
                #     return HttpResponse(template.render(context, request))
                # elif (i.utype == "station"):
                #     request.session["uname"] = uname
                #
                #     context = {}
                #     template = loader.get_template("stationhome.html")
                #     return HttpResponse(template.render(context, request))
        else:
            return HttpResponse("<script>alert('invalid uname or pwd');window.location='/patientlog';</script>")
    else:

        context = {}
        template = loader.get_template("patientlog.html")
        return HttpResponse(template.render(context, request))

def element(request):
    context={}
    template=loader.get_template("elements.html")
    return HttpResponse(template.render(context,request))

def patientappointment(request):
    if request.method == 'POST':
        r = appointment()
        name = request.POST.get("name")
        email = request.POST.get("email")
        date = request.POST.get("datepicker")
        symptoms = request.POST.get("Symptoms")
        contact = request.POST.get("contact")

        r.Name = name
        r.Email = email
        r.Date = date
        r.Symptoms = symptoms
        r.Contact = contact
        r.status = 'pending'
        r.save()
        return HttpResponse("<script>alert('Booking added  Successfully');window.location='/appointment'</script>")
    else:
        uname = request.session["uname"]
        r1 = patientregister.objects.raw("select * from patientapp_patientregister where Username=%s", [uname])
        template=loader.get_template("appointment.html")
        context = {'key': r1}
        return HttpResponse(template.render(context,request))
def medicaltips(request):
    context={}
    template=loader.get_template("medicaltips.html")
    return HttpResponse(template.render(context,request))
def bill(request):
    d=eprescripotion.objects.all()
    context={'key':d}
    template=loader.get_template("billamount.html")
    return HttpResponse(template.render(context,request))
def addaccount(request):
    if request.method=='POST':
        r = pay()
        bank = request.POST.get("bankname")
        branch = request.POST.get("branchname")
        cardno = request.POST.get("cno")
        cardholder = request.POST.get("cname")
        amount = request.POST.get("amount")
        r.BankName=bank
        r.Branch=branch
        r.cardno=cardno
        r.cardholder=cardholder
        r.amount=amount
        r.save()
        return HttpResponse("<script>alert('payment Successfully');window.location='/patienthome'</script>")
    else:
        context = {}
        template = loader.get_template("addaccount.html")
        return HttpResponse(template.render(context, request))

def medicalhistory(request):
    e=eprescripotion.objects.all()
    context={'key':e}
    template=loader.get_template("p_medicalhistory.html")
    return HttpResponse(template.render(context,request))

def departments(request):
    context={}
    template=loader.get_template("department.html")
    return HttpResponse(template.render(context,request))