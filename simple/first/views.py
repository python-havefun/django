from django.shortcuts import render,get_object_or_404
#from django.template import loader
from django.http import Http404, HttpResponseRedirect,HttpResponse
from .models import Question
from .form import QuestionForm

def index(request,question_id):
    q=get_object_or_404(Question,id=question_id)
    return render(request,'first/index.html',{'data':q})

def details(request):
    q=Question.objects.all()
    context={'data':q,}
    return render(request,'first/details.html',context)

def user_data(request):
    l=[]
    l.append(request.path)
    l.append(request.get_host())
    l.append(request.get_full_path())
    l.append(request.is_secure())
    l.append(request.META['HTTP_USER_AGENT'])
    #l.append(request.META['HTTP_REFRER'])
    #l.append(request.META(['REMOTE_ADDR']))
    cont={'use':l,}
    return render(request,'first/user_details.html',cont)

def search_form(request):
    return render(request, 'first/search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q=request.GET['q']
        try:
            s=Question.objects.get(question_title=q)
            return render(request,'first/search_data.html',{'s':s})
        except:

            return render(request,'first/search_form.html',{'error':True})
    else:
        return render(request,'first/search_form.html',{'empty':True})

def QuesForm(request):
    if request.method =='POST'
        form=QuestionForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
 

