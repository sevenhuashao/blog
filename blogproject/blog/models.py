from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

# Create your models here.


class Category(models.Model):
    # 文章目录
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    # 文章标签
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=70)
    # 文章内容
    body = models.TextField()
    # 文章创建时间
    created_time = models.DateTimeField()
    # 文章最后一次修改时间
    modified_time = models.DateTimeField()
    # blank=True ，参数之后就可以允许为空值
    # 文章摘要，可以允许为空值
    excerpt = models.CharField(max_length=200, blank=True)
    # 文章分类
    category = models.ForeignKey(Category)
    # 文章标签，可以允许为空值，一个文章可以有多个标签
    tags = models.ManyToManyField(Tag, blank=True)
    # 文章作者，User为django.contrib.auth,models导入的，通过ForeignKey把文章与User关联
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    # Django允许我们在models.Model的子类里定义一个Meta的内部类，这个内部类通过制定的一些属性来规定这个类的一些特性
    # 如我们在这里要制定Post的排序方式，首先看Post的代码：
    class Meta:
        ordering = ['-created_time']
