from django.shortcuts import render,redirect
from .models import goal
import datetime
def index(request):
    goal_=goal.objects.all()
    return render(request,'index.html',{'goal_':goal_})

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
