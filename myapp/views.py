

from django.shortcuts import render, redirect
from fontTools.misc.cython import returns
from google.protobuf.internal.test_bad_identifiers_pb2 import message
from reportlab.lib.pagesizes import elevenSeventeen

from myapp.models import Appointment,Comment, Member
from myapp.forms import AppointmentForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        if Member.objects.filter(
            username = request.POST['username'],
            password = request.POST['password']
        ).exists():
            return render(request, 'index.html')

        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def services(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')

def doctors(request):
    return render(request, 'doctors.html')

def myservice(request):
    return render(request, 'services.html')

def appointment(request):
    if request.method == 'POST':
       myappointment= Appointment(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message']
        )
       myappointment.save()
       return redirect('/show')

    else:
        return render(request, 'appointment.html')


def comment(request):
    if request.method == 'POST':
        mycomment = Comment(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message']
        )
        mycomment.save()
        return redirect('/comment')
    else:
        return render(request, 'comment.html')


def show(request):
    allappointments = Appointment.objects.all()
    return render(request, 'show.html',{'appointment':allappointments})

def delete(request,id):
    appoint = Appointment.objects.get(id=id)
    appoint.delete()
    return redirect('/show')

def edit(request, id):
    editappointment = Appointment.objects.get(id=id)
    return render(request, 'edit.html',{'appointment':editappointment})

def update(request,id):
    updateinfo = Appointment.objects.get(id=id)
    form = AppointmentForm(request.POST,instance = updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html')

def register(request):
    if request.method == 'POST':
          members =  Member(
            name = request.POST['name'],
            username = request.POST['username'],
            password = request.POST['password']
        )
          members.save()
          return redirect('/login')
    else:
        return render(request, 'register.html')





def login(request):
    return render(request, 'login.html')


