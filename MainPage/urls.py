from os import name
from django.urls import path
from . import views 

urlpatterns=[
    path('',views.main, name='main'),
    path('index',views.index, name='index'),
    path('Dindex',views.Dindex, name='Dindex'),
    path('aboutHD',views.aboutHD, name='aboutHD'),
    path('predictHD',views.predictHD, name="predictHD"),
    path('predictDD',views.predictDD, name="predictDD"),
    path('Type', views.Type, name='Type'),
    path('DTypes', views.DTypes, name='DTypes'),
    path('Prevention', views.Prevention, name="Prevention"),
    path('DPrevention', views.DPrevention, name="DPrevention"),
    path('Symptoms', views.Symptoms, name="Symptoms"),
    path('Treatment', views.Treatment, name="Treatment"),
    path('Causes', views.Causes, name="Causes"),
    # path('index',views.index, name='index'),
]