from django.urls import path
from . import views

urlpatterns = [
    path('fetch/', views.fetch_data),
    path('api/', views.NewsAPI.as_view()),

   
   
]


