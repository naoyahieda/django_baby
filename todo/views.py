from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo

#Todoリスト表示
def list_func(request):
    todo_list = Todo.objects.all() #これでデータベースからすべてのTodoリストをとってくる。
    return render(request, 'todo/list.html', {"todo_list":todo_list})

#Todoの詳細を表示する関数
def detail_func(request,number):
    print(number) 
    todo = Todo.objects.get(id=number) #Todoリストの中でidがnumber番のものを取得
    return render(request, 'todo/detail.html', {"todo":todo})

#Todoを削除し、一覧に戻る関数
def delete_func(request,number):
    todo = Todo.objects.get(id=number) #Todoリストの中でidがnumber番のものを取得
    todo.delete()
    return redirect("todo_list")

#Todoを検索し、表示する関数
def search_func(request):
    search_word = request.GET["query"] #URLの最後にくっついた検索ワードを取得
    print(search_word)
    try:
        todo = Todo.objects.get(title=search_word) #Todoリストのタイトルがsearch_wordのものを取得
        return render(request, 'todo/detail.html', {"todo":todo})
    except:
        return HttpResponse(search_word+"の検索結果はみつかりませんでした。")