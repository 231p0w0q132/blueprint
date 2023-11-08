from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [ 
    path('',views.index,name='index'),
    path('make_goal',views.make_goal,name='make_goal'),
    path('read_more/<int:fir>',views.read_more,name='read_more'),
    path('suc_gl/<int:fir>',views.suc_gl,name='suc_gl'),
]
