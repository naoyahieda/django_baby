from django.contrib import admin
from .models import Post

#admin.pyの役割は、管理サイトで操作できるように登録すること。

#ブログの記事(Post)を管理サイトに登録
admin.site.register(Post)