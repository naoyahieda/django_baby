from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render
#Hello Worldをブラウザに返す関数
def hello_func(request):
    return HttpResponse("Hello World")

urlpatterns = [
    path('hello/',hello_func), #localhost:8000/helloときたらhello_funcを実行する。
    path('blog/', include('blog.urls')),#blog/urls.pyにhttp://〇〇.△△/blog/~ の処理を全て任せている。
    path('todo/', include('todo.urls')),#上と同じ、Todoバージョン
    path('admin/', admin.site.urls),#管理サイトをDjangoが自動で生成
]
