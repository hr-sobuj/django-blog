from django.urls import path
from . import views 

app_name='App_Login'

urlpatterns=[
    path('registration/',views.Registration,name='registration'),
    path('login/',views.LoginView,name='login'),
    path('profile/',views.ProfileView,name='profile'),
    path('logout/',views.LogoutView,name='logout'),
    path('update/',views.UpdateProfileView,name='update'),
    path('password/',views.ChangePassword,name='password'),
    path('addpropic/',views.AddProfilePicView,name='addpropic'),
    path('updatepropic/',views.UpdataProfilePicView,name='updatepropic'),
]