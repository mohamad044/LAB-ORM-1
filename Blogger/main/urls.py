from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home_view,name='home_view'),
    path('create_post/',views.create_post_view,name='create_post_view'),
    path('post/detail/<post_id>',views.post_detail_view,name='post_detail_view'),
    path('post/update/<post_id>',views.post_update_view,name='post_update_view'),
    path('post/delete/<post_id>',views.post_delete_view,name='post_delete_view'),
    path('dark_mode/',views.dark_mode_view,name='dark_mode_view'),
    path('post/search',views.search_post_view,name='search_post_view'),
    path('post/<post_id>/comment/',views.add_comment_view,name='add_comment_view')
]
