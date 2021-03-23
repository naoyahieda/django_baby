from django.http import HttpResponse
from django.urls import path
from .views import blog_list,blog_detail,blog_good,redirect_sample

urlpatterns = [
    path('list/',blog_list,name="post_list"),
    path('<int:blog_id>/',blog_detail,name="post_detail"),
    path('redirect/',redirect_sample),
    path('<int:blog_id>/good',blog_good,name="post_good"),
]