from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.


def post_list(request):
    posts = Post.objects.filter(
        publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
