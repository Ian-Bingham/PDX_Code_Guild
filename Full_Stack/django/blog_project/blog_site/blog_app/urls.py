from django.urls import path
from . import views


app_name = 'blog_app'  # for namespacing
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('make_post/', views.make_post, name='make_post'),
    path('post_detail/<str:blog_id>', views.post_detail, name='post_detail'),
    path('make_comment/<str:blog_id>', views.make_comment, name='make_comment'),
]
