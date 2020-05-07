from django.urls import path
from basic_app import views

app_name = "basic_app"


urlpatterns = [
    path('register/', views.register, name='register'),
]
