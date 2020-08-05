from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post

# Create your views here.


class PostView(TemplateView):
    template_name = "post/homepage.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_posts"] = Post.objects.all()
        return context
