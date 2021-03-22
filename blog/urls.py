from django.http import HttpResponse
from django.urls import path
#Hello Blogをブラウザに返す関数
def hello_blog(request):
    return HttpResponse("Hello Blog")

urlpatterns = [
    path('hello/',hello_blog),
]