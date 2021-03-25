#admin.pyの役割は、管理サイトで操作できるように登録すること
from django.contrib import admin
from .models import Todo

#下の一行はTodoのモデルを管理サイトで扱えるよう登録
admin.site.register(Todo)