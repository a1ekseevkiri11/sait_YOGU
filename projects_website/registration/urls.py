from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as registration_views


urlpatterns = [
    path('profile/', registration_views.profile, name='profile'),
    path('profileCustomer/', registration_views.CustomerProfile.as_view(), name='profileCustomer'),
    path('profileLecturer/', registration_views.LecturerProfile.as_view(), name='profileLecturer'),
    path('profileStudent/', registration_views.StudentProfile.as_view(), name='profileStudent'),
    path('login/', registration_views.CustomLoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]
