from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
#Hello Worldをブラウザに返す関数
def hello(request):
    return HttpResponse("Hello World")

def html(request):
    return render(request, 'base.html')

urlpatterns = [
    path('hello/',html),
    path('admin/', admin.site.urls),
]
