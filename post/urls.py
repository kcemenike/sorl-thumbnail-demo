from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.PostView.as_view(), name='home')
]
