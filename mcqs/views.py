from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import MCQ

def index(request):
    all_mcq = MCQ.objects.all()
    context={'all_mcq' : all_mcq,}
    return render(request,'mcqs/index.html',context)

def list(request , num):
    #mcq=MCQ.objects.get(pk=num)

    all_mcq = MCQ.objects.all()
    try:
        for mcq in all_mcq:
            if(mcq.id == int(num)):
                s='<center></center>'
                strval="<center><h2>Details of question:</h2><br><h2> "+\
                    str(mcq.ca)+"</h2> <br><h2>"+\
                    str(mcq.wa1)+"</h2><br> <h2>"+\
                    str(mcq.wa2)+"</h2><br></center>"
                return HttpResponse(s + strval)
    except MCQ.DoesNOtExist:
        raise Http404("MCQ not exist")
