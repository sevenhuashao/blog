from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

from .models import Comment
from .forms import CommentForm

# Create your views here.


def post_comment(request, post_pk):
    # 先获取被评论的文章，因为后续需要将评论和被评论的文章关联起来
    # 这里我们使用Django 提供的一个快捷函数 get_object_or_404
    # 这个函数的作用是当获取的文章Post存在时，则获取， 否则返回404页面给用户
    post = get_object_or_404(Post, pk=post_pk)



    # HTTP请求有get 和post两种，一般用户通过表单提交数据都是通过post请求
    # 因此只有当用户的请求为post时才需要处理表单数据
    if request.method == 'POST':
        # 用户提交的数据存在request.POST中，这是一个类字段对象
        # 我们利用这些数据构造了CommentForm的实例，这样Django的表单就生成了
        form = CommentForm(request.POST)

        if form.is_valid():
            # 检查数据是否合同， 调用表单的save方法保存数据到数据库
            # commit=False的作用是利用表单的数据生成Comment模型累的实例，但还不保存评论数据到数据库
            comment = form.save(commit=False)

            # 将评论和被评论的文章关联起来
            comment.post = post

            # 最终将评论数据保存进数据库， 调用模型实例的save方法
            comment.save()
            # 重定向到post的详情页，实际上当redirect函数接收到一个模型的实例时，它会调用这个模型实例的get_absolute
            # 然后重定向到get_absolute_url 方法返回URL
            return redirect(post)
        else:

            # 检查到数据不合法，重新渲染详情页，并渲染表单的错误。
            # 因此我们传了三个模版变量给detail.html
            # 一个是文章Post， 一个是评论列表， 一个是表单Form
            # 注意我们这边用到了post.comment_set.all()方法
            # 这个用法有点类似与Post.objects.all()
            # 其作用是获取这篇post下的所有评论
            # 因为post 和 comment是Foreignkey关联的，因此私用post.comment_set.all()反响查询全部评论。
            comment_list = post.comment_set.all()
            context = {
                'post': post,
                'form':form,
                'comment_list': comment_list
            }
            return render(request, 'blog/detail.html', context=context)

    return redirect(post)
