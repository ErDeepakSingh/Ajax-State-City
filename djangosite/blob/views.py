from django.shortcuts import render
from . import models as blob_models


# Create your views here.
def blob_home(request):
    context = {
        'posts': blob_models.Post.objects.all()
    }
    return render(request, 'blob/blob_home.html', context)


def blob_post(request, post_id=None):
    post=blob_models.Post.objects.get(id=post_id)
    context = {
        'blob_post': post
    }
    return render(request, 'blob/blob_post.html',
                  context)
