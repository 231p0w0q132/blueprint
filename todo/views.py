from django.shortcuts import render,redirect,get_object_or_404
from .models import goal,cle_gl
from django.core.paginator import Paginator
import datetime
def index(request):
    page = int(request.GET.get('page',0))
    if page>=1 :
        page= page-1
    goal_=goal.objects.all()
    finish_=cle_gl.objects.all()[page*10:page*10+10] 
    return render(request,'index.html',{'goal_':goal_,'finish_':finish_})

def make_goal(request):
    
    if request.method == 'POST':
        subject=request.POST.get('subject')
        content=request.POST.get('content')
        end_date=request.POST.get('end_date')
        now=datetime.datetime.now()
        create_date=str(now)[:10]
        print(end_date)
        print(create_date)
        q=goal(subject=subject,content=content,create_date=create_date,end_date=end_date)
        q.save()
        return redirect('todo:index')
    return render(request,'make_goal.html')

def read_more(request,fir):
    if request.method == 'POST':
        q=get_object_or_404(goal,pk=fir)
        q.subject=request.POST.get('subject')
        q.content=request.POST.get('content')
        q.end_date=request.POST.get('end_date')
        q.save()
        return redirect('todo:index')
    return render(request,'edit_goal.html',{'val':get_object_or_404(goal,pk=fir)})

def suc_gl(request,fir):
    if request.method=='GET':
        cg=cle_gl()
        q=get_object_or_404(goal,pk=fir)
        cg.subject=q.subject
        cg.cre_date=q.create_date
        cg.end_date=str(datetime.datetime.now())[:10]
        cg.save()
        q.delete()
        return redirect('todo:index')
