from django.urls import path
from blog.views import blogListView, post_details

urlpatterns = [
    path('', blogListView, name='blog_list'),
    path('post/<int:pk>', post_details, name='post_details'),

]