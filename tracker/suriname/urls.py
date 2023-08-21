from django.urls import path,include
from . import views


urlpatterns = [
    path('home/',views.home,name='home'),
    path('update/',views.update_status,name='update_status'),
]
