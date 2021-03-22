from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post

#ブログ記事一覧
def blog_list(request):
    blogs = Post.objects.all()
    return render(request, 'blog/post_list.html', {"blogs":blogs})

#ブログ記事の各々の詳細
def blog_detail(request, blog_id):
    blog = Post.objects.get(id=blog_id)
    return render(request, 'blog/post_detail.html', {"blog":blog})

#リダイレクトの説明
def redirect_sample(request):
    return redirect("post_list")

#ブログにいいねできるように
def blog_good(request, blog_id):
    blog = Post.objects.get(id=blog_id)
    blog.good += 1
    blog.save()
    return redirect('post_detail',blog_id=blog_id)