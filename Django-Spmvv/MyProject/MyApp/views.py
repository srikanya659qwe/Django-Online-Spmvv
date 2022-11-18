from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hai(request):
	return HttpResponse("Hai guys welcome to django session")

def hello(request):
	return HttpResponse("<h3 style=color:red;background-color:navy><center>django workshop</center></h3>")

def dynamic(request,id):
	return HttpResponse("<center><h1 style=color:pink>my rollnumber is:{}</h1></center>".format(id))

def data(request,name):
	return HttpResponse("<center><h2 style=background-color:yellow>My name is:{}</h2></center>".format(name))

def task(request,a,b):
	return HttpResponse("<h1>My rollnumber is :{} and My name is:{}</h1>".format(a,b))

def temp(request):
	return render(request,'temp.html',{})

def table(request):
	return render(request,'table.html')

def get(request,n,m):
	return render(request,'get.html',{'id':n,'name':m})

def inline(request):
	return render(request,'inline.html',{})

def internal(request):
	return render(request,'internal.html',{})

def external(request):
	return render(request,'external.html',{})