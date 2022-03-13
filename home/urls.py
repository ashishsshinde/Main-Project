from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='register'),
    path('UserRegistration/',views.UserRegistration,name='UserRegistration'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('login/',views.LoginUser,name='login'),
    path('student/',views.student,name='student'),
    path('contact/',views.contact1,name='contact1'),
    path('buy/',views.buy,name='buy'),
    path('call/',views.visit,name='visit'),
]
