from django.urls import path
from Login_App import views

app_name = "Login_App"

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.editprofile_view, name='edit'),
    path('logout/', views.logout_view, name='logout'),
]