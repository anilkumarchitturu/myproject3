from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def getinput(request):
    return render(request,'getinput.html')
def getadd(request):
    x = request.GET["t1"]
    y = request.GET["t2"]
    z = int(x)+int(y)
    res = HttpResponse("sum is:"+str(z))
    return res
def postinput(request):
    return render(request,'postinput.html')
def postadd(request):
    x = request.POST["t1"]
    y = request.POST["t2"]
    z = int(x)+int(y)
    res = HttpResponse("sum is:"+str(z))
    return res

