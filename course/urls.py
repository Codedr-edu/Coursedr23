from django.urls import path
from . import views

urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('learn/',views.Add_form,name='add_form'),
    path('thank/',views.thank,name='thank'),
    path('admin/home/',views.admin_home.as_view(),name='admin_home'),
    path('accounts/login/',views.LoginPage,name='a_login'),
    path('accounts/signup/',views.SignupPage,name='signup'),
    path('accounts/logout/',views.LogoutPage,name='log_out'),
    path('course/add/',views.Course_form,name='course_form'),
    path('complete/',views.complete,name='done_deal')
]