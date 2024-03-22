from django.urls import path
from . import views

urlpatterns = [
    path('',views.clone,name='clone')
]
