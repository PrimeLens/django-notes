from django.shortcuts import render

from django.http import HttpResponse


from django.http import Http404

from streams.models import Post


# def index(request):
#   return HttpResponse('<p>hello world<p/>')


def index(request):
  posts = Post.objects.all()
  return render(request, 'index.html', {
    'posts': posts,     # note here var name is plural
  })

