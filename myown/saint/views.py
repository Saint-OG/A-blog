# from django.shortcuts import render

# # Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Students


def index(request):
  mystudents = Students.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mystudents' : mystudents,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))


def addrecord(request):
  a = request.POST['first']
  b = request.POST['last']
  c = request.POST['dob']
  d = request.POST['course']
  e = request.POST['sex']
  f = request.POST['matric']
  g = request.POST['number'] 
  mystudents = Students(first_name=a, last_name=b, date_of_birth=c, course=d, Sex=e, matric=f, phone_number=g)
  mystudents.save()
  return HttpResponseRedirect(reverse('index'))


def delete(request, id):
  mystudents = Students.objects.get(id=id)
  mystudents.delete()
  return HttpResponseRedirect(reverse('index'))


def update(request, id):
  mystudents = Students.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mystudents' : mystudents,
  }
  return HttpResponse(template.render(context, request))


def updaterecord(request, id):
  a = request.POST['first']
  b = request.POST['last']
  c = request.POST['dob']
  d = request.POST['course']
  e = request.POST['sex']
  f = request.POST['matric']
  g = request.POST['number'] 
  student = Students.objects.get(id=id)
  student.first_name=a
  student.last_name=b
  student.date_of_birth=c
  student.course=d
  student.Sex=e
  student.matric=f
  student.phone_number=g
  student.save()
  return HttpResponseRedirect(reverse('index'))