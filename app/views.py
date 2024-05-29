from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        DTFO=TopicForm(request.POST)
        if DTFO.is_valid():
            DTFO.save()
            return HttpResponse('Data Inserted into topic')
        else:
            return HttpResponse("Else block")
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=WebpageForm()
    d={"EWFO":EWFO}
    if request.method=='POST':
        DWFO=WebpageForm(request.POST)
        if DWFO.is_valid():
            DWFO.save()
            return HttpResponse('Data Inserted into Webpage')
        else:
            return HttpResponse("Else block")
    return render(request,'insert_webpage.html',d)

def insert_Accessrecord(request):
    EAFO=AccessRecordForm()
    d={"EAFO":EAFO}
    if request.method=='POST':
        DAFO=AccessRecordForm(request.POST)
        if DAFO.is_valid():
            DAFO.save()
            return HttpResponse('Data Inserted into AccessRecord')
        else:
            return HttpResponse("Else block")
    return render(request,'insert_Accessrecord.html',d)