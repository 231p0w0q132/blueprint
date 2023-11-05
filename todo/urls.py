from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [ 
    path('',views.index,name='index'),
    path('make_goal',views.make_goal,name='make_goal'),
]
