from django.shortcuts import render
from .models import Vehicle_Details

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def home(request):
    dest1=Vehicle_Details.objects.all()
    return render(request,'home.html',{"dest1":dest1})

def vehicle(request,pk):
    dest2 = Vehicle_Details.objects.get(id=pk)
    return render(request,"vehicle.html",{"dest2":dest2})