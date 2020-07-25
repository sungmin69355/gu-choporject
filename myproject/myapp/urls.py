from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('write_diary',views.write_diary,name='write_diary'),
]