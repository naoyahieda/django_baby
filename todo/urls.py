from django.http import HttpResponse
from django.urls import path
from . import views

def hello_blog_func(request):
    return HttpResponse("<h1>Todoアプリを作っていきましょう！</h1>")

urlpatterns = [
    path('hello/',hello_blog_func),
    path('list/',views.list_func,name="todo_list"),
    path('<int:number>/',views.detail_func,name="todo_detail"),
    path('<int:number>/delete',views.delete_func,name="todo_delete"),
    path('search/',views.search_func,name="todo_search"),
]