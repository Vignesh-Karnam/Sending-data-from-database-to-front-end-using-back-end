from django.shortcuts import render
from app.models import *

# Create your views here.
def dept(request):
    DO=Dept.objects.all()
    d={'Dept':DO}
    return render(request,'dept.html',d)


def emp(request):
    EO=Emp.objects.all()
    d={'emp':EO}
    return render(request,'emp.html',d)