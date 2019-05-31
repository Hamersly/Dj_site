from django.shortcuts import render
from django.views.generic import View
from django.urls import reverse
from django.shortcuts import reverse
from .utils import *
from .models import Post, Tag
from .forms import TagForm, PostForm
from django.shortcuts import redirect
# Ниже, что бы скрыть от неавторизованных пользователей что-либо.
# from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blogg/index.html', context={'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blogg/post_detail.html'


class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blogg/post_create.html'
    # raise_exception = True

class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    form_model = PostForm
    template = 'blogg/post_update.html'
    # raise_exception = True

class PostDelete(ObjectDeleteMixin,View):
    model = Post
    template = 'blogg/post_delete.html'
    redirect_url = 'posts_list_url'
    # raise_exception = True


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blogg/tags_list.html', context={'tags': tags})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blogg/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blogg/tag_create.html'
    # raise_exception = True

class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    form_model = TagForm
    template = 'blogg/tag_update.html'
    # raise_exception = True

class TagDelete(ObjectDeleteMixin,View):
    model = Tag
    template = 'blogg/tag_delete.html'
    redirect_url = 'tags_list_url'
    # raise_exception = True
    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     return render(request, 'blogg/tag_delete.html', context={'tag': tag})
    #
    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     tag.delete()
    #     return redirect(reverse('tags_list_url'))