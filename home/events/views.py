from django.shortcuts import render,HttpResponse
from events.models import Post

# Create your views here.
def events(request):
    allPosts = Post.objects.all()
    return render(request, 'events.html', {'allPosts': allPosts})

def eventPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request, 'eventsPost.html', context)

def about(request):
    return render(request, 'about.html')

def search(request):
    query = request.GET['query']
    allPosts = Post.objects.filter(title__icontains=query)
    params = {'allPosts': allPosts }
    return render(request, 'search.html', params)