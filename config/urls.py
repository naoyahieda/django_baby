from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render
#Hello Worldをブラウザに返す関数
def hello_func(request):
    return HttpResponse("Hello World")

urlpatterns = [
    path('hello/',hello_func),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
