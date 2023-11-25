from Posts_App import views
from django.urls import path


app_name = 'Posts_App'

urlpatterns = [
    path('', views.home, name='home'),
    path('like/<pk>/', views.liked_view, name='like'),
    path('unlike/<pk>/', views.unlike_view, name='unlike'),
]