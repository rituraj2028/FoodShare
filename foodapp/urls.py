from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('donate/', views.donate_food, name='donate'),
    path('available/', views.available_food, name='available'),
]
