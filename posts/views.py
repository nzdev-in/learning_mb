from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from . models import PostModel

class FrontPage(TemplateView):
    template_name = "base.html"

class PostListView(ListView):
    model = PostModel
    template_name = "list.html"
    context_object_name = 'all_posts'
