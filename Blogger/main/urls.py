from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home_view,name='home_view'),
    path('create_post/',views.create_post_view,name='create_post_view'),
    path('dark_mode/',views.dark_mode_view,name='dark_mode_view')
]
