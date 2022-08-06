from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('allpost', views.allpost, name='allpost'),
    path('bash', views.bash, name='bash'),
    path('bash/<str:post_title>', views.bash, name='bash'),
]