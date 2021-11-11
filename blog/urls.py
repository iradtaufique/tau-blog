from django.urls import path
from blog.views import (blogListView, post_details, financial_posts,
                        business_posts,travels_posts, technology_posts,
                        update_comment, delete_comment)

urlpatterns = [
    path('', blogListView, name='blog_list'),
    path('post/<int:pk>', post_details, name='post_details'),

    path('post/finance', financial_posts, name='finance_posts'),
    path('post/business', business_posts, name='business_posts'),
    path('post/travel', travels_posts, name='travel_posts'),
    path('post/technology', technology_posts, name='technology_posts'),

    path('edit-comment/<int:id>', update_comment, name='edit_comment'),
    path('delete-comment/<int:id>', delete_comment, name='delete_comment'),

]